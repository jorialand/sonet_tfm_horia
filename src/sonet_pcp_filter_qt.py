import sys

from PySide2.QtCore import QCoreApplication, Qt
from PySide2.QtWidgets import QDialog, QApplication

from src import sonet_pcp_filter_qt_ui


class sonet_pcp_filter_qt(QDialog, sonet_pcp_filter_qt_ui.Ui_sonet_pcp_filter):
    def __init__(self, *args, **kwargs):
        super(sonet_pcp_filter_qt, self).__init__(*args, **kwargs)
        self.setupUi(self)



if __name__ == "__main__":
     QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
     app = QApplication([])
     dialog = sonet_pcp_filter_qt()
     dialog.show()
     sys.exit(app.exec_())
