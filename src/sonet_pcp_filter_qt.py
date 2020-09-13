import sys

from PySide2.QtCore import QCoreApplication, Qt
from PySide2.QtWidgets import QDialog, QApplication, QDialogButtonBox

from src import sonet_pcp_filter_qt_ui


class sonet_pcp_filter_qt(QDialog, sonet_pcp_filter_qt_ui.Ui_sonet_pcp_filter):
    def __init__(self, *args, **kwargs):
        super(sonet_pcp_filter_qt, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.init()

    def init(self):
        self.top_left_group_box.setEnabled(False)  # TODO Implement dept arriv filter group box.
        self.time_of_flight_group_box.setEnabled(False)  # TODO Implement time of flight filter group box.

        # Connect signals and slots
        self.btn_accept = self.dialog_button_box.button(QDialogButtonBox.Ok)
        self.btn_accept.clicked.connect(self.accept)

        self.btn_cancel = self.dialog_button_box.button(QDialogButtonBox.Cancel)
        self.btn_cancel.clicked.connect(self.reject)

        self.cb_energy.stateChanged.connect(self.cb_energy_changed)
        self.combo_energy_parameter.currentIndexChanged.connect(self.cmb_energy_parameter_changed)

    def cmb_energy_parameter_changed(self,index):
        cmb_units = self.combo_energy_units

        if index in [0,1,2]:
            #km/s
            cmb_units.setCurrentIndex(0)
            return 0
        elif index in [3,4]:
            #km2/s2
            cmb_units.setCurrentIndex(1)
            return 0
        elif index in [5]:
            #º
            cmb_units.setCurrentIndex(2)
            return 0
        else:
            print('Warning: cmb_energy_parameter_changed()')

    def cb_energy_changed(self):
        cb = self.cb_energy
        if cb.isChecked():
            self.enable_energy_combos(True)
        else:
            self.enable_energy_combos(False)
    def enable_energy_combos(self, ar_enable):
        self.combo_energy_parameter.setEnabled(ar_enable)
        self.combo_energy_operator.setEnabled(ar_enable)
        self.spin_energy_number.setEnabled(ar_enable)

    def pb_reset_clicked(self):
        pass
    def pb_add_clicked(self):
        pass
    def pb_delete_clicked(self):
        pass
    def pb_deleteAll_clicked(self):
        pass

if __name__ == "__main__":
    QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
    app = QApplication([])
    dialog = sonet_pcp_filter_qt( )
    dialog.show( )
    sys.exit(app.exec_( ))
