import pandas as pd
from PySide2.QtCore import QDate

from src import database
from src.SonetUtils import TripType, sonet_log, SonetLogType


# ==============================================================================================
# ==============================================================================================
#
#
#                                    CLASS SonetTrajectoryFilter
#
#
# ==============================================================================================
# ==============================================================================================

class SonetTrajectoryFilter:
    """
        This class purpose is to host the set of conditions (aka filter) to be applied to SonetSpacecraft trajectories.
        Each SonetSpacecraft will have at least one SonetTrajectoryFilter object, which will implement the filtering
        functionality.

        The filter, here stored as _data,  is a Pandas dataframe with the following structure:
        |Status  | Type    | Filter                |
        |  1     |  Energy | filter1 activated...  |
        |  0     |  Dates  | filter2 deactivated...|
        |  0     |  Tof    | filter3 deactivated...|

        The status column, holds a boolean indicating if the filter is currently enabled or not.
        The type column, holds the type of the filter, indicating which porkchop plot variable is affecting.
        The filter column, holds the filter, as a Python list of strings.
    """

    def __init__(self, a_parent, a_trip_type=TripType.NA):
        """
        :param a_parent: pointer to the parent, a s/c to which pertains this filter.
        :param a_trip_type: the type of trip to which apply this filter, OUTGOING|INCOMING.
        """
        self._data = pd.DataFrame(columns=['Status', 'Type', 'Filter'])

        if not TripType.is_valid(a_trip_type):
            sonet_log(SonetLogType.ERROR, 'SonetTrajectoryFilter.__init__."Wrong TripType passed as argument"')

        self._p_the_spacecraft = a_parent
        self._trip_type = a_trip_type

    @staticmethod
    def convert_simple_dats_filter_to_query_format(a_filter):
        """
        Convert a human readable filter to a machine friendly one.

        Example of input filter: ['Departs', 'Earth', 'On', '01-05-2020']
        """
        # TODO: Warning! if-else labyrinth following... Not efficient but not needed at this stage.
        action = a_filter[0]
        planet = a_filter[1]
        # No importa, the calling function knows if the spc is departing/arriving to/from Earth/Mars.
        operator = a_filter[2]
        date = a_filter[3]

        # Convert action to query format (e.g. the table column's name).
        if action == 'Departs':
            action = 'DepDates'
        elif action == 'Arrives':
            action = 'ArrivDates'

        # Convert planet to query format.
        pass

        # Convert operator to query format.
        if operator == 'On':
            operator = '=='
        elif operator == 'Before':
            operator = '<='
        elif operator == 'After':
            operator = '>='

        # Convert date to query format.
        date = QDate.toJulianDay(QDate.fromString(date, 'dd-MM-yyyy'))

        return [action, planet, operator, date]

    @staticmethod
    def convert_pcp_table_to_human_format(a_pcp_table):
        # Convert DepDates & ArrivDates from JD to Gregorian calendar.
        a_pcp_table['DepDates'] = a_pcp_table.DepDates.apply(QDate.fromJulianDay)
        a_pcp_table['ArrivDates'] = a_pcp_table.ArrivDates.apply(QDate.fromJulianDay)

        return a_pcp_table

    def get_data(self):
        """
        Getter method.
        Gets the internal data.
        :return: a pandas dataframe.
        """
        return self._data

    def get_filtered_pcp(self):
        """
        La clave.
        Applies the filter _data to the porkchop plot, and returns a filtered pandas Dataframe.
        If the _data dataframe is empty, the return will be the porkchop plot with no filter applied.
        If the filter is too restrictive, then the return will be an empty DataFrame.
        :return: A pandas DataFrame. If something went wrong, then it will return False.
        """
        # If not available pcp in the db, return empty dataframe.
        the_pcp_table = database.get_pcp_table(self._trip_type)
        if the_pcp_table.empty:
            return the_pcp_table

        # Get activated filters as pandas DataFrame.
        the_filter_energy = SonetTrajectoryFilter._get_activated_filters_of_a_given_type(self._data, True, 'Energy')
        the_filter_tof = SonetTrajectoryFilter._get_activated_filters_of_a_given_type(self._data, True,
                                                                                      'Time of flight')
        the_filter_simple_dates = SonetTrajectoryFilter._get_activated_filters_of_a_given_type(self._data, True,
                                                                                               'SimpleDate')
        the_filter_complex_dates = SonetTrajectoryFilter._get_activated_filters_of_a_given_type(self._data, True,
                                                                                                'ComplexDate')

        # Convert them to string.
        query_energy = self._get_query_string(the_filter_energy, a_type='Energy')
        query_tof = self._get_query_string(the_filter_tof, a_type='Time of flight')
        query_simple_dates = self._get_query_string(the_filter_simple_dates, a_type='SimpleDate')
        query_complex_dates = self._get_query_string(the_filter_complex_dates, a_type='ComplexDate')

        # Some of them can be empty, so not include them in the resultant query string.
        query_list = []
        for q in [query_energy, query_tof, query_simple_dates, query_complex_dates]:
            if len(q) != 0:
                query_list.append(q)
        # Resultant query string.
        query_string = ' and '.join(query_list)

        # Check, the_pcp_table shall be a dataframe
        if not isinstance(the_pcp_table, pd.DataFrame):
            sonet_log(SonetLogType.ERROR, 'SonetTrajectoryFilter.get_filtered_pcp."Returned type is not a dataframe"')
            return False

        # Check, if empty query string, return the pcp DataFrame with no filter.
        if not query_string:
            return self.convert_pcp_table_to_human_format(the_pcp_table.copy())
            # hex(id(variable_here)) to see variable address.
        else:
            try:
                # Return the filtered porkchop plot.
                res = the_pcp_table.query(query_string)
                return self.convert_pcp_table_to_human_format(res.copy())
            except KeyError:
                print('Error in SonetTrajectoryFilter.get_filtered_pcp: Wrong _trip_type')
                return False

    def get_trip_type(self):
        """
        Getter function.
        :return:
        """
        return self._trip_type

    @staticmethod
    def _get_activated_filters_of_a_given_type(a_filter, a_activated, a_filter_type):
        return a_filter.loc[(a_filter['Status'] == a_activated) & (a_filter['Type'] == a_filter_type), 'Filter'].copy()

    def _get_query_string(self, a_filter, a_type='') -> str:
        """
        Convert a input filter to a queryable string.
        The user can add any number of Energy/TOF/Dates filters to a_filter, get
        them as a Python list and then concatenate them with 'AND', finally returning them as a query string.

        Example of input filters:
         - Energy: [dvt, ==, 6, km/s ]
         - Time of flight:
         - SimpleDate: ['Departs','Earth','On', '01-05-2020']
         - ComplexDate: ['Departs', 'Earth', '30', 'Days', 'After', 'DAV', 'Earth - Mars', 'Launching']
        """
        query_str = []

        if a_type == 'Energy' or a_type == 'Time of flight':
            for f in list(a_filter):
                query_str.append(' '.join(f[0:2]) + ' ' + str(f[2]))

        elif a_type == 'SimpleDate':
            for f in list(a_filter):
                aux = self.convert_simple_dats_filter_to_query_format(f)
                query_str.append(aux[0] + ' ' + aux[2] + ' ' + str(aux[3]))

        elif a_type == 'ComplexDate':
            for f in list(a_filter):
                str_1 = str_2 = str_3 = ''
                part_1 = f[0]
                part_2 = f[2]

                # Part 1 - departure or arrival.
                if part_1 == 'Departs':
                    str_1 = 'DepDates'
                elif part_1 == 'Arrives':
                    str_1 = 'ArrivDates'

                # Part 2 - operator.
                if part_2 == 'At least':
                    str_2 = '>='
                elif part_2 == 'At maximum':
                    str_2 = '<='
                elif part_2 == 'At the same time':
                    str_2 = '=='

                # Part 3 - the date.
                if part_2 in ['At least', 'At maximum']:
                    # Get the offset.
                    the_offset = int(f[3])
                    if f[5] == 'After':
                        the_offset = +1 * the_offset
                    elif f[5] == 'Before':
                        the_offset = -1 * the_offset

                    # Get the s/c.
                    the_sc = database.get_spacecraft(f[6])
                    the_date = the_sc.get_departure_arrival_date(p_trip=f[7], p_trip_event=f[8])
                    the_date = the_date + the_offset
                    str_3 = str(the_date)

                elif part_2 in ['At the same time']:

                    # Get the s/c.
                    the_sc = database.get_spacecraft(f[3])
                    the_date = the_sc.get_departure_arrival_date(p_trip=f[4], p_trip_event=f[5])
                    str_3 = str(the_date)

                # Part 4 - query string build.
                if part_2 in ['At least', 'At maximum']:
                    query_str.append(str_1 + ' ' + str_2 + ' ' + str_3)
                elif part_2 in ['At the same time']:
                    the_date_one_day_after = str(the_date + 1)
                    the_date_one_day_before = str(the_date - 1)
                    query_str.append(
                        str_1 + ' >= ' + the_date_one_day_before + ' and ' + str_1 + ' <= ' + the_date_one_day_after)

        # Get the filters, as a unique string.
        query = ' and '.join(query_str)
        return query

    def set_data(self, a_data: pd.DataFrame) -> bool:
        """
        Setter method.

        :param a_data: the filter to be applied.
        """

        sonet_log(SonetLogType.INFO, 'SonetTrajectoryFilter.set_data')

        # Check that input is a pandas DataFrame.
        if not isinstance(a_data, pd.DataFrame):
            sonet_log(SonetLogType.ERROR, 'SonetTrajectoryFilter.set_data."Wrong input type"')
            return False

        # Check columns.
        if not list(a_data.columns) == ['Status', 'Type', 'Filter']:
            sonet_log(SonetLogType.ERROR, 'SonetTrajectoryFilter.set_data."Wrong filter columns"')
            return False

        # If the filter is the same, do not apply it.
        if a_data.equals(self._data):
            return True
        else:
            # If not, set the new filter
            self._data = a_data.copy()

            # And reset the current selected trajectories for the s/c.
            self._p_the_spacecraft.reset_trajectory()
            return True

    def set_trip_type(self, a_trip_type):
        """
        Setter function.
        :param a_trip_type:cd
        :return:
        """
        if not TripType.is_valid(a_trip_type):
            return False
        self._trip_type = a_trip_type

    @staticmethod
    def update_filters_dependencies(a_the_filter):
        """
        Prepares the filters to update their dependencies.
        :param a_the_filter: a SonetTrajectoryFilter obj or a list of them
        """
        has_return_trajectory = False
        if isinstance(a_the_filter, list):
            has_return_trajectory = True

        if has_return_trajectory:
            # The s/c has got both outgoing an incoming trips.
            a_the_filter: list
            filter1: SonetTrajectoryFilter = a_the_filter[0]
            filter2: SonetTrajectoryFilter = a_the_filter[1]

            filter1.update_filter_dependencies()
            filter2.update_filter_dependencies()

        else:
            # The s/c has got only outgoing trip.
            a_the_filter: SonetTrajectoryFilter
            a_the_filter.update_filter_dependencies()

    def update_filter_dependencies(self):
        """
        Updates the filter dependencies.
            - The dependencies are introduced by the complex date filter (the one which relates a s/c dep/arriv date with
            other s/c dep/arriv date.
            - If a complex date filter isn't valid, then deactivate it and reset any selected trajectory.
        """

        # Traverse the filter dataframe, if found and activated & invalid 'ComplexDate' row, deactivate it.
        for i in range(self._data.shape[0]):
            row = self._data.iloc[i]
            if row['Status'] == 1 and row['Type'] == 'ComplexDate':
                if not SonetTrajectoryFilter.is_valid_filter(row['Filter']):
                    # The filter isn't valid anymore, deactivate it and reset any s/c selected trajectory
                    # self._data.iloc[i]['Status'] = 0 #DataFrame SettingWithCopyWarning!
                    self._data.at[i,'Status'] = 0
                    self._p_the_spacecraft.reset_trajectory(self._trip_type)

    @staticmethod
    def is_valid_filter(a_the_filter: list) -> bool:
        """
        Determines if a passed filter is still valid or not.
        First retrieve the s/c and trip to which this s/c is dependent of.
        If the s/c cannot be found, then it has been erased, so the filter is not valid anymore.
        If the s/c can be found, but among its current selected trajectories, we cannot find the one we have in our
        filter, then the filter is not valid anymore.
        :param a_the_filter: a ComplexDate filter
        """
        if a_the_filter[2] in ['At least', 'At maximum']:
            the_sc = a_the_filter[6]
            the_trip = a_the_filter[7]
        else:
            # At the same time.
            the_sc = a_the_filter[3]
            the_trip = a_the_filter[4]

        # the_sc: SonetSpacecraft
        try:
            the_sc = database.get_spacecraft(the_sc)
        except KeyError:
            # the_sc has been removed from the db.
            return False

        if the_trip in the_sc.get_trajectory_selected():
            return True
        else:
            return False
