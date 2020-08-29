import sys

from PySide2.QtCore import Slot, QAbstractListModel, QAbstractTableModel, Qt
from PySide2.QtWidgets import QApplication, QMainWindow

from src import main_window_ui
from src import sonet_spacecraft as spacecraft
from src.sonet_pcp_filter_qt import sonet_pcp_filter_qt  # From module X import class Y.


# from src.sonet_mission_tree_model import SonetMissionTreeModel

# QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)  # To avoid AA_ShareOpenGLContexts warning in QtCreator.

def build_mock_data():
    result = {'Spacecraft 1': spacecraft.SonetSpacecraft(),
              'Spacecraft 2': spacecraft.SonetSpacecraft(),
              'Spacecraft 3': spacecraft.SonetSpacecraft(),
              'Spacecraft 4': spacecraft.SonetSpacecraft(),
              'Spacecraft 5': spacecraft.SonetSpacecraft()}
    return result


mock_data = build_mock_data()


class MainWindow(QMainWindow, main_window_ui.Ui_main_window):
    """
    docstring
    """

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        # The container for the mission tree objects.
        # self._mission_tree = {}
        # self.mission_tree_model = ListModel()
        # self.sonet_mission_tree_qlv.setModel(self.mission_tree_model)
        # Menu bar
        self.menubar.setNativeMenuBar(False)  # I'd problems with MacOSX native menubar, the menus didn't appear.
        # Exit QAction
        # No funciona! TODO: Arreglar Exit QAction.
        # exit_action = QAction("Exit", self)
        # exit_action.setShortcut("Ctrl+Q")
        # exit_action.triggered.connect(self.exit_app)

        # Connect signals and slots
        self.sonet_pcp_filter_qpb.clicked.connect(self.open_sonet_pcp_filter_qt)
        self.sonet_add_spacecraft_qpb.clicked.connect(self.new_spacecraft)

    # Signals should be defined only within classes inheriting from QObject!
    # +info:https://wiki.qt.io/Qt_for_Python_Signals_and_Slots
    def getTableModel(self):
        return self._table_model

    @Slot()
    def open_sonet_pcp_filter_qt(self):
        print("Slot open_sonet_pcp_filter_qt called.")
        # dialog = sonet_pcp_filter_qt()
        dialog = sonet_pcp_filter_qt(self)
        dialog.setModal(True)
        dialog.show()

    @Slot()
    def new_spacecraft(self):
        print("Slot new_spacecraft called.")

        self._list_model = ListModel(mock_data)
        self.sonet_mission_tree_qlv.setModel(self._list_model)
        self.sonet_mission_tree_qlv.clicked.connect(self._list_model.list_clicked)
        self._table_model = TableModel(mock_data)
        self.sonet_pcp_table_qtv_outgoing.setModel(self._table_model)

    # self.sonet_pcp_table_qtv_outgoing.setModel(self._mission_tree.get(new_key).model_outgoing)
    # self.sonet_pcp_table_qtv_incoming.setModel(self._mission_tree.get(new_key).model_incoming)

    @Slot()
    def exit_app(self):
        print("Slot exit_app called.")
        sys.exit()


class TableModel(QAbstractTableModel):
    def __init__(self, data, parent=None):
        super(TableModel, self).__init__(parent)
        self._data = data  # _data is a dict
        # defualt key
        self.dict_key = sorted(self._data.keys())[0]

    def set_key(self, key):
        print('TableModel() Slot set_key() called.')
        self.beginResetModel()
        self.dict_key = key
        self.endResetModel()

    def rowCount(self, QModelIndex_parent=None, *args, **kwargs):
        return self._data[self.dict_key]._df_outgoing.shape[0]

    def columnCount(self, QModelIndex_parent=None, *args, **kwargs):
        return self._data[self.dict_key]._df_outgoing.shape[1]

    def data(self, QModelIndex, int_role=None):
        row = QModelIndex.row()
        column = QModelIndex.column()
        if int_role == Qt.DisplayRole:
            return str(self._data[self.dict_key]._df_outgoing.iloc[row, column])


class ListModel(QAbstractListModel):
    def __init__(self, data, parent=None):
        super(ListModel, self).__init__(parent)
        self._data = sorted(data.keys())

    def list_clicked(self, index):
        row = index.row()
        key = self._data[row]
        main_window.getTableModel().set_key(key)


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

# TODO_DONE: tasks at the begining were not being tracked.
# TODO_DONE: Format table to two decimals.
# TODO_DONE: Create spacecraft object, with two PCP tables.
# TODO: Add the current spacecrafts to the Mission tree QListView.
# TODO: When the user selects one of the spacecrafts in the Mission tree, the PCP table QTableView shall be updated with the PCP pandas models.
# TODO: Create two spacecrafts, and start playing with filters...
# TODO: Connect spacecraft PCP table with the Pandas-Qt model-view...
#
