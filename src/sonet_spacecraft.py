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
        #self._df_outgoing = build_mock_DataFrame()
        #self._df_incoming = build_mock_DataFrame()

        # print(df_outgoing.head())
        # print(df_incoming.head( ))

# TODO: Convert DepDates column to readable date (e.g. YYYY-MM-DD)
# TODO: Convert theta column to readable angle (e.g. degrees)
