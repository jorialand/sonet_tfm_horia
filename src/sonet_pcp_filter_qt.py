import sys

from PySide2.QtCore import QCoreApplication, Qt
from PySide2.QtWidgets import QDialog, QApplication, QDialogButtonBox

from src import sonet_pcp_filter_qt_ui


class sonet_pcp_filter_qt(QDialog, sonet_pcp_filter_qt_ui.Ui_sonet_pcp_filter):
    def __init__(self, *args, ar_list_spacecrafts=[], ar_current_index=-1):
        super(sonet_pcp_filter_qt, self).__init__(*args)#, **kwargs)
        self.setupUi(self)
        self.init(ar_list_spacecrafts, ar_current_index)

    def init(self, ar_list_spacecrafts=[], ar_current_index=-1):
        # Connect signals and slots.
        self.btn_accept = self.dialog_button_box.button(QDialogButtonBox.Ok)
        self.btn_accept.clicked.connect(self.accept)

        self.btn_cancel = self.dialog_button_box.button(QDialogButtonBox.Cancel)
        self.btn_cancel.clicked.connect(self.reject)

        self.select_spacecraft.currentIndexChanged.connect(self.cmb_select_spacecraft_changed)
        self.cb_energy.stateChanged.connect(self.cb_energy_changed)
        self.combo_energy_parameter.currentIndexChanged.connect(self.cmb_energy_parameter_changed)

        # Fill select_spacecraft combo with the available spacecrafts and select the current one.
        self.init_select_spacecraft_combo(ar_list_spacecrafts, ar_current_index)

    def init_select_spacecraft_combo(self,  ar_list_spacecrafts=[], ar_current_index=-1):
        """
        Fill select_spacecraft combo box with the available spacecrafts.
        And select the one selected by the user.
        If no selection (ar_current_index = -1, then 0 should be selected, which tells
        the user that it has to do a selection.
        :param ar_list_spacecrafts:
        :param ar_current_index:
        :return:
        """
        self.select_spacecraft.addItems(ar_list_spacecrafts)
        if ar_current_index is not -1:
            self.select_spacecraft.setCurrentIndex(ar_current_index + 1)  # The '+1' is because the combo box is already
            # populated with 'Select spacecraft...' item when the above addItems() is executed.
        else:
            self.select_spacecraft.setCurrentIndex(0)

    def cmb_select_spacecraft_changed(self, index):
        """
        Updates the 'Select trip' combo box every time the 'Select spacecraft' changes.
        If the spacecraft is crewed, then it will have both outgoing and incoming trips.
        If the spacecraft is cargo, then it will have only outgoing trip.
        Each trip is represented by a Pandas dataframe.
        :param index:
        :return:
        """
        print('Slot cmb_select_spacecraft_changed() called.')
        print(self.select_spacecraft.itemText(index))

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
    QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)  # To avoid AA_ShareOpenGLContexts Qt warning.
    app = QApplication([])
    dialog = sonet_pcp_filter_qt( )
    dialog.show( )
    sys.exit(app.exec_( ))
