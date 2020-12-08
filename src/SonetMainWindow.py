"""
This is the SonetMainWindow class, inherits from QMainWindow.

Author: Horia Ghionoiu Martínez.
Project: Sonet Mars Mission Architecture Planner
Started:
Code submitted:
Project defense:
"""
import datetime
import sys

import pandas as pd
# From module X import class Y.
from PySide2.QtCore import QAbstractListModel, QAbstractTableModel, QModelIndex, Qt
from PySide2.QtGui import QColor
from PySide2.QtWidgets import QMainWindow, QApplication
from fbs_runtime.application_context.PySide2 import ApplicationContext

from src import database
from src import sonet_main_window_ui
from src.SonetPCPFilterQt import SonetPCPFilterQt
from src.SonetSpacecraft import SonetSpacecraft
from src.SonetUtils import SONET_DEBUG, TripType


# QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)  # To avoid AA_ShareOpenGLContexts warning in QtCreator.

# TODO When user selects one item, all row should be selected instead.

def get_main_window():
    """
    Getter method.
    """
    return main_window

def force_table_view_update():
    """
    Force update of the selected table view.
    """
    index = get_main_window().sonet_pcp_tabs_qtw.currentIndex()
    get_main_window().sonet_pcp_tabs_qtw.currentChanged.emit(index)


class SonetMainWindow(QMainWindow, sonet_main_window_ui.Ui_main_window):
    """
    SonetMainWindow class, representing the main application window.
    """

    def __init__(self, *args, **kwargs):
        super(SonetMainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        # Menu bar
        self.menubar.setNativeMenuBar(False)  # I'd problems with MacOSX native menubar, the menus didn't appear

        # TODO Añadir QActions (e.g. Exit, Save, etc.)

        # Objects database
        self.n = 0  # Counter for spacecrafts naming, to be deprecated
        # Table models, it should be declared prior to list model
        self._table_model_outgoing = TableModel(TripType.OUTGOING)
        self._table_model_incoming = TableModel(TripType.INCOMING)
        self.sonet_pcp_table_qtv_outgoing.setModel(self._table_model_outgoing)
        self.sonet_pcp_table_qtv_incoming.setModel(self._table_model_incoming)

        # List model, it should be declared after table model
        self._list_model = ListModel()
        self.sonet_mission_tree_qlv.setModel(self._list_model)
        # TODO: Explain why this ordering when declaring table + list model

        # Connect signals and slots
        self.sonet_add_spacecraft_qpb.clicked.connect(self.clicked_new_spacecraft)
        self.sonet_remove_spacecraft_qpb.clicked.connect(self.clicked_remove_spacecraft)
        self.sonet_pcp_filter_qpb.clicked.connect(self.clicked_apply_filter)

        self.sonet_mission_tree_qlv.clicked.connect(self._list_model.list_clicked)
        self.sonet_pcp_tabs_qtw.currentChanged.connect(self.clicked_tab)

    # Signals should be defined only within classes inheriting from QObject!
    # +info:https://wiki.qt.io/Qt_for_Python_Signals_and_Slots

    def get_table_model(self, pcp_table_model=None):
        switcher = {
            TripType.OUTGOING: self._table_model_outgoing,
            TripType.INCOMING: self._table_model_incoming
        }
        return switcher.get(pcp_table_model, 'Error in SonetMainWindow.get_table_model: '
                                             'No model found with the requested argument')

    def get_list_model(self):
        return self._list_model

    def clicked_apply_filter(self):
        if SONET_DEBUG:
            print("clicked_apply_filter")

        arg1 = database.get_spacecrafts_list()
        arg2 = self.sonet_mission_tree_qlv.currentIndex().row()
        filter_dialog_qt = SonetPCPFilterQt(self, ar_list_spacecrafts=arg1, ar_current_index=arg2)

        # Pre-action
        filter_dialog_qt.setModal(True)
        filter_dialog_qt.setSizeGripEnabled(True)

        filter_dialog_qt.exec_()
        # Force Qt repaint to update the table views.
        # TODO Awkward update, to improve.
        index = get_main_window().sonet_mission_tree_qlv.currentIndex()
        self.sonet_mission_tree_qlv.clicked.emit(index)

    def clicked_new_spacecraft(self):
        """
        This method is called when clicking over 'Add SonetSpacecraft' QPushButton, it creates a new SonetSpacecraft.
        :return: True if OK, False else.
        """
        if SONET_DEBUG:
            print('SonetMainWindow.clicked_new_spacecraft()')
        ###
        # self.sp = SonetSpacecraft()
        # self.sp.set_spacecraft_type(SpacecraftType.CREWED)
        # self.sp.set_has_return_trajectory(False)
        # self.sp.set_filters()
        # filter_ = self.sp.get_filter()
        # filtered_pcp_table = filter_.get_filtered_pcp()
        ###

        # Create new SonetSpacecraft
        self.n += 1
        spacecraft_type_crew = self.sonet_spacecraft_type_qcmb.currentText()
        spacecraft_type_return = self.sonet_spacecraft_type_has_return_trajectory_qcmb.currentText()
        database.db['Spacecraft ' + str(self.n)] = SonetSpacecraft(spacecraft_type_crew, spacecraft_type_return)

        # Update list model
        lm = self.get_list_model()
        lm.update()

        if SONET_DEBUG:
            print('Created Spacecraft ' + str(self.n)
                  + ' (' + spacecraft_type_crew + ', ' + spacecraft_type_return + ')')
        return True

    #@Slot()
    def clicked_remove_spacecraft(self):
        # Get the current list view selection.
        selection = self.sonet_mission_tree_qlv.currentIndex().row()

        # If there's no SonetSpacecraft, then return.
        db = database.db
        if len(list(db.keys())) is 0:
            print('There is no spacecrafts to remove.')
            return 0
        # If there is no selection, remove last SonetSpacecraft.
        if (selection is -1):
            selection = len(list(db.keys())) - 1

        # Remove it from the database.
        key = list(db.keys())[selection] # The selected object (e.g. SonetSpacecraft).
        # print(selection)
        # print(key)
        del db[key]

        # Update table models.
        self.get_table_model(TripType.OUTGOING).reset_model()
        self.get_table_model(TripType.INCOMING).reset_model()

        # Update list model.
        lm = self.get_list_model()
        lm.update()

        print(key + ' removed.')
        return True

    #@Slot()
    def clicked_tab(self, index):
        if SONET_DEBUG:
            print('Slot clicked_tab called.')
        if self.sonet_mission_tree_qlv.currentIndex().row() is not -1:
            if index is 0:
                # Outgoing trip selected.
                n_filtered = main_window._table_model_outgoing._data.shape[0]
                n = database.get_pcp_table(TripType.OUTGOING).shape[0]
                self.sonet_label_rows_filtered_visible.setText(str(n_filtered) + ' rows visible out of ' + str(n))
            elif index is 1:
                # Incoming trip selected.
                n_filtered = main_window._table_model_incoming._data.shape[0]
                n = database.get_pcp_table(TripType.OUTGOING).shape[0]
                self.sonet_label_rows_filtered_visible.setText(str(n_filtered) + ' rows visible out of ' + str(n))

    #@Slot()
    def exit_app(self):
        # print("Slot exit_app called.")
        sys.exit()


# TODO: Move TableModel and ListModel classes outside main_window.py file.
class TableModel(QAbstractTableModel):
    """
    TODO docstring TableModel()
    """

    def __init__(self, a_trip_type=None, parent=None):
        super(TableModel, self).__init__(parent)
        self._data = pd.DataFrame()  # A Pandas dataframe
        self._trip_type = a_trip_type  # TripType.[OUTGOING|INCOMING]

    def add_spacecraft(self):
        n = len(self._data.keys())

        # The XResetModel() notifies all the attached views that the model is about to be updated.
        self.beginResetModel()
        self._data['Spacecraft ' + str(n + 1)] = SonetSpacecraft()
        self.endResetModel()

        # Custom update procedure to update the SonetMainWindow's list model and list view.
        lm = get_main_window().get_list_model()
        lm.update()

    def set_model_data(self, a_the_filtered_dataframe=None):
        """
        Set the table model's internal _data, stored as dataframe.
        """
        if SONET_DEBUG:
            print('TableModel.set_model_data('+ str(self._trip_type) + ') called.')

        self.beginResetModel()
        self._data = a_the_filtered_dataframe.reset_index(drop=True)
        self.endResetModel()

    def reset_model(self):
        """
        Reset the table model.
        """
        if SONET_DEBUG:
            print('TableModel() Slot reset_model() called.')

        self.beginResetModel()
        self._data = None
        self.endResetModel()
        return True

    def rowCount(self, QModelIndex_parent=None, *args, **kwargs):
        # try:
        #     self.dict_key
        # except AttributeError:
        #     return 0
        # else:
        #     return self._data[self.dict_key].get_pcp_table(self._trip_type).shape[0]
        if self._data is None:
            return 0
        return self._data.shape[0]  # Number of rows of the dataframe

    def columnCount(self, QModelIndex_parent=None, *args, **kwargs):
        # try:
        #     self.dict_key
        # except AttributeError:
        #     return 0
        # else:
        #     return self._data[self.dict_key].get_pcp_table(self._trip_type).shape[1]
        if self._data is None:
            return 0
        return self._data.shape[1]  # Number of columns of the dataframe

    def data(self, index=QModelIndex, role=None):
        if not index.isValid():
            return None

        row = index.row()
        column = index.column()

        # if role == Qt.DisplayRole:
        # return str(self._data[self.dict_key]._df_outgoing.iloc[row, column])
        if role == Qt.DisplayRole:
            # return str(self._data.iloc[index.row(), index.column()])
            # Get the raw value
            # value = self._data[self.dict_key].get_pcp_table(self._trip_type).iloc[row, column]
            value = self._data.iloc[row, column]

            # Perform per-type checks and render accordingly.
            if isinstance(value, datetime.datetime):
                # Render time to YYY-MM-DD.
                return value.strftime("%Y-%m-%d")

            if isinstance(value, float):
                # Render float to 2 dp
                return "%.2f" % value

            if isinstance(value, str):
                # Render strings with quotes
                return '"%s"' % value

            # Default (anything not captured above: e.g. int)
            return value

        if role == Qt.BackgroundRole:
            # Pair rows will have different color, to visually distinguish them from the even ones.
            if row % 2 is not 0:
                return QColor(255, 230, 255)
            # Very light blue 230, 242, 255
            # Very light purple 240, 240, 245
            # Very light pink 255, 230, 255
        return None

    def headerData(self, section, orientation, role):

        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                # return str(self._data[self.dict_key].get_pcp_table(self._trip_type).columns[section])
                return str(self._data.columns[section])
            if orientation == Qt.Vertical:
                # return str(self._data[self.dict_key].get_pcp_table(self._trip_type).index[section])
                return str(self._data.index[section])
        return None


class ListModel(QAbstractListModel):
    """
    TODO docstring ListModel()
    """

    def __init__(self, data=None, parent=None):
        super(ListModel, self).__init__(parent)
        self._data = {}.keys()  # It's a dictionary keys

    def get_data(self):
        return list(self._data)

    def list_clicked(self, index):
        """
        Slot executed whenever an item from the ListModel is clicked. It sets both
        the outgoing and incoming table models, and updates both associated table views.

        There are two possible situations. The clicked spacecraft has only
        TripType.OUTGOING trip type, or both TripType.OUTGOING and TripType.INCOMING.
        If it is the first case, then for the return trip, an empty dataframe
        is displayed.
        """
        # key is a string identifying a SonetSpacecraft objet within the database.
        row = index.row()
        try:
            key = list(self._data)[row]
        except IndexError:
            if row is -1:
                # No spacecraft selected, possible when entered this method because
                # of emmited signal, no problem in this cases.
                return False
            print('Warning in list_clicked')

        if SONET_DEBUG:
            print('ListModel.list_clicked: ' + key + ' selected.')

        the_spacecraft = database.db[key]
        the_filter = the_spacecraft.get_filter()

        # The method get_filter returns a SonetTrajectoryFilter if the spacecraft has only
        # one trip, and a list of them otherwise.
        # Once we get the filtered porkchop dataframe, we display it by setting it as _data and resetting the table
        # model.
        try:
            # Case where spacecraft only has got only outgoing trajectory.
            the_filtered_dataframe = the_filter.get_filtered_pcp()
            main_window._table_model_outgoing.set_model_data(the_filtered_dataframe)
            the_filtered_dataframe = pd.DataFrame()
            main_window._table_model_incoming.set_model_data(the_filtered_dataframe)

            if SONET_DEBUG:
                print('This spacecraft has no return trajectory.')
        except AttributeError:
            # Case where spacecraft only has got both outgoing and incoming trajectories.
            # Outgoing. (la magia ocurre aquí)
            the_filtered_dataframe = the_filter[0].get_filtered_pcp()
            main_window._table_model_outgoing.set_model_data(the_filtered_dataframe)
            # Incoming.
            the_filtered_dataframe = the_filter[1].get_filtered_pcp()
            main_window._table_model_incoming.set_model_data(the_filtered_dataframe)
        except:
            print('Error in ListModel.list_clicked.')
            return False

        force_table_view_update()

    def update(self):
        # print('ListModel() Slot update() called.')
        self.beginResetModel()
        self._data = list(database.db.keys())
        self.endResetModel()

    def rowCount(self, QModelIndex_parent=None, *args, **kwargs):
        return len(self._data)

    def data(self, QModelIndex, int_role=None):
        row = QModelIndex.row()
        if int_role == Qt.DisplayRole:
            return str(list(self._data)[row])

    def flags(self, QModelIndex):
        return Qt.ItemIsEnabled | Qt.ItemIsSelectable

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    main_window = SonetMainWindow()
    main_window.show()

    sys.exit(app.exec_())
    # exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    # sys.exit(exit_code)


    # appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    # window = QMainWindow()
    # window.resize(250, 150)
    # window.show()
    # exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    # sys.exit(exit_code)