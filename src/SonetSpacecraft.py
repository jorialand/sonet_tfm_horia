import pandas as pd
# from overloading import overload

from src.SonetTrajectoryFilter import SonetTrajectoryFilter
from src.SonetUtils import SpacecraftType, TripType, sonet_log, SonetLogType


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
    def __init__(self, a_spacecraft_name=None, a_spacecraft_type_crew=None, a_spacecraft_type_return=None):
        sonet_log(SonetLogType.INFO, 'SonetSpacecraft.__init__')

        # Instance members
        self._spacecraft_type = None
        self._has_return_trajectory = None

        self.set_spacecraft_name(a_spacecraft_name)
        self.set_spacecraft_type(a_spacecraft_type_crew)
        self.set_has_return_trajectory(a_spacecraft_type_return)
        self.set_filters()

    # Public methods
    def get_filter(self, a_trip_type=None):
        """
        Getter method, overload with a more specific functionality. It returns a concrete SonetTrajectoryFilter, based
        on the input a_trip_type.
        :param a_trip_type: TripType enum.
        :return: SonetTrajectoryFilter.
        """
        # If no trip type specified, return all the filters.
        if a_trip_type is None:
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

        if not isinstance(a_trip_type, TripType):
            sonet_log(SonetLogType.ERROR, 'SonetSpacecraft.get_filter."Wrong TripType"')
            return False

        if self._has_return_trajectory:
            if a_trip_type is TripType.OUTGOING:
                return self._pcp_filter1
            elif a_trip_type is TripType.INCOMING:
                return self._pcp_filter2
        else:
            if a_trip_type is TripType.OUTGOING:
                return self._pcp_filter
            elif a_trip_type is TripType.INCOMING:
                sonet_log(SonetLogType.ERROR, 'SonetSpacecraft.get_filter."Asked for incoming filter to an one-way S/C"')
                return False

    def get_filter_data(self, get_dataframe_copy=False):
        """
        Getter method.
        It's not the same to return a dataframe and a dataframe.copy(). get_dataframe_copy controls if we are getting
        the pointers to the original dataframes or copies of them.
         - If I return a dataframe, I am returning a pointer to the original dataframe, so all modifications are going
         to affect to the original dataframe.
         - If I return a dataframe copy, I am returning a new dataframe, so all modifications are not going to affect to
         the original dataframe.
         :param get_dataframe_copy: bool representing if we want original dataframes or copies.
        :return: a pandas dataframe or a list of them.
        """
        # Type check.
        if not isinstance(self._has_return_trajectory, bool):
            sonet_log(SonetLogType.ERROR, 'SonetSpacecraft.get_filter_data."Bad constructed S/C"')
            return False  # _has_return_trajectory should be bool, if not, there's some error.

        if self._has_return_trajectory:
            # If there are both outgoing and incoming trajectories, we return a list with both filter's dataframes.
            if get_dataframe_copy:
                return [self._pcp_filter1.get_data().copy(), self._pcp_filter2.get_data().copy()]
            else:
                return [self._pcp_filter1.get_data(), self._pcp_filter2.get_data()]
        else:
            # In case the spacecraft has no return trajectory, we just get the filter dataframe of the outgoing one.
            if get_dataframe_copy:
                return self._pcp_filter.get_data().copy()
            else:
                return self._pcp_filter.get_data()

    def get_has_return_trajectory(self):
        """
        Getter method.
        :return: bool. If the variable hasn't been setted, then it will return the default value,
        None, which is considered a boolean False.
        """
        return self._has_return_trajectory

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
        0.5 if 1 out of 2 trajectories are selected.
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

        else:
            # One-way s/c.
            if self._trajectory is None:
                return 0
            elif isinstance(self._trajectory, pd.Series):
                return 1
            else:
                sonet_log(SonetLogType.ERROR,
                          'SonetSpacecraft.get_trajectory_selection_status."Wrong trajectory type"')

    def set_filter(self, a_the_filter, dataframe=False):
        """
        Setter method.
        Sets the argument filter as current SonetSpacecraft's filter. If the input is a list of filters, then the
        spacecraft has outgoing and return trajectories and has two filters, otherwise only has outgoing trajectory and
        has only one filter.
        :return: bool true if everything was ok, false otherwise.
        """
        if dataframe is True:
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
        has_return_trajectory = self._has_return_trajectory

        # Type check.
        if not isinstance(has_return_trajectory, bool):
            return False

        if has_return_trajectory:
            # Two way trip.
            self._pcp_filter1 = SonetTrajectoryFilter(TripType.OUTGOING)
            self._pcp_filter2 = SonetTrajectoryFilter(TripType.INCOMING)

            self._trajectory1 = None
            self._trajectory2 = None
        else:
            # One way trip.
            self._pcp_filter = SonetTrajectoryFilter(TripType.OUTGOING)

            self._trajectory = None

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
        pass

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

    def set_trajectory(self, a_trajectory=None, a_is_incoming_trajectory=False):
        """
        Setter method.
        Sets the trajectories fields for a given s/c, the a_outgoing_trajectory paramenter controls whether
        we are setting the outgoing or incoming trajectory, in case the s/c has both. It's a bit weird but...
        :param a_trajectory: Pandas Series representing a dataframe row
        """
        # Check.
        if not (isinstance(a_trajectory, pd.Series) or isinstance(a_trajectory, list)):
            if a_trajectory is None:
                sonet_log(SonetLogType.INFO, 'SonetSpacecraft.set_trajectory."None trajectory"')
                return
            else:
                sonet_log(SonetLogType.ERROR, 'SonetSpacecraft.set_trajectory."Wrong trajectory type"')
                return False

        if self._has_return_trajectory:
            # Two-way s/c.
            if a_is_incoming_trajectory:
                self._trajectory2 = a_trajectory
            else:
                self._trajectory1 = a_trajectory
        else:
            # One-way s/c.
            self._trajectory = a_trajectory

        return True

    # Private methods
