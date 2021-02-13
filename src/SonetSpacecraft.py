import pandas as pd
from pandas import DataFrame
# from overloading import overload

from PySide2.QtCore import QModelIndex, QDate
from src.SonetTrajectoryFilter import SonetTrajectoryFilter
from src.SonetUtils import SpacecraftType, TripType, sonet_log, SonetLogType, SONET_MSG_TIMEOUT


class SonetSpacecraft:
    """
    Sonet spacecraft class.
    The spacecrafts can be:
     - Cargo/crewed.
     - One way/two way.

    A correct form to build a SonetSpacecraft object would be to declare an empty SonetSpacecraft() and then call to
    the constructing methods:
     - set_spacecraft_type()
     - set_has_return_trajectory()
     - set_filters()

    A correct form to work with the spacecraft filter would be:
     - Get a filter, with get_filter() or directly modifying the desired filter (e.g. _pcp_filter1, _pcp_filter1, or
     _pcp_filter).
     - Modify the filter's internal dataframe using the SonetTrajectoryFilter's set_data method.
     -  Get a filtered porkchop plot table with SonetTrajectoryFilter's get_filtered_pcp method.
    """
    _has_return_trajectory: bool

    def __init__(self, a_spacecraft_name=None, a_spacecraft_type_crew=None, a_spacecraft_type_return=None, ap_main_window=None):
        sonet_log(SonetLogType.INFO, 'SonetSpacecraft.__init__')

        # Instance members
        self._p_main_window = ap_main_window
        self._spacecraft_type = None
        self._has_return_trajectory = None

        self.set_spacecraft_name(a_spacecraft_name)
        self.set_spacecraft_type(a_spacecraft_type_crew)
        self.set_has_return_trajectory(a_spacecraft_type_return)
        self.set_filters()

    # Public methods
    def get_filter(self, ar_trip_type=None):
        """
        Getter method. It returns a concrete SonetTrajectoryFilter, based
        on the input a_trip_type.
        :param ar_trip_type: TripType enum.
        :rtype: SonetTrajectoryFilter
        """
        # If no trip type specified, return all the filters.
        if ar_trip_type is None:
            try:
                return self._pcp_filter
            except AttributeError:
                return [self._pcp_filter1, self._pcp_filter2]
            except TypeError:
                return False

        # Type check.
        if not isinstance(self._has_return_trajectory, bool):
            sonet_log(SonetLogType.ERROR, 'SonetSpacecraft.get_filter."Bad constructed S/C"')
            return False  # _has_return_trajectory should be bool, if not, there's some error.

        if not isinstance(ar_trip_type, TripType):
            sonet_log(SonetLogType.ERROR, 'SonetSpacecraft.get_filter."Wrong TripType"')
            return False

        if self._has_return_trajectory:
            if ar_trip_type is TripType.OUTGOING:
                return self._pcp_filter1
            elif ar_trip_type is TripType.INCOMING:
                return self._pcp_filter2
        else:
            if ar_trip_type is TripType.OUTGOING:
                return self._pcp_filter
            elif ar_trip_type is TripType.INCOMING:
                sonet_log(SonetLogType.ERROR, 'SonetSpacecraft.get_filter."Asked for incoming filter to an one-way S/C"')
                return False

    def get_filter_data(self, p_get_dataframe_copy=False):
        """
        Getter method.
        It's not the same to return a dataframe and a dataframe.copy(). get_dataframe_copy controls if we are getting
        the pointers to the original dataframes or copies of them.
         - If I return a dataframe, I am returning a pointer to the original dataframe, so all modifications are going
         to affect to the original dataframe.
         - If I return a dataframe copy, I am returning a new dataframe, so all modifications are not going to affect to
         the original dataframe.
         :param p_get_dataframe_copy: bool representing if we want original dataframes or copies.
        :return: a pandas dataframe or a list of them.
        :rtype: DataFrame
        :rtype: list
        """
        # Type check.
        if not isinstance(self._has_return_trajectory, bool):
            sonet_log(SonetLogType.ERROR, 'SonetSpacecraft.get_filter_data."Bad constructed S/C"')
            return False  # _has_return_trajectory should be bool, if not, there's some error.

        if self._has_return_trajectory:
            # If there are both outgoing and incoming trajectories, we return a list with both filter's dataframes.
            if p_get_dataframe_copy:
                return [self._pcp_filter1.get_data().copy(), self._pcp_filter2.get_data().copy()]
            else:
                return [self._pcp_filter1.get_data(), self._pcp_filter2.get_data()]
        else:
            # In case the spacecraft has no return trajectory, we just get the filter dataframe of the outgoing one.
            if p_get_dataframe_copy:
                return self._pcp_filter.get_data().copy()
            else:
                return self._pcp_filter.get_data()

    def get_has_return_trajectory(self):
        """
        Getter method.
        @return: bool. If the variable hasn't been setted, then it will return the default value,
        None, which is considered a boolean False.
        """
        return self._has_return_trajectory

    def get_spacecraft_name(self):
        """
        Getter method.

        :rtype: str
        """
        return self._spacecraft_name

    def get_spacecraft_type(self):
        """
        Getter method.
        :return: Enum (SpacecraftType). If the variable hasn't been setted, then it will return the default value,
        None, which is considered a boolean False.
        """
        return self._spacecraft_type

    def get_trajectory_selection_status(self):
        """
        Getter method.
        Returns the current trajectory selection status:
        0 if no trajectory is selected.
        0.5 if 1 out of 2 trajectories are selected (for two-way spacecrafts).
        1 if all the trajectories are selected.
        :return: 0, 0.5, or 1.
        """
        if self._has_return_trajectory:
            # Two-way s/c.
            A = (self._trajectory1 is None) and (self._trajectory2 is None)
            B = (self._trajectory1 is None) or (self._trajectory2 is None)
            C = isinstance(self._trajectory1, pd.Series) and isinstance(self._trajectory2, pd.Series)
            if A:
                return 0
            elif C:
                return 1
            elif B:
                return 0.5
            else:
                sonet_log(SonetLogType.ERROR,
                          'SonetSpacecraft.get_trajectory_selection_status."Wrong trajectory type"')
                return

        else:
            # One-way s/c.
            if self._trajectory is None:
                return 0
            elif isinstance(self._trajectory, pd.Series):
                return 1
            else:
                sonet_log(SonetLogType.ERROR,
                          'SonetSpacecraft.get_trajectory_selection_status."Wrong trajectory type"')
                return

    def get_trajectory_selected(self):
        """
        Returns a list with the current selected trajectories.

        @return: ['Earth - Mars'] or ['Earth - Mars', 'Mars - Earth']
        :rtype: list
        """
        sonet_log(SonetLogType.INFO, 'SonetSpacecraft.get_trajectory_selected')

        the_selected_trajectories = []

        if self._has_return_trajectory:
            # Two-way s/c.
            if self._trajectory1 is not None:
                the_selected_trajectories.append('Earth - Mars')
            if self._trajectory2 is not None:
                the_selected_trajectories.append('Mars - Earth')
        else:
            # One-way s/c.
            if self._trajectory is not None:
                the_selected_trajectories.append('Earth - Mars')

        return the_selected_trajectories

    def get_departure_arrival_date(self, p_trip='', p_trip_event='') -> int:
        """
        Getter method.
        Returns the s/c's departure or arrival date, for the selected p_trip,
        and for the passed p_trip_event.
        Example:
         - p_trip = 'Earth - Mars'
        - p_trip_event = 'Launching'

        @param p_trip: 'Earth - Mars' or 'Mars - Earth'
        @param p_trip_event: 'Launching' or 'Landing'
        @return: the date
        """
        # Are there selected trajectories for this s/c? There should be.
        if self.get_trajectory_selection_status() != 0:
            # Get the trajectory/ies.
            the_trajectory = []
            if self.get_has_return_trajectory():
                if p_trip == 'Earth - Mars':
                    the_trajectory = list(self._trajectory1)
                elif p_trip == 'Mars - Earth':
                    the_trajectory = list(self._trajectory2)
            else:
                if p_trip == 'Earth - Mars':
                    the_trajectory = list(self._trajectory)

            # Get the departure/arrival date.
            the_date = 0
            if p_trip_event == 'Launching':
                the_date = QDate.toJulianDay(the_trajectory[0])
            elif p_trip_event == 'Landing':
                the_date = QDate.toJulianDay(the_trajectory[1])

            return the_date

    def get_trajectory_selected_row(self) -> (QModelIndex, QModelIndex):
        if self._has_return_trajectory:
            return self._trajectory1_index, self._trajectory2_index
        else:
            return self._trajectory_index

    def reset_trajectory(self):
        """
        Resets the current selected trajectories. Used when a s/c filter changes and the already selected trajectories
        are no longer valid.
        """
        if self._has_return_trajectory:
            self._trajectory1 = None
            self._trajectory2 = None
            self._trajectory1_index = QModelIndex()
            self._trajectory2_index = QModelIndex()
        else:
            self._trajectory = None
            self._trajectory_index = QModelIndex()

    def set_filter(self, a_the_filter: SonetTrajectoryFilter, p_dataframe=False):
        """
        Setter method.
        Sets the argument a_the_filter as current SonetSpacecraft's filter. If the passed a_the_filter is
        a list of filters, then the spacecraft has outgoing and return trajectories and has two filters,
        otherwise it only has outgoing trajectory and thus only one filter.

        :param a_the_filter: the pcp filter
        :param p_dataframe: flag indicating if the argument a_the_filter is a dataframe or a SonetTrajectoryFilter
        """
        sonet_log(SonetLogType.INFO, 'SonetSpacecraft.set_filter')

        if p_dataframe is True:
            if isinstance(a_the_filter, list):
                self._pcp_filter1.set_data(a_the_filter[0].copy())
                self._pcp_filter2.set_data(a_the_filter[1].copy())
            elif isinstance(a_the_filter, pd.DataFrame):
                self._pcp_filter.set_data(a_the_filter.copy())
        else:
            if isinstance(a_the_filter, list):
                self._pcp_filter1.set_data(a_the_filter[0].get_data().copy())
                self._pcp_filter2.set_data(a_the_filter[1].get_data().copy())
            elif isinstance(a_the_filter, SonetTrajectoryFilter):
                self._pcp_filter.set_data(a_the_filter.get_data().copy())

    def set_filters(self):
        """
        Method for constructing a SonetSpacecraft object. The spacecraft has one filter per trajectory.
        TODO: Bad practice - defining instance attributes outside the class constructor.
        :return: True if everything was ok, false otherwise.
        """
        sonet_log(SonetLogType.INFO, 'SonetSpacecraft.set_filters')

        has_return_trajectory = self._has_return_trajectory

        # Type check.
        if not isinstance(has_return_trajectory, bool):
            return False

        if has_return_trajectory:
            # Two way trip.
            self._pcp_filter1 = SonetTrajectoryFilter(self, TripType.OUTGOING)
            self._pcp_filter2 = SonetTrajectoryFilter(self, TripType.INCOMING)

            self._trajectory1 = None
            self._trajectory2 = None

            self._trajectory1_index = QModelIndex()
            self._trajectory2_index = QModelIndex()

        else:
            # One way trip.
            self._pcp_filter = SonetTrajectoryFilter(self, TripType.OUTGOING)

            self._trajectory = None
            self._trajectory_index = QModelIndex()

        return True

    def set_has_return_trajectory(self, a_has_return_trajectory=None):
        """
        Method for constructing a SonetSpacecraft object.
        :param a_has_return_trajectory: bool
        :return: True if everything was ok, false otherwise.

        """
        # Convert string input to bool.
        if isinstance(a_has_return_trajectory, str):
            if a_has_return_trajectory == 'One way':
                a_has_return_trajectory = False
            elif a_has_return_trajectory == 'Two way':
                a_has_return_trajectory = True

        # Type check.
        if not isinstance(a_has_return_trajectory, bool):
            return False

        self._has_return_trajectory = a_has_return_trajectory
        return True

    def set_spacecraft_name(self, a_spacecraft_name=None):
        """
        Method for constructing a SonetSpacecraft object.
        :param a_spacecraft_name: a string.
        :return: True if everything was ok, false otherwise.
        """
        self._spacecraft_name = a_spacecraft_name

    def set_spacecraft_type(self, a_spacecraft_type=None):
        """
        Method for constructing a SonetSpacecraft object.
        :param a_spacecraft_type: Enum (SpacecraftType)
        :return: True if everything was ok, false otherwise.
        """
        # Convert string input to SpacecraftType enum.
        if isinstance(a_spacecraft_type, str):
            if a_spacecraft_type == 'Crewed':
                a_spacecraft_type = SpacecraftType.CREWED
            elif a_spacecraft_type == 'Cargo':
                a_spacecraft_type = SpacecraftType.CARGO

        # Check.
        if not SpacecraftType.is_valid(a_spacecraft_type):
            return False

        self._spacecraft_type = a_spacecraft_type
        return True

    def set_trajectory(self, a_trajectory=None, a_index=False, a_is_incoming_trajectory=False):
        """
        Setter method.
        Sets the trajectories fields for a given s/c, the a_is_incoming_trajectory paramenter controls whether
        we are setting the outgoing or incoming trajectory, in case the s/c has both. It's a bit weird but...

        @param a_is_incoming_trajectory: flag to control which trajectory are we setting.
        @param a_trajectory: Pandas Series representing a pcp row.
        @param a_index: the position of the pcp row.
        """
        # Check.
        if not (isinstance(a_trajectory, pd.Series) or isinstance(a_trajectory, list) or (a_index != None)):
            if a_trajectory is None:
                sonet_log(SonetLogType.INFO, 'SonetSpacecraft.set_trajectory."No trajectory selected"')
                self._p_main_window.statusbar.showMessage('No trajectory selected.', SONET_MSG_TIMEOUT)
                return
            else:
                sonet_log(SonetLogType.ERROR, 'SonetSpacecraft.set_trajectory."Wrong trajectory type"')
                self._p_main_window.statusbar.showMessage('UUups. Internal error, check debug log.')
                return False

        if self._has_return_trajectory:
            # Two-way s/c.
            if a_is_incoming_trajectory:
                self._trajectory2 = a_trajectory
                self._trajectory2_index = a_index
            else:
                self._trajectory1 = a_trajectory
                self._trajectory1_index = a_index
        else:
            # One-way s/c.
            self._trajectory = a_trajectory
            self._trajectory_index = a_index

        return True

    # Private methods
