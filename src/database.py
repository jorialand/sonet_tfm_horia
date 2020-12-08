"""
Database.
Here are going to be stored all spacecrafts, created during runtime
execution. No persistence at this moment (i.e. the database dies
when closing the program)-
"""
import pandas as pd
from numpy import pi
from PySide2.QtCore import QDate
from src.SonetUtils import SONET_DEBUG, TripType

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
        return pcp_outgoing
    elif a_trip_type == TripType.INCOMING:
        return pcp_incoming
    else:
        return False

def get_spacecraft(a_spacecraft):
    """
    Getter function.

    :param a_spacecraft: string
    :return: SonetSpacecraft.
    """
    return db[a_spacecraft]

def get_spacecrafts_list():
    """
    Getter function.
    - Returns the list of spacecrafts within the database.

    :return: list of spacecrafts.
    """
    return list(db.keys())

def import_pcp_from_matlab():
    """
    This method reads the incoming Matlab AstroLib's porkchop trajectories.

    For convenience, it adds a new row 'ArrivDates', which is a combination
    of 'DepDates'+'tof' columns.
    """
    if SONET_DEBUG:
        print('database.import_pcp_from_matlab')

    # Read data
    pcp_out = pd.read_csv(dir_path + '10kPCP_Earth2Mars.txt')
    pcp_inc = pd.read_csv(dir_path + '10kPCP_Mars2Earth.txt')

    # New column 'ArrivDates'
    pcp_out['ArrivDates'] = pcp_out.DepDates + pcp_out.tof
    pcp_inc['ArrivDates'] = pcp_inc.DepDates + pcp_inc.tof
    
    # Convert DepDates from JD2000 to Gregorian calendar.
    JD2000 = 2451545.0  # Julian Day 2000, extracted from AstroLib matlab codebase
    # David de la Torre).
    pcp_out['DepDates'] = (pcp_out.DepDates + JD2000).apply(QDate.fromJulianDay)
    pcp_inc['DepDates'] = (pcp_inc.DepDates + JD2000).apply(QDate.fromJulianDay)

    # Also convert ArrivDates.
    pcp_out['ArrivDates'] = (pcp_out.ArrivDates + JD2000).apply(QDate.fromJulianDay)
    pcp_inc['ArrivDates'] = (pcp_inc.ArrivDates + JD2000).apply(QDate.fromJulianDay)

    # Convert theta from radians to sexagesimal degrees.
    pcp_out.theta = pcp_out.theta * 180 / pi
    pcp_inc.theta = pcp_inc.theta * 180 / pi

    reordered_cols = ['DepDates', 'ArrivDates', 'tof', 'theta', 'dvt', 'dvd', 'dva', 'c3d', 'c3a']
    pcp_out = pcp_out.reindex(columns=reordered_cols)
    pcp_inc = pcp_inc.reindex(columns=reordered_cols)

    return pcp_out, pcp_inc

# The spacecrafts database in runtime.
db = {}

# dir_path = '/Users/Jorialand/code/tfm/sonet/sonet_tfm_horia/src/'
dir_path = 'C:/workcopy/data/'

# pcp_outgoing = pd.read_csv(dir_path + '10kPCP_Earth2Mars.txt')
# pcp_incoming = pd.read_csv(dir_path + '10kPCP_Mars2Earth.txt')

pcp_outgoing, pcp_incoming = import_pcp_from_matlab()
