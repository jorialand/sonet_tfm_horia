import random

import pandas as pd

from src.Utils import ObjectType


class SonetSpacecraft:
    def __init__(self):
        # Attributes
        self._type = ObjectType.SPACECRAFT

        # Pandas model
        dir_path = '/Users/Jorialand/code/tfm/sonet/sonet_tfm_horia/src/'
        self._df_outgoing = pd.read_csv(dir_path + '10kPCP_Earth2Mars.txt')
        self._df_incoming = pd.read_csv(dir_path + '10kPCP_Mars2Earth.txt')
        # Debug
        ini = random.randint(0,10)
        fin = random.randint(11,22)
        self._df_outgoing = self._df_outgoing.iloc[ini:fin]
        self._df_incoming = self._df_incoming.iloc[ini:fin]

    def getPCPTable(self, table):
        switcher = {
            'outgoing': self._df_outgoing,
            'incoming': self._df_incoming
        }
        return switcher.get(table, 'No table found with the requested argument')

# TODO: Convert DepDates column to readable date (e.g. YYYY-MM-DD)
# TODO: Convert theta column to readable angle (e.g. degrees)
