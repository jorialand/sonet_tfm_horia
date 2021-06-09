from enum import Enum, unique

import pandas as pd
from PySide2.QtCore import QDate
from PySide2.QtWidgets import QMessageBox

import src.database as db


# from src.SonetMainWindowQt import get_main_window # If you want to import sth from main window, it crashes before starting the app :S.

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
    def get_str(a_type):
        if a_type == SpacecraftType.CREWED:
            return 'Human'
        elif a_type == SpacecraftType.CARGO:
            return 'Cargo'
        else:
            pass

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

def add_auto_trajectory_selection_filter(fw=None, a_operator='Min', a_param='dvt'):
    fw.auto_traj_sel_cb_enabled.setChecked(True)
    fw.auto_traj_sel_cmb_min_max.setCurrentText(a_operator)
    fw.auto_traj_sel_cmb_item.setCurrentText(a_param)
    fw.pb_add.clicked.emit()

def add_complex_date_filter(fw=None, a_event='Departs', a_value='At least', a_value2=90, a_value3='After',
                            a_sc='Another s/c name', a_sc_trip='Earth - Mars', a_sc_trip2='Landing'):
    """
    The combo widgets values, are (in general) the same as seen in the window combo.

    :param fw: pointer to the filters window.
    :param a_event: 'Departs'|'Arrives'.
    :param a_value: 'At least'|'At maximum'|'At the same time'.
    :param a_value2: The offset value: int.
    :param a_value3: 'After'|'Before'.
    :param a_sc: The s/c to which offset: str.
    :param a_sc_trip: 'Earth - Mars'|'Mars - Earth'.
    :param a_sc_trip2: 'Launching'|'Landing'.
    """
    fw.cb_dep_arriv_dates.setChecked(True)
    fw.combo_dept_arriv.setCurrentText(a_event)
    fw.cb_dates_1.setChecked(True)
    fw.combo_at_least.setCurrentText(a_value)
    fw.spin_number.setValue(a_value2)
    fw.combo_when.setCurrentText(a_value3)
    fw.radio_spacecraft.setChecked(True)
    fw.combo_select_spacecraft.setCurrentText(a_sc)
    fw.combo_select_trip.setCurrentText(a_sc_trip)
    fw.combo_event.setCurrentText(a_sc_trip2)
    fw.pb_add.clicked.emit()
def add_energy_filter(fw=None, a_param='dvt', a_operator='<=', a_value=10):
    """
    The combo widgets values, are (in general) the same as seen in the window combo.

    :param fw: pointer to the filters window.
    :param a_param: 'dvt'|'dvd'|'dva'|'c3d'|'c3a'|'theta'.
    :param a_operator: '<='|'>='.
    :param a_value: float.

    """
    fw.cb_energy.setChecked(True)
    fw.combo_energy_parameter.setCurrentText(a_param)
    fw.combo_energy_operator.setCurrentText(a_operator)
    fw.spin_energy_number.setValue(a_value)
    fw.pb_add.clicked.emit()

def add_sc_cargo_oneway(mw=None, a_sc_name=''):
    """
    Create a cargo (Earth - Mars) s/c.
    :param mw: pointer to the main window.
    :param a_sc_name: str.
    """

    mw.sonet_spacecraft_type_qcmb.setCurrentIndex(1)  # Cargo.
    mw.sonet_spacecraft_type_has_return_trajectory_qcmb.setCurrentIndex(0)  # One way.
    mw.sonet_sc_name_le.setText(a_sc_name)
    mw.sonet_add_spacecraft_qpb.clicked.emit()

def add_sc_crewed_twoway(mw=None, a_sc_name=''):
    """
    Create a crewed (Earth - Mars + Mars - Earth) s/c.
    :param mw: pointer to the main window.
    :param a_sc_name: str.
    """
    mw.sonet_spacecraft_type_qcmb.setCurrentIndex(0)  # Crewed.
    mw.sonet_spacecraft_type_has_return_trajectory_qcmb.setCurrentIndex(1)  # Two way.
    mw.sonet_sc_name_le.setText(a_sc_name)
    mw.sonet_add_spacecraft_qpb.clicked.emit()

# Note: fw stands for filters window :).
def add_simple_date_filter(fw=None, a_event='Arrives', a_when='Before', a_date=None):
    """
    The combo widgets values, are (in general) the same as seen in the window combo.

    :param fw: pointer to the filters window.
    :param a_event: 'Departs'|'Arrives'.
    :param a_when: 'On'|'After'|'Before'.
    :param a_date: the date: [day(int), month(int), year(int)].
    """
    fw.cb_dep_arriv_dates.setChecked(True)
    fw.combo_dept_arriv.setCurrentText(a_event)  # Departs|Arrives
    fw.cb_dates_2.setChecked(True)
    fw.combo_when_2.setCurrentText(a_when)  # On|Before|After
    fw.dateEdit.setDate(QDate(a_date[2], a_date[1], a_date[0]))
    fw.pb_add.clicked.emit()

def add_tof_filter(fw=None, a_operator='<=',  a_value=200):
    fw.cb_time_of_flight.setChecked(True)
    fw.combo_time_of_flight_operator.setCurrentText(a_operator)
    fw.spin_number_2.setValue(a_value)
    fw.pb_add.clicked.emit()

def build_example_mission(p_main_window=None, p_filters_window=None, a_mission_name='Demo 1'):
    """
    Build your missions here! Just follow the same structure as seen in 'Demo 1' case to automatically create a
    predefined mission when starting the app.

    This approach has some drawbacks! But it's the only one that has worked for me :).

    :param p_main_window:
    :param p_filters_window:
    :param a_mission_name:
    """

    if a_mission_name == 'Demo 1':

        # If called from __main__.
        if p_main_window:
            # Create the s/c.
            add_sc_cargo_oneway(mw=p_main_window, a_sc_name='SHAB')
            add_sc_cargo_oneway(mw=p_main_window, a_sc_name='DAV')
            add_sc_crewed_twoway(mw=p_main_window, a_sc_name='MTV')

            # Create the edit filters window.
            p_main_window.clicked_apply_filter(a_build_test_mission=a_mission_name)

        # If called from main_window, after just created the edit filters window.
        if p_filters_window:
            # Add filters.

            # SHAB > Earth-Mars
            select_sc_and_trip(fw=p_filters_window, a_sc='SHAB', a_trip='Earth - Mars')
            # First LOpp & Low-cost.
            add_simple_date_filter(fw=p_filters_window, a_event='Arrives', a_when='Before', a_date=[1,1,2028])
            add_auto_trajectory_selection_filter(fw=p_filters_window, a_operator='Min', a_param='dvt')

            # DAV > Earth-Mars
            select_sc_and_trip(fw=p_filters_window, a_sc='DAV', a_trip='Earth - Mars')
            # First LOpp & Low-cost.
            add_simple_date_filter(fw=p_filters_window, a_event='Arrives', a_when='Before', a_date=[1,1,2028])
            add_auto_trajectory_selection_filter(fw=p_filters_window, a_operator='Min', a_param='dvt')

            # MTV > Earth-Mars
            select_sc_and_trip(fw=p_filters_window, a_sc='MTV', a_trip='Earth - Mars')
            # Arrive Mars 2nd LOpp & After SHAB/DAV have landed in Mars.
            add_simple_date_filter(fw=p_filters_window, a_event='Arrives', a_when='Before', a_date=[1,1,2030])
            add_complex_date_filter(fw=p_filters_window, a_event='Departs', a_value='At least', a_value2=90,
                                    a_value3='After', a_sc='SHAB', a_sc_trip='Earth - Mars', a_sc_trip2='Landing')
            add_complex_date_filter(fw=p_filters_window, a_event='Departs', a_value='At least', a_value2=90,
                                    a_value3='After', a_sc='DAV', a_sc_trip='Earth - Mars', a_sc_trip2='Landing')
            # Fast-transit.
            # add_auto_trajectory_selection_filter(fw=p_filters_window, a_operator='Min', a_param='tof')
            add_tof_filter(fw=p_filters_window, a_operator='<=', a_value=250)

            # MTV < Mars-Earth
            select_sc_and_trip(fw=p_filters_window, a_sc='MTV', a_trip='Mars - Earth')
            # The mission lasts at least 90d & returns Earth before 2nd LOpp ends.
            add_complex_date_filter(fw=p_filters_window, a_event='Departs', a_value='At least', a_value2=90,
                                    a_value3='After', a_sc='MTV', a_sc_trip='Earth - Mars', a_sc_trip2='Landing')
            add_simple_date_filter(fw=p_filters_window, a_event='Departs', a_when='Before', a_date=[1,1,2032])
            # Fast-transit & low-cost.
            add_tof_filter(fw=p_filters_window, a_operator='<=', a_value=240)
            # add_energy_filter(fw=p_filters_window, a_param='dvt', a_operator='<=', a_value=17)
            # Select the first oportunity which matches above conditions.
            # add_auto_trajectory_selection_filter(fw=p_filters_window, a_operator='Min', a_param='Departure date')

            # Accept&Close the window does not work here :(.
            # p_filters_window.btn_accept.clicked.emit()

    if a_mission_name == 'NASA DRA5.0 Long-Stay - Pre-deployment':

        # If called from __main__.
        if p_main_window:
            # Create the s/c.
            add_sc_cargo_oneway(mw=p_main_window, a_sc_name='SHAB 1')
            add_sc_cargo_oneway(mw=p_main_window, a_sc_name='DAV 1')
            add_sc_crewed_twoway(mw=p_main_window, a_sc_name='MTV 1')
            add_sc_cargo_oneway(mw=p_main_window, a_sc_name='SHAB 2')
            add_sc_cargo_oneway(mw=p_main_window, a_sc_name='DAV 2')
            add_sc_crewed_twoway(mw=p_main_window, a_sc_name='MTV 2')
            # Create the edit filters window.
            p_main_window.clicked_apply_filter(a_build_test_mission=a_mission_name)

        # If called from main_window, after just created the edit filters window, add filters.
        if p_filters_window:
            # Launch opportunities.
            # E-M 2028, 2030, 2032, 2034, 2035.5?
            # M-E ...

            # SHAB 1 land on Mars in the 1st launch op.
            select_sc_and_trip(fw=p_filters_window, a_sc='SHAB 1', a_trip='Earth - Mars')
            add_simple_date_filter(fw=p_filters_window, a_event='Arrives', a_when='Before', a_date=[1, 1, 2028])
            add_auto_trajectory_selection_filter(fw=p_filters_window, a_operator='Min', a_param='dvt')

            # DAV 1 land on Mars in the 1st launch op.
            select_sc_and_trip(fw=p_filters_window, a_sc='DAV 1', a_trip='Earth - Mars')
            add_simple_date_filter(fw=p_filters_window, a_event='Arrives', a_when='Before', a_date=[1, 1, 2028])
            add_auto_trajectory_selection_filter(fw=p_filters_window, a_operator='Min', a_param='dvt')


            # MTV 1 lands on Mars in the 2nd launch op.
            select_sc_and_trip(fw=p_filters_window, a_sc='MTV 1', a_trip='Earth - Mars')
            add_simple_date_filter(fw=p_filters_window, a_event='Arrives', a_when='Before', a_date=[1, 1, 2030])
            add_simple_date_filter(fw=p_filters_window, a_event='Arrives', a_when='After', a_date=[1, 1, 2028])
            add_tof_filter(fw=p_filters_window, a_operator='<=', a_value=240)
            # MTV 1 departs Mars in the next launch op.
            select_sc_and_trip(fw=p_filters_window, a_sc='MTV 1', a_trip='Mars - Earth')
            add_simple_date_filter(fw=p_filters_window, a_event='Departs', a_when='Before', a_date=[1, 1, 2032])
            add_simple_date_filter(fw=p_filters_window, a_event='Departs', a_when='After', a_date=[1, 1, 2030])
            add_tof_filter(fw=p_filters_window, a_operator='<=', a_value=240)

            # SHAB 2 land on Mars in the 2nd launch op.
            select_sc_and_trip(fw=p_filters_window, a_sc='SHAB 2', a_trip='Earth - Mars')
            add_simple_date_filter(fw=p_filters_window, a_event='Arrives', a_when='Before', a_date=[1, 1, 2030])
            add_simple_date_filter(fw=p_filters_window, a_event='Arrives', a_when='After', a_date=[1, 1, 2028])
            add_auto_trajectory_selection_filter(fw=p_filters_window, a_operator='Min', a_param='dvt')

            # DAV 2 land on Mars in the 2nd launch op.
            select_sc_and_trip(fw=p_filters_window, a_sc='DAV 2', a_trip='Earth - Mars')
            add_simple_date_filter(fw=p_filters_window, a_event='Arrives', a_when='Before', a_date=[1, 1, 2030])
            add_simple_date_filter(fw=p_filters_window, a_event='Arrives', a_when='After', a_date=[1, 1, 2028])
            add_auto_trajectory_selection_filter(fw=p_filters_window, a_operator='Min', a_param='dvt')

            # MTV 2 land on Mars in the 3rd launch op.
            select_sc_and_trip(fw=p_filters_window, a_sc='MTV 2', a_trip='Earth - Mars')
            add_simple_date_filter(fw=p_filters_window, a_event='Arrives', a_when='Before', a_date=[1, 1, 2032])
            add_simple_date_filter(fw=p_filters_window, a_event='Arrives', a_when='After', a_date=[1, 1, 2030])
            add_tof_filter(fw=p_filters_window, a_operator='<=', a_value=240)
            # MTV 2 departs Mars in the next launch op.
            select_sc_and_trip(fw=p_filters_window, a_sc='MTV 2', a_trip='Mars - Earth')
            add_simple_date_filter(fw=p_filters_window, a_event='Arrives', a_when='Before', a_date=[1, 1, 2034])
            add_simple_date_filter(fw=p_filters_window, a_event='Arrives', a_when='After', a_date=[1, 1, 2032])
            add_tof_filter(fw=p_filters_window, a_operator='<=', a_value=240)

    if a_mission_name == 'NASA DRA5.0 Long-Stay - All-up':
        # Create the s/c.
        if p_main_window:
            add_sc_cargo_oneway(mw=p_main_window, a_sc_name='SHAB')
            add_sc_cargo_oneway(mw=p_main_window, a_sc_name='DAV')
            add_sc_crewed_twoway(mw=p_main_window, a_sc_name='MTV')

            # Create the edit filters window.
            p_main_window.clicked_apply_filter(a_build_test_mission=a_mission_name)
        # Add filters.
        if p_filters_window:
            select_sc_and_trip(fw=p_filters_window, a_sc='SHAB', a_trip='Earth - Mars')
            add_simple_date_filter(fw=p_filters_window, a_event='Arrives', a_when='After', a_date=[1, 1, 2028])
            add_simple_date_filter(fw=p_filters_window, a_event='Arrives', a_when='Before', a_date=[1, 1, 2030])
            select_sc_and_trip(fw=p_filters_window, a_sc='DAV', a_trip='Earth - Mars')
            add_simple_date_filter(fw=p_filters_window, a_event='Arrives', a_when='After', a_date=[1, 1, 2028])
            add_simple_date_filter(fw=p_filters_window, a_event='Arrives', a_when='Before', a_date=[1, 1, 2030])
            select_sc_and_trip(fw=p_filters_window, a_sc='MTV', a_trip='Earth - Mars')
            add_simple_date_filter(fw=p_filters_window, a_event='Arrives', a_when='After', a_date=[1, 1, 2028])
            add_simple_date_filter(fw=p_filters_window, a_event='Arrives', a_when='Before', a_date=[1, 1, 2030])
            select_sc_and_trip(fw=p_filters_window, a_sc='MTV', a_trip='Mars - Earth')
            add_complex_date_filter(fw=p_filters_window, a_event='Departs', a_value='At least', a_value2=180,
                                    a_value3='After', a_sc='MTV', a_sc_trip='Earth - Mars', a_sc_trip2='Landing')


    if a_mission_name == 'NASA DRA5.0 Short-Stay - Pre-deployment':
        # Create the s/c.
        if p_main_window:
            pass
        # Add filters.
        if p_filters_window:
            pass
    if a_mission_name == 'NASA DRA5.0 Short-Stay - All-up':
        # Create the s/c.
        if p_main_window:
            pass
        # Add filters.
        if p_filters_window:
            pass

# Note: mw stands for main window :).
def find_min_max_idx(a_df, p_find='Min', p_col='dvt'):
    """
    Find the index of the min or max value of the p_col within the DataFrame a_df.

    :param a_df: a Pandas DataFrame.
    :param p_find: find a min or a max.
    :param p_col: the dataframe column where to search.
    :return: the index of the DataFrame row.
    """
    # Convert the input, if needed.
    if p_col == 'Departure date':
        p_col = 'DepDates'
    elif p_col == 'Arrival date':
        p_col = 'ArrivDates'

    if p_find == 'Min':
        if p_col =='DepDates':
            ix = a_df[[p_col]].DepDates.apply(QDate.toJulianDay).idxmin()
            return pd.Series(data={p_col: ix}, index=[p_col])
        elif p_col == 'ArrivDates':
            ix = a_df[[p_col]].ArrivDates.apply(QDate.toJulianDay).idxmin()
            return pd.Series(data={p_col: ix}, index=[p_col])
        else:
            return a_df[[p_col]].idxmin()
    elif p_find == 'Max':
        if p_col =='DepDates':
            ix = a_df[[p_col]].DepDates.apply(QDate.toJulianDay).idxmax()
            return pd.Series(data={p_col: ix}, index=[p_col])
        elif p_col == 'ArrivDates':
            ix = a_df[[p_col]].ArrivDates.apply(QDate.toJulianDay).idxmax()
            return pd.Series(data={p_col: ix}, index=[p_col])
        else:
            return a_df[[p_col]].idxmax()

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

def print_dataframe(a_dataframe):
    for i in range(a_dataframe.shape[0]):
        row = a_dataframe.iloc[i]
        print(row.to_list())

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
                sc.reset_trajectory(p_all_trajectories=False, p_trajectory='Earth-Mars')
            if p_trips == 'Mars-Earth':
                sc.reset_trajectory(p_all_trajectories=False, p_trajectory='Mars-Earth')
        elif p_filters_and_trajectories == 'Filters':
        # Reset filters - NOT NEEDED YET.
            if p_trips == 'Both':
                pass
            if p_trips == 'Earth-Mars':
                pass
            if p_trips == 'Mars-Earth':
                pass

def select_sc_and_trip(fw=None, a_sc='', a_trip=''):
    """

    :param fw: pointer to the filters window.
    :param a_sc: str.
    :param a_trip: 'Earth - Mars'|'Mars - Earth'.
    """
    fw.select_spacecraft.setCurrentText(a_sc)
    fw.select_trip.setCurrentText(a_trip)

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
