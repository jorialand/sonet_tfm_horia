import sys
from datetime import datetime

import pandas as pd
from PySide2.QtCore import QAbstractTableModel, Qt
from PySide2.QtWidgets import QApplication, QMainWindow, QAction

from src import main_window_ui
from src.sonet_pcp_filter_qt import sonet_pcp_filter_qt  # From module X import class Y.


# QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)  # To avoid AA_ShareOpenGLContexts warning in QtCreator.


class MainWindow(QMainWindow, main_window_ui.Ui_main_window):
    """
    docstring
    """

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        # Pandas model
        dirPath = '/Users/Jorialand/code/tfm/sonet/sonet_tfm_horia/src/'
        df = pd.read_csv(dirPath + '10kPCP_Earth2Mars.txt')
        model = pandasModel(df)
        self.pcp_table.setModel(model)

        # Menu bar
        self.menubar.setNativeMenuBar(False)

        # Exit QAction
        exit_action = QAction("Exit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.exit_app)

        # Connect signals and slots
        self.sonet_pcp_filter_pb_qt.clicked.connect(self.open_sonet_pcp_filter_qt)

    def open_sonet_pcp_filter_qt(self):
        print("Slot open_sonet_pcp_filter_qt has been called!")
        # dialog = sonet_pcp_filter_qt()
        dialog = sonet_pcp_filter_qt(self)
        dialog.setModal(True)
        dialog.show( )

    #@Slot()
    def exit_app(self, checked):
        sys.exit( )


class pandasModel(QAbstractTableModel):
    """
    Qt table model representing the Porkchop plot data coming from Pandas.
    rowCount(), columnCount(), and data() are required to be implemented to properly subclass QAbstractTableModel.
    +info: https://www.learnpyqt.com/courses/model-views/qtableview-modelviews-numpy-pandas/
    """

    def __init__(self, data):
        # QAbstractTableModel.__init__(self)
        super(pandasModel, self).__init__( )
        self._data = data

    def rowCount(self, parent=None):
        """
        docstring
        """

        return self._data.shape[0]

    def columnCount(self, parent=None):
        """
        docstring
        """
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        """
        The structure of the pandas data.
        :param index: the current index. The row and the column.
        :param role: Qt.DisplayRole means what is being represented.
        """
        if index.isValid():
            if role == Qt.DisplayRole:
                # Get the raw value
                value = self._data.iloc[index.row(), index.column()]
                # return str(self._data.iloc[index.row(), index.column()])

                # Perform per-type checks and render accordingly.
                if isinstance(value, datetime):
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
        return None

    def headerData(self, section, orientation, role):
        """

        :param section:
        :param orientation:
        :param role:
        """
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._data.columns[section])
            if orientation == Qt.Vertical:
                return str(self._data.index[section])
        return None



if __name__ == "__main__":

    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec_())

# TODO: Format table to two decimals.
# TODO: Create spacecraft object, with two PCP tables.
# TODO: Create two spacecrafts, and start playing with filters...
# TODO: Connect spacecraft PCP table with the Pandas-Qt model-view...
#
