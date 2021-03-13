# ==============================================================================================
# ==============================================================================================
#
#
#                                    FILE database
#
#
# ==============================================================================================
# ==============================================================================================

"""
Database.
Here are going to be stored all spacecrafts, created during runtime
execution. No persistence at this moment (i.e. the database dies
when closing the program)-
"""
import pandas as pd

# from PySide2.QtCore import QDate
from src.SonetSpacecraft import SonetSpacecraft
from src.SonetUtils import TripType


def get_pcp_table(a_trip_type):
    """
    Getter function.
    - Returns the whole pcp table stored.
    :param a_trip_type: the type of trip asked for [OUTGOING|INCOMING]
    :return: Pandas DataFrame
    """
    if not TripType.is_valid(a_trip_type):
        return False

    if a_trip_type == TripType.OUTGOING:
        if df_pcp_outgoing is None:
            return pd.DataFrame()
        else:
            return df_pcp_outgoing
    elif a_trip_type == TripType.INCOMING:
        if df_pcp_incoming is None:
            return pd.DataFrame()
        else:
            return df_pcp_incoming
    else:
        return False

def get_spacecraft(a_spacecraft: str):
    """
    Getter function.

    :param a_spacecraft: string
    :rtype: SonetSpacecraft
    """
    return db[a_spacecraft]

def get_spacecrafts_list(p_return_objects=False):
    """
    Getter function.
    Returns the list of spacecrafts within the database.

    :return: list of spacecrafts.
    :rtype: list
    """
    if p_return_objects:
        return list(db.values())
    else:
        return list(db.keys())

def get_working_pcp_paths():
    return [df_pcp_outgoing_path, df_pcp_incoming_path]

def set_working_pcp(a_trip: TripType, a_pkl_file_path: str):
    """
    Sets the working PCPs, if the passed path is empty, then the PCP is set to None.
    :param a_trip: Outgoing/Incoming trip
    :param a_pkl_file_path: the pkl file path
    :returns bool indicating if the working pcp has changed or is the same as before.
    """
    global df_pcp_outgoing, df_pcp_outgoing_path
    global df_pcp_incoming, df_pcp_incoming_path
    has_changed = False

    if a_trip == TripType.OUTGOING:
        if a_pkl_file_path != df_pcp_outgoing_path:
            has_changed = True

        if a_pkl_file_path:
            df_pcp_outgoing = pd.read_pickle(a_pkl_file_path)
            df_pcp_outgoing_path = a_pkl_file_path
        else:
            df_pcp_outgoing = None
            df_pcp_outgoing_path = ''
    elif a_trip == TripType.INCOMING:
        if a_pkl_file_path != df_pcp_incoming_path:
            has_changed = True

        if a_pkl_file_path:
            df_pcp_incoming = pd.read_pickle(a_pkl_file_path)
            df_pcp_incoming_path = a_pkl_file_path
        else:
            df_pcp_incoming = None
            df_pcp_incoming_path = ''

    return has_changed


# The spacecrafts database.
db = {}

# The pcp trajectories database.
df_pcp_outgoing_path = ''
df_pcp_outgoing = None

df_pcp_incoming_path = ''
df_pcp_incoming = None