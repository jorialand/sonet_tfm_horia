"""
    This class purpose is to host the set of conditions (aka filter) to be applied to spacecraft's trajectories.
    Each spacecraft will have at least one SonetTrajectoryFilter object, which will implement the filtering
    functionality.

    The filter is a Pandas dataframe with the following structure:
    |Status  | Type    | Filter                |
    |  1     |  Energy | filter1 activated...  |
    |  0     |  Dates  | filter2 deactivated...|
    |  0     |  Tof    | filter3 deactivated...|
"""
import pandas as pd


class SonetTrajectoryFilter:
    def __init__(self):
        self._filter = pd.DataFrame(columns=['Status', 'Type', 'Filter'])

       # Debug
       #  new_row = {'Status': 1, 'Type': FilterType.ENERGY, 'Filter': 'filter1'}
       #  self._filter = self._filter.append(new_row, ignore_index=True)
       #  self._filter = self._filter.append(new_row, ignore_index=True)

    # Public methods
    def get_filter(self):
        return self._filter

    def set_filter(self, a_filter):
        self._filter = a_filter
