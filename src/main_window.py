import datetime
import sys

import pandas as pd
from PySide2.QtCore import Slot, QAbstractListModel, QAbstractTableModel, QModelIndex, Qt
from PySide2.QtGui import QColor
from PySide2.QtWidgets import QApplication, QMainWindow

# From module X import class Y.
from src import main_window_ui
from src import sonet_spacecraft as spacecraft
from src.sonet_pcp_filter_qt import sonet_pcp_filter_qt


# QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)  # To avoid AA_ShareOpenGLContexts warning in QtCreator.

# TODOs
# TODO When user selects one item, all row should be selected instead.

def build_mock_data():
    result = {'Spacecraft 1': spacecraft.SonetSpacecraft(),
              'Spacecraft 2': spacecraft.SonetSpacecraft(),
              'Spacecraft 3': spacecraft.SonetSpacecraft(),
              'Spacecraft 4': spacecraft.SonetSpacecraft(),
              'Spacecraft 5': spacecraft.SonetSpacecraft()}
    return result

def getMainWindow():
    return main_window

def getDB():
    return getMainWindow()._obj_db

class MainWindow(QMainWindow, main_window_ui.Ui_main_window):
    """
    docstring
    """

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        # Menu bar
        self.menubar.setNativeMenuBar(False)  # I'd problems with MacOSX native menubar, the menus didn't appear.

        # TODO Añadir QActions (e.g. Exit, Save, etc.).

        # Objects database
        self._obj_db = {}
        self.n = 0  # Counter for spacecrafts naming, to be deprecated.
        # Table models, it should be declared prior to list model
        self._table_model_outgoing = TableModel('outgoing')
        self._table_model_incoming = TableModel('incoming')
        self.sonet_pcp_table_qtv_outgoing.setModel(self._table_model_outgoing)
        self.sonet_pcp_table_qtv_incoming.setModel(self._table_model_incoming)

        # List model, it should be declared after table model
        self._list_model = ListModel()
        self.sonet_mission_tree_qlv.setModel(self._list_model)

        # Connect signals and slots
        self.sonet_pcp_filter_qpb.clicked.connect(self.open_sonet_pcp_filter_qt)
        self.sonet_add_spacecraft_qpb.clicked.connect(self.new_spacecraft)
        self.sonet_remove_spacecraft_qpb.clicked.connect(self.remove_spacecraft)
        self.sonet_mission_tree_qlv.clicked.connect(self._list_model.list_clicked)

    # Signals should be defined only within classes inheriting from QObject!
    # +info:https://wiki.qt.io/Qt_for_Python_Signals_and_Slots

    def getTableModel(self, pcp_table_model=''):
        switcher = {
            'outgoing': self._table_model_outgoing,
            'incoming': self._table_model_incoming
        }
        return switcher.get(pcp_table_model, 'No model found with the requested argument')

    def getListModel(self):
        return self._list_model

    @Slot()
    def open_sonet_pcp_filter_qt(self):
        # print("Slot open_sonet_pcp_filter_qt called.")
        ans1 = self.getListModel().get_data()
        ans2 = self.sonet_mission_tree_qlv.currentIndex().row()
        filter_dialog_qt = sonet_pcp_filter_qt(self, ar_list_spacecrafts=ans1, ar_current_index=ans2)
        filter_dialog_qt.setModal(True)
        filter_dialog_qt.show()

    @Slot()
    def new_spacecraft(self):
        # print("Slot new_spacecraft called.")

        # Create new spacecraft
        #self.n = self.n + 1
        self.n += 1
        self._obj_db['Spacecraft ' + str(self.n)] = spacecraft.SonetSpacecraft()

        # Update list model
        lm = self.getListModel()
        lm.update()

    @Slot()
    def remove_spacecraft(self):
        # print("Slot remove_spacecraft called.")

        # Get the current list view selection.
        selection = self.sonet_mission_tree_qlv.currentIndex().row()

        # If there's no spacecraft, then return.
        db = getDB()
        if len(list(db.keys())) is 0:
            print('There is no spacecrafts to remove.')
            return 0
        # If there is no selection, remove last spacecraft.
        if (selection is -1):
            selection = len(list(db.keys())) - 1

        # Remove it from the database.
        key = list(db.keys())[selection] # The selected object (e.g. spacecraft).
        # print(selection)
        # print(key)
        del db[key]

        # Update table models.
        self.getTableModel('outgoing').reset_model()
        self.getTableModel('incoming').reset_model()

        # Update list model.
        lm = self.getListModel()
        lm.update()

        return 0

    @Slot()
    def exit_app(self):
        # print("Slot exit_app called.")
        sys.exit()

# TODO: Move TableModel and ListModel classes outside main_window.py file.
class TableModel(QAbstractTableModel):
    """
    TODO docstring TableModel()
    """

    def __init__(self, pcp_table='', parent=None):
        super(TableModel, self).__init__(parent)
        self._data = pd.DataFrame()  # It's a Pandas dataframe
        self._pcp_table = pcp_table

    def add_spacecraft(self):
        n = len(self._data.keys())

        self.beginResetModel()
        self._data['Spacecraft ' + str(n + 1)] = spacecraft.SonetSpacecraft()
        self.endResetModel()

        lm = getMainWindow().getListModel()
        lm.update()

    def set_key(self, key):
        # print('TableModel() Slot set_key() called.')
        self.beginResetModel()
        self._data = getDB()[key].getPCPTable(self._pcp_table)
        self.endResetModel()

    def reset_model(self):
        # print('TableModel() Slot reset_model() called.')
        self.beginResetModel()
        self._data = None
        self.endResetModel()
        return 0

    def rowCount(self, QModelIndex_parent=None, *args, **kwargs):
        # try:
        #     self.dict_key
        # except AttributeError:
        #     return 0
        # else:
        #     return self._data[self.dict_key].getPCPTable(self._pcp_table).shape[0]
        if self._data is None:
            return 0
        return self._data.shape[0]  # Number of rows of the dataframe

    def columnCount(self, QModelIndex_parent=None, *args, **kwargs):
        # try:
        #     self.dict_key
        # except AttributeError:
        #     return 0
        # else:
        #     return self._data[self.dict_key].getPCPTable(self._pcp_table).shape[1]
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
            # value = self._data[self.dict_key].getPCPTable(self._pcp_table).iloc[row, column]
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
                # return str(self._data[self.dict_key].getPCPTable(self._pcp_table).columns[section])
                return str(self._data.columns[section])
            if orientation == Qt.Vertical:
                # return str(self._data[self.dict_key].getPCPTable(self._pcp_table).index[section])
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
        row = index.row()
        key = self._data[row]
        getMainWindow().getTableModel('outgoing').set_key(key)
        getMainWindow().getTableModel('incoming').set_key(key)

    def update(self):
        # print('ListModel() Slot update() called.')
        self.beginResetModel()
        # self._data = sorted(getMainWindow()._obj_db.keys())
        self._data = list(getMainWindow()._obj_db.keys())
        self.endResetModel()

    def rowCount(self, QModelIndex_parent=None, *args, **kwargs):
        return len(self._data)

    def data(self, QModelIndex, int_role=None):
        row = QModelIndex.row()
        if int_role == Qt.DisplayRole:
            return str(self._data[row])

    def flags(self, QModelIndex):
        return Qt.ItemIsEnabled | Qt.ItemIsSelectable

if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec_())
