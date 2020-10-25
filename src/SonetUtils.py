import random
from enum import Enum, unique

import pandas as pd

# Flag controlling if the debug messages are going to be printed in the Python console. Useful for debugging.
SONET_DEBUG = True

def PrintDict(ar_dict):
    """
    Convenience function for printing a dictionary to console.
    Useful for debugging.
    :param ar_dict:
    """
    print("Keys> ", [x for x in ar_dict.keys()])
    print("Values> ", [x for x in ar_dict.values()])


@unique
class SpacecraftType(Enum):
    """
    Enum representing the kind of spacecrafts.
    """
    NA = 0  # NA stands for Not Assigned
    CREWED = 1
    CARGO = 2

    @staticmethod
    def get_the_list():
        """
        Returns this class enum as Python list, useful to verify if a input object is of valid enum type.
        :return: Python list.
        """
        return [SpacecraftType.CREWED, SpacecraftType.CARGO]

    @staticmethod
    def is_valid(a_spacecraft_type):
        """
        Checks if a input variable is of a valid spacecraft type, e.g. if it is found in the SpacecraftType enum.
        :param a_spacecraft_type: a variable to check.
        :return: True if the argument is a valid spacecraft type, false otherwise.
        """
        list_valid_types = SpacecraftType.get_the_list()
        if a_spacecraft_type in list_valid_types:
            return True
        return False

@unique
class FilterType(Enum):
    """
    Enum representing the type of filter applied to the spacecrafts trajectories.
    """
    NA = 0
    ENERGY = 1  # ['dvt', '<', '4', 'km/s']
    TOF = 2  # ['Time of flight', '<', '200', 'days']
    DATES = 3  # ['Departs', 'Earth', 'Before', '20/07/2021']
    DATES_2 = 4  # ['Departs', 'Mars', 'At the same time', 'Spacecraft 1', 'Leaves Earth']

@unique
class TripType(Enum):
    """
    Enum representing the trip type, outgoing, and incoming.
    """
    NA = 0
    OUTGOING = 1
    INCOMING = 2

    @staticmethod
    def get_the_list():
        """
        Returns this class enum as Python list, useful to verify if a input object is of valid enum type.
        :return: Python list.
        """
        return [TripType.OUTGOING, TripType.INCOMING]

    @staticmethod
    def is_valid(a_trip_type):
        """
        Checks if the input variable is of a valid enum type, e.g. if it is found in the TripType enum.
        :param a_trip_type: a variable to check.
        :return: True if the argument is a valid TripType, false otherwise.
        """
        list_valid_types = TripType.get_the_list()
        if a_trip_type in list_valid_types:
            return True
        return False

    @staticmethod
    def convert_to_enum(a_trip_type):
        if a_trip_type == 'Earth - Mars':
            return TripType.OUTGOING
        elif a_trip_type == 'Mars - Earth':
            return TripType.INCOMING

def build_mock_DataFrame(num_rows=5, num_columns=8, min=0, max=10):
    """

    :param num_rows:
    :param num_columns:
    :param min:
    :param max:
    :return:
    """
    # Build columns
    num_rows = random.randint(1,1e2)
    _ = ['col'+str(i) for i in range(num_columns)]
    result = pd.DataFrame(columns=_)
    build_row = lambda: [random.randint(min,max) for _ in range(num_columns)]
    for i in range(num_rows):
        result.loc[len(result)] = build_row()
    return result


def build_mock_filter():
    """

    :return:
    """
    _data = pd.DataFrame(columns=['Status', 'Type', 'Filter'])
    new_row = {'Status': 0, 'Type': FilterType.ENERGY, 'Filter': ['dvt', '<=', 100, 'km/s']}
    _data = _data.append(new_row, ignore_index=True)

    new_row = {'Status': 0, 'Type': FilterType.ENERGY, 'Filter': ['c3d', '<=', 64, 'km/s']}
    _data = _data.append(new_row, ignore_index=True)

    new_row = {'Status': 0, 'Type': FilterType.ENERGY, 'Filter': ['dva', '<=', 5, 'km/s']}
    _data = _data.append(new_row, ignore_index=True)

    new_row = {'Status': 0, 'Type': FilterType.ENERGY, 'Filter': ['theta', '<=', 3.1416, 'deg']}
    _data = _data.append(new_row, ignore_index=True)

    new_row = {'Status': 0, 'Type': FilterType.TOF, 'Filter': ['tof', '<=', 250, 'Days']}
    _data = _data.append(new_row, ignore_index=True)

    new_row = {'Status': 0, 'Type': FilterType.TOF, 'Filter': ['tof', '>=', 100, 'Days']}
    _data = _data.append(new_row, ignore_index=True)

    return _data

if __name__ == "__main__":
    d = {'key1': 'value1', 'key2': 'value1'}
    PrintDict(d)
