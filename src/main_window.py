import sys

from PySide2.QtCore import QCoreApplication, Qt
from PySide2.QtWidgets import QApplication, QMainWindow

from src import main_window_ui
from src.sonet_pcp_filter_qt import sonet_pcp_filter_qt  # From module X import class Y.

QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)  # To avoid AA_ShareOpenGLContexts warning in QtCreator.


###
class MainWindow(QMainWindow, main_window_ui.Ui_main_window):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        # Connect signals and slots
        self.sonet_pcp_filter_pb_qt.clicked.connect(self.open_sonet_pcp_filter_qt)

    def open_sonet_pcp_filter_qt(self):
        print("Slot open_sonet_pcp_filter_qt has been called!")
        #dialog = sonet_pcp_filter_qt()
        dialog = sonet_pcp_filter_qt(self)
        dialog.setModal(True)
        dialog.show()

if __name__ == "__main__":

    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec_())
