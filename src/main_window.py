import sys

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

        self.menubar.setNativeMenuBar(False)

        ## Exit QAction
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

    # @Slot()
    def exit_app(self, checked):
        sys.exit( )


class pandasModel(QAbstractTableModel):
    """
    docstring
    """

    def __init__(self, data):
        QAbstractTableModel.__init__(self)
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

        :param index:
        :param role:
        """
        if index.isValid( ):
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row( ), index.column( )])
        return None

    def headerData(self, col, orientation, role):
        """

        :param col:
        :param orientation:
        :param role:
        """
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        return None



if __name__ == "__main__":

    app = QApplication(sys.argv)

    dirPath = '/Users/Jorialand/code/tfm/sonet/sonet_tfm_horia/src/'
    df = pd.read_csv(dirPath + '1MPCP_Earth2Mars.txt')
    # print(df.head())
    model = pandasModel(df)

    main_window = MainWindow()
    main_window.pcp_table.setModel(model)
    main_window.show()

    sys.exit(app.exec_())

# TODO: Implement model Pandas-Qt.
# TODO: Create spacecraft object.
# TODO: Connect spacecraft PCP table with the Pandas-Qt model-view.
#
