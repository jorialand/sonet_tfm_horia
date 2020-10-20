"""
Database.
Here are going to be stored all spacecrafts, created during runtime
execution. No persistence at this moment (i.e. the database dies
when closing the program)-
"""
import pandas as pd

from src.SonetUtils import TripType

db = {}

dir_path = '/Users/Jorialand/code/tfm/sonet/sonet_tfm_horia/src/'
pcp_outgoing = pd.read_csv(dir_path + '10kPCP_Earth2Mars.txt')
pcp_incoming = pd.read_csv(dir_path + '10kPCP_Mars2Earth.txt')


# @staticmethod
def get_pcp_table(a_trip_type):
    if not TripType.is_valid(a_trip_type):
        return False

    if a_trip_type == TripType.OUTGOING:
        return pcp_outgoing
    elif a_trip_type == TripType.INCOMING:
        return pcp_incoming
    else:
        return False