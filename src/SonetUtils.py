from enum import Enum, unique

from PySide2.QtWidgets import QMessageBox

import src.database as db


# from src.SonetSpacecraft import SonetSpacecraft # Error if importing! :S
# from src.SonetMainWindowQt import get_main_window
# ==============================================================================================
# ==============================================================================================
#
#
#                                    File SonetUtils
#
#
# ==============================================================================================
# ==============================================================================================

# Enums.
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
    def convert_to_enum(a_trip_type):
        if a_trip_type == 'Earth - Mars':
            return TripType.OUTGOING
        elif a_trip_type == 'Mars - Earth':
            return TripType.INCOMING

    @staticmethod
    def convert_to_str(a_trip_type):
        if a_trip_type == TripType.OUTGOING:
            return 'Earth - Mars'
        elif a_trip_type == TripType.INCOMING:
            return 'Mars - Earth'

    @staticmethod
    def get_index(a_trip_type):
        if a_trip_type == 'Earth - Mars':
            return 0
        elif a_trip_type == 'Mars - Earth':
            return 1

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

@unique
class SonetDebugLevel(Enum):
    """
    Flag controlling if the debug messages are going to be printed in the Python console.
    Useful for debugging.
    """
    NO_DEBUG = 0
    ONLY_ERRORS = 1
    FULL_VERBOSE = 2

@unique
class SonetLogType(Enum):
    """
    Type of message to be logged.
    """
    INFO = 0
    WARNING = 1
    ERROR = 2

# Utility methods.
def popup_msg(text='text', icon=QMessageBox.Information, info_text='info_text', window_title='window_title'):
    msg = QMessageBox()
    msg.setIcon(icon)
    msg.setText(text)
    msg.setInformativeText(info_text)
    # msg.setDetailedText("The details are as follows:")
    msg.setWindowTitle(window_title)
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec_()

def sonet_log(a_log_type, a_log_msg):
    """
    Log to console the status of the sonet application.
    Currently, there are three states logging modes: NO_DEBUG, ONLY_ERRORS, and FULL_VERBOSE.
    If the global variable SONET_DEBUG_LEVEL is set to:
     - NO_DEBUG, then no debug messages should be logged.
     - ONLY_ERRORS, only errors or warnings should be logged.
     - FULL_VERBOSE, any other message is logged. It also includes the ONLY_ERRORS level messages.

     Example: sonet_log(SonetLogType.INFO, 'ClassName.method_name."the_msg"')

    """

    if SONET_DEBUG_LEVEL is SonetDebugLevel.NO_DEBUG:
        # If debug logging is deactivated, then do nothing.
        pass
    else:
        # Warnings/Errors should be logged whether the application log level is ONLY_ERRORS or FULL_VERBOSE.
        if a_log_type is SonetLogType.WARNING:
            print('Warning: ' + a_log_msg)
        elif a_log_type is SonetLogType.ERROR:
            print('Error: ' + a_log_msg)
        elif a_log_type is SonetLogType.INFO:
            # Info logs, are only printed in FULL_VERBOSE mode.
            if SONET_DEBUG_LEVEL is SonetDebugLevel.FULL_VERBOSE:
                print('Info: ' + a_log_msg)

def reset_sc_filters_and_trajectories(p_filters_and_trajectories='Both', p_trips='Both'):
    """
    Traverse all the s/c in the database and reset their filters and trajectories,
    inform to the user throught the main window status bar.
    """
    # For each s/c.
    for sc in db.get_spacecrafts_list(p_return_objects=True):
        if p_filters_and_trajectories == 'Both':
        # Reset filters and trajectories.
            if p_trips == 'Both':
                sc.reset_filter_and_trajectory(p_all_trips=True)
            if p_trips == 'Earth-Mars':
                sc.reset_filter_and_trajectory(TripType.OUTGOING)
            if p_trips == 'Mars-Earth':
                sc.reset_filter_and_trajectory(TripType.INCOMING)
        elif p_filters_and_trajectories == 'Trajectories':
        # Reset trajectories.
            if p_trips == 'Both':
                sc.reset_trajectory()
            if p_trips == 'Earth-Mars':
                sc.reset_trajectory('Earth-Mars')
            if p_trips == 'Mars-Earth':
                sc.reset_trajectory('Mars-Earth')
        elif p_filters_and_trajectories == 'Filters':
        # Reset filters - NOT NEEDED YET.
            if p_trips == 'Both':
                pass
            if p_trips == 'Earth-Mars':
                pass
            if p_trips == 'Mars-Earth':
                pass

# Global debug verbose level for the application.
SONET_DEBUG_LEVEL = SonetDebugLevel.ONLY_ERRORS

# Global main window's status bar messages duration, in milliseconds.
SONET_MSG_TIMEOUT = 2500

# Global paths.
SONET_DIR = '/Users/jorialand/code/tfm/sonet/sonet_tfm_horia/'
SONET_DATA_DIR = SONET_DIR + 'data/'
SONET_PCP_DATA_DIR = SONET_DIR + 'data/PCP/'
DEFAULT_OUTGOING_PCP = SONET_PCP_DATA_DIR + 'PCP_Earth2Mars_2025__P5_Y1.500000e+00_mr0_lp0/PCP_Earth2Mars.pkl'
DEFAULT_INCOMING_PCP = SONET_PCP_DATA_DIR + 'PCP_Mars2Earth_2026__P5_Y1.500000e+00_mr0_lp0/PCP_Mars2Earth.pkl'
if __name__ == "__main__":
    pass
