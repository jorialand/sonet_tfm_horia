"""
Database.
Here are going to be stored all spacecrafts, created during runtime
execution. No persistence at this moment (i.e. the database dies
when closing the program)-
"""
import pandas as pd
db = {}

dir_path = '/Users/Jorialand/code/tfm/sonet/sonet_tfm_horia/src/'
pcp_outgoing = pd.read_csv(dir_path + '10kPCP_Earth2Mars.txt')
pcp_incoming = pd.read_csv(dir_path + '10kPCP_Mars2Earth.txt')