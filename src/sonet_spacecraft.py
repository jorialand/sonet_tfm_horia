import random

import pandas as pd

from src.sonet_Utils import ObjectType, SpacecraftType


class SonetSpacecraft:
    def __init__(self, a_spacecraft_type=None):
        # Private members
        self._obj_type = ObjectType.SPACECRAFT
        self._spacecraft_type = a_spacecraft_type

        # Public members
        # ...

        dir_path = '/Users/Jorialand/code/tfm/sonet/sonet_tfm_horia/src/'
        _ = self.getSpacecraftType()
        if _ is SpacecraftType.CREWED:
            self._df_outgoing = pd.read_csv(dir_path + '10kPCP_Earth2Mars.txt')
            self._df_incoming = pd.read_csv(dir_path + '10kPCP_Mars2Earth.txt')

            # Debug
            ini = random.randint(0, 10)
            fin = random.randint(11, 22)
            self._df_outgoing = self._df_outgoing.iloc[ini:fin]

            ini = random.randint(0, 10)
            fin = random.randint(11, 22)
            self._df_incoming = self._df_incoming.iloc[ini:fin]


        elif _ is SpacecraftType.CARGO:
            self._df_outgoing = pd.read_csv(dir_path + '10kPCP_Earth2Mars.txt')

            # Debug
            ini = random.randint(0, 10)
            fin = random.randint(11, 22)
            self._df_outgoing = self._df_outgoing.iloc[ini:fin]

    # Public methods
    def getSpacecraftType(self):
        return self._spacecraft_type

    def getObjectType(self):
        return self._obj_type

    def getPCPTable(self, a_table=None):
        """
        Returns the Pandas dataframe representing the porkchop table of the outgoing (e.g. Earth-Mars) or
        incoming trip.
        Note: For CARGO spacecrafts, no incoming trip is available, so it is returned an empty dataframe.

        :param a_table: str representing if is asked for ['outgoing'|'incoming']  porkchop table.
        :return: a Pandas dataframe.
        """
        if a_table is None:
            print('Specify "outgoing" or "incoming" porkchop plot table.')
            return 0

        try:
            if a_table == 'outgoing':
                return self._df_outgoing
            elif a_table == 'incoming':
                return self._df_incoming
            else:
                print('No table found with the requested argument')
                return None
        except AttributeError:
            return pd.DataFrame()


    # Private methods
# TODO: Convert DepDates column to readable date (e.g. YYYY-MM-DD)
# TODO: Convert theta column to readable angle (e.g. degrees)
