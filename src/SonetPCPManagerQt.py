

from PySide2.QtWidgets import QDialog, QStatusBar, QFileDialog, QDialogButtonBox

from src import sonet_pcp_manager_ui  # The user interface, created with QtCreator.
from src.SonetUtils import SONET_MSG_TIMEOUT, SONET_PCP_DATA_DIR


# ==============================================================================================
# ==============================================================================================
#
#
#                                    CLASS SonetPCPManagerQt
#
#
# ==============================================================================================
# ==============================================================================================


class SonetPCPManagerQt(QDialog, sonet_pcp_manager_ui.Ui_sonet_pcp_manager):
    """
    Window in charge of managing the available PCP trajectories within the app,
    and also generates new ones, if desired.

    The matlab data is stored in .mat files, in matrix format.
    The app needs pcp data in table format. The tables are stored in .pkl files.
    """
    def __init__(self, *args, **kwargs):
        super(SonetPCPManagerQt, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.show()

        # Status bar,for messages to the user.
        self.status_bar = QStatusBar()
        self.status_bar.setSizeGripEnabled(False)
        self.status_bar_HLayout.addWidget(self.status_bar)

        # Signals and slots connect.
        self.sonet_read_pcp_outgoing_trajectories_matrix_qpb.clicked.connect(self.clicked_read_pcp_matrix_file_outgoing)
        self.sonet_read_pcp_incoming_trajectories_matrix_qpb.clicked.connect(self.clicked_read_pcp_matrix_file_incoming)
        self.sonet_dvt_limit_qcb.stateChanged.connect(self.clicked_dvt_limit_checkbox)
        self.sonet_convert_pcp_2_table_format_qpb.clicked.connect(self.clicked_convert_pcp_2_table_format)
        self.sonet_read_pcp_outgoing_trajectories_table_qpb.clicked.connect(self.clicked_read_pcp_table_file_outgoing)
        self.sonet_read_pcp_incoming_trajectories_table_qpb.clicked.connect(self.clicked_read_pcp_table_file_incoming)

        self.btn_OK = self.sonet_ok_cancel_qpb_group.button(QDialogButtonBox.Ok)
        self.btn_OK.clicked.connect(self.clicked_ok)
        self.btn_OK.clicked.connect(self.accept)

        self.btn_cancel = self.sonet_ok_cancel_qpb_group.button(QDialogButtonBox.Cancel)
        self.btn_cancel.clicked.connect(self.clicked_cancel)
        self.btn_cancel.clicked.connect(self.reject)

        # sonet_log(SonetLogType.INFO, 'class_tal.method_tal')
        # self.status_bar.showMessage('tal.', SONET_MSG_TIMEOUT)

    def clicked_cancel(self):
        pass

    def clicked_convert_pcp_2_table_format(self):
        """
        Converts matrix to tabular pcp data. .mat -> .pkl.
        """
        self.status_bar.showMessage('SonetPCPManagerQt.clicked_convert_pcp_2_table_format."Not implemented."',
                                    SONET_MSG_TIMEOUT)
        pass

    def clicked_dvt_limit_checkbox(self):
        """
        Activate/deactivate the dvt limit line edit widget, depending of the check box state.
        """
        self.sonet_dvt_limit_qdoublespinbox.setEnabled(self.sonet_dvt_limit_qcb.isChecked())

    def clicked_ok(self):
        pass

    def clicked_read_pcp_matrix_file_incoming(self):
        """
        Opens a select file dialog, the user has to select a valid matlab file containing the pcp data.
        """
        filename, filter_ = QFileDialog.getOpenFileName(parent=self, caption='Read PCP file (.mat)',
                                                        dir=SONET_PCP_DATA_DIR,
                                                        filter='*.mat')
        if filename:
            self.sonet__incoming_trajectories_matrix_line_edit.setText(filename)

    def clicked_read_pcp_matrix_file_outgoing(self):
        """
        Opens a select file dialog, the user has to select a valid matlab file containing the pcp data.
        """
        filename, filter_ = QFileDialog.getOpenFileName(parent=self, caption='Read PCP file (.mat)',
                                                        dir=SONET_PCP_DATA_DIR,
                                                        filter='*.mat')
        if filename:
            self.sonet__outgoing_trajectories_matrix_line_edit.setText(filename)

    def clicked_read_pcp_table_file_incoming(self):
        """
        Opens a select file dialog, the user has to select a valid pickle file containing the pcp data.
        """
        filename, filter_ = QFileDialog.getOpenFileName(parent=self, caption='Read PCP file (.pkl)',
                                                        dir=SONET_PCP_DATA_DIR,
                                                        filter='*.pkl')
        if filename:
            self.sonet__incoming_trajectories_table_line_edit.setText(filename)

    def clicked_read_pcp_table_file_outgoing(self):
        """
        Opens a select file dialog, the user has to select a valid pickle file containing the pcp data.
        """
        filename, filter_ = QFileDialog.getOpenFileName(parent=self, caption='Read PCP file (.pkl)',
                                                        dir=SONET_PCP_DATA_DIR,
                                                        filter='*.pkl')
        if filename:
            self.sonet__outgoing_trajectories_table_line_edit.setText(filename)

