import pandas as pd

from PySide2.QtCore import QDate

from src import database
from src.SonetUtils import TripType, sonet_log, SonetLogType


class SonetTrajectoryFilter:
    """
        This class purpose is to host the set of conditions (aka filter) to be applied to SonetSpacecraft's trajectories.
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
    def __init__(self, a_trip_type=TripType.NA):
        self._data = pd.DataFrame(columns=['Status', 'Type', 'Filter'])

        if not TripType.is_valid(a_trip_type):
            sonet_log(SonetLogType.ERROR, 'SonetTrajectoryFilter.__init__."Wrong TripType passed as argument"')

        self._trip_type = a_trip_type

    # Public methods
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
        # Get activated filters as pandas DataFrame.
        the_filter_energy = self._get_activated_filters_of_a_given_type(self._data, True, 'Energy')
        the_filter_tof = self._get_activated_filters_of_a_given_type(self._data, True, 'Time of flight')
        the_filter_dates = self._get_activated_filters_of_a_given_type(self._data, True, 'Date')
        the_filter_dates2 = self._get_activated_filters_of_a_given_type(self._data, True, '???')

        # Convert them to string.
        query_energy = self._get_query_string(the_filter_energy, a_type='Energy')
        query_tof = self._get_query_string(the_filter_tof, a_type='Time of flight')
        query_dates = self._get_query_string(the_filter_dates, a_type='Date')
        query_dates2 = self._get_query_string(the_filter_dates2, a_type='???')

        # Some of them can be empty, so not include them in the resultant query string.
        query_list = []
        for q in [query_energy, query_tof, query_dates, query_dates2]:
            if len(q) != 0:
                query_list.append(q)
        # Resultant query string.
        query_string = ' and '.join(query_list)

        # The porkchop dataframe
        the_pcp_table = database.get_pcp_table(self._trip_type)

        # Check, the_pcp_table shall be a dataframe
        if not isinstance(the_pcp_table, pd.DataFrame):
            sonet_log(SonetLogType.ERROR, 'SonetTrajectoryFilter.get_filtered_pcp."Returned type is not a dataframe"')
            return False

        # Check, if empty query string, return the pcp DataFrame with no filter.
        if not query_string:
            return self.convert_pcp_table_to_human_format(the_pcp_table.copy()) # hex(id(variable_here)) to see variable address.
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

    def set_data(self, a_data):
        """
        Setter method.
        :param a_data: a dataframe
        """
        # Check that input is a pandas DataFrame.
        if not isinstance(a_data, pd.DataFrame):
            return False

        # Check columns.
        if not list(a_data.columns) == ['Status', 'Type', 'Filter']:
            return False

        self._data = a_data.copy()
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

    # Private methods
    def _get_activated_filters_of_a_given_type(self, a_filter, a_activated, a_filter_type):
        return a_filter.loc[(a_filter['Status'] == a_activated) & (a_filter['Type'] == a_filter_type), 'Filter'].copy()

    def _get_query_string(self, a_filter, a_type=''):
        """
        The user can add any number of Energy/TOF/Dates filters to a_filter, get
        them as a Python list and then concatenate them with 'AND', finally returning them as a query string.

        Example of input filters:
         - Energy: [dvt, ==, 6, km/s ]
         - Time of flight:
         - Date: ['Departs','Earth','On', '01-05-2020']
        """
        query_list = []

        if a_type == 'Energy' or a_type == 'Time of flight':
            for f in list(a_filter):
               query_list.append(' '.join(f[0:2]) + ' ' + str(f[2]))
        elif a_type == 'Date':
            # ['Departs', 'Earth', 'On', '01-05-2020']
            # ['Arrives', 'Earth', 'On', '01-05-2020']

            # ['Departs', 'Mars', 'On', '01-05-2020']
            # ['Arrives', 'Mars', 'On', '01-05-2020']

            # [  ...    ,  ...  , 'On/Before/After', 'TAL']

            for f in list(a_filter):
                aux = self.convert_filter_to_query_format(f)
                query_list.append(aux[0] + ' ' + aux[2] + ' ' + str(aux[3]))


        # Get the filters, as a unique string.
        query = ' and '.join(query_list)
        return query

    def convert_filter_to_query_format(self, a_filter):
        """
        Convert a human readable filter to a machine friendly one.

        Example of input filter: ['Departs', 'Earth', 'On', '01-05-2020']
        """
        # TODO: Warning! if-else labyrinth following... Not efficient but not needed at this stage.
        action = a_filter[0]
        planet = a_filter[1]  # No importa, the calling function knows if the spc is departing/arriving to/from Earth/Mars.
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
        # Check that input is a dataframe.
        # Check that input has right format.
        # TODO: Convert all the dataframe dates rows each time it is called will
        #  slow down the code... performance issue :(.
        #if isinstance(a_pcp_table.iloc[0].DepDates) == QDate:
        #    stop = True
        # Convert DepDates & ArrivDates from JD to Gregorian calendar.
        a_pcp_table['DepDates'] = (a_pcp_table.DepDates).apply(QDate.fromJulianDay)
        a_pcp_table['ArrivDates'] = (a_pcp_table.ArrivDates).apply(QDate.fromJulianDay)

        return a_pcp_table