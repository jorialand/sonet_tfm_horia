import datetime
import sys

from PySide2.QtCore import Slot, QAbstractListModel, QAbstractTableModel, QModelIndex, Qt
from PySide2.QtGui import QColor
from PySide2.QtWidgets import QApplication, QMainWindow

# From module X import class Y.
from src import main_window_ui
from src import sonet_spacecraft as spacecraft
from src.sonet_pcp_filter_qt import sonet_pcp_filter_qt


# QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)  # To avoid AA_ShareOpenGLContexts warning in QtCreator.

# TODO: Instead of a predefined mock_data dict, the user should be capable of adding and removing spacecrafts.
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


# TODO: Move TableModel and ListModel classes outside main_window.py file.
class TableModel(QAbstractTableModel):
    def __init__(self, data, parent=None):
        super(TableModel, self).__init__(parent)
        self.dict_key = sorted(data.keys())[0]  # default key
        self._data = data[self.dict_key]._df_outgoing  # data  # data is a dict, _data is a pandas dataframe


    def set_key(self, key):
        print('TableModel() Slot set_key() called.')
        self.beginResetModel()
        self.dict_key = key
        self.endResetModel()

    def rowCount(self, QModelIndex_parent=None, *args, **kwargs):
        return self._data.shape[0]

    def columnCount(self, QModelIndex_parent=None, *args, **kwargs):
        return self._data.shape[1]

    def data(self, index=QModelIndex, role=None):

        if not index.isValid():
            return None

        row = index.row()
        column = index.column()

        # if role == Qt.DisplayRole:
            #return str(self._data[self.dict_key]._df_outgoing.iloc[row, column])
        if role == Qt.DisplayRole:
            # return str(self._data.iloc[index.row(), index.column()])
            # Get the raw value
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
                return str(self._data.columns[section])
            if orientation == Qt.Vertical:
                return str(self._data.index[section])
        return None
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