# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sonet_pcp_manager.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtWidgets import *


class Ui_sonet_pcp_manager(object):
    def setupUi(self, sonet_pcp_manager):
        if not sonet_pcp_manager.objectName():
            sonet_pcp_manager.setObjectName(u"sonet_pcp_manager")
        sonet_pcp_manager.setEnabled(True)
        sonet_pcp_manager.resize(624, 771)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(sonet_pcp_manager.sizePolicy().hasHeightForWidth())
        sonet_pcp_manager.setSizePolicy(sizePolicy)
        sonet_pcp_manager.setMinimumSize(QSize(0, 0))
        sonet_pcp_manager.setMaximumSize(QSize(16777215, 16777215))
        sonet_pcp_manager.setWindowOpacity(0.970000000000000)
        self.gridLayout = QGridLayout(sonet_pcp_manager)
        self.gridLayout.setObjectName(u"gridLayout")
        self.sonet_working_pcp_qgb = QGroupBox(sonet_pcp_manager)
        self.sonet_working_pcp_qgb.setObjectName(u"sonet_working_pcp_qgb")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.sonet_working_pcp_qgb.sizePolicy().hasHeightForWidth())
        self.sonet_working_pcp_qgb.setSizePolicy(sizePolicy1)
        self.gridLayout_3 = QGridLayout(self.sonet_working_pcp_qgb)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.sonet__incoming_trajectories_table_line_edit = QLineEdit(self.sonet_working_pcp_qgb)
        self.sonet__incoming_trajectories_table_line_edit.setObjectName(u"sonet__incoming_trajectories_table_line_edit")
        self.sonet__incoming_trajectories_table_line_edit.setReadOnly(True)

        self.gridLayout_3.addWidget(self.sonet__incoming_trajectories_table_line_edit, 2, 1, 1, 1)

        self.sonet_working_pcp_qtw = QTreeWidget(self.sonet_working_pcp_qgb)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.sonet_working_pcp_qtw.setHeaderItem(__qtreewidgetitem)
        self.sonet_working_pcp_qtw.setObjectName(u"sonet_working_pcp_qtw")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.sonet_working_pcp_qtw.sizePolicy().hasHeightForWidth())
        self.sonet_working_pcp_qtw.setSizePolicy(sizePolicy2)
        self.sonet_working_pcp_qtw.setMaximumSize(QSize(16777215, 160))

        self.gridLayout_3.addWidget(self.sonet_working_pcp_qtw, 0, 0, 1, 2)

        self.sonet__outgoing_trajectories_table_line_edit = QLineEdit(self.sonet_working_pcp_qgb)
        self.sonet__outgoing_trajectories_table_line_edit.setObjectName(u"sonet__outgoing_trajectories_table_line_edit")
        self.sonet__outgoing_trajectories_table_line_edit.setReadOnly(True)

        self.gridLayout_3.addWidget(self.sonet__outgoing_trajectories_table_line_edit, 2, 0, 1, 1)

        self.sonet_read_pcp_incoming_trajectories_table_qpb = QPushButton(self.sonet_working_pcp_qgb)
        self.sonet_read_pcp_incoming_trajectories_table_qpb.setObjectName(u"sonet_read_pcp_incoming_trajectories_table_qpb")

        self.gridLayout_3.addWidget(self.sonet_read_pcp_incoming_trajectories_table_qpb, 3, 1, 1, 1)

        self.label_2 = QLabel(self.sonet_working_pcp_qgb)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_3 = QLabel(self.sonet_working_pcp_qgb)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 1, 1, 1, 1)

        self.sonet_read_pcp_outgoing_trajectories_table_qpb = QPushButton(self.sonet_working_pcp_qgb)
        self.sonet_read_pcp_outgoing_trajectories_table_qpb.setObjectName(u"sonet_read_pcp_outgoing_trajectories_table_qpb")

        self.gridLayout_3.addWidget(self.sonet_read_pcp_outgoing_trajectories_table_qpb, 3, 0, 1, 1)


        self.gridLayout.addWidget(self.sonet_working_pcp_qgb, 8, 0, 1, 1)

        self.status_bar_HLayout = QHBoxLayout()
        self.status_bar_HLayout.setObjectName(u"status_bar_HLayout")
        self.status_bar_HLayout.setSizeConstraint(QLayout.SetFixedSize)

        self.gridLayout.addLayout(self.status_bar_HLayout, 15, 0, 1, 1)

        self.line = QFrame(sonet_pcp_manager)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 5, 0, 1, 1)

        self.sonet_ok_cancel_qpb_group = QDialogButtonBox(sonet_pcp_manager)
        self.sonet_ok_cancel_qpb_group.setObjectName(u"sonet_ok_cancel_qpb_group")
        self.sonet_ok_cancel_qpb_group.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.sonet_ok_cancel_qpb_group, 9, 0, 1, 1)

        self.sonet_read_pcp_qgb = QGroupBox(sonet_pcp_manager)
        self.sonet_read_pcp_qgb.setObjectName(u"sonet_read_pcp_qgb")
        sizePolicy1.setHeightForWidth(self.sonet_read_pcp_qgb.sizePolicy().hasHeightForWidth())
        self.sonet_read_pcp_qgb.setSizePolicy(sizePolicy1)
        self.gridLayout_4 = QGridLayout(self.sonet_read_pcp_qgb)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.sonet__outgoing_trajectories_matrix_line_edit = QLineEdit(self.sonet_read_pcp_qgb)
        self.sonet__outgoing_trajectories_matrix_line_edit.setObjectName(u"sonet__outgoing_trajectories_matrix_line_edit")
        self.sonet__outgoing_trajectories_matrix_line_edit.setMinimumSize(QSize(268, 0))
        self.sonet__outgoing_trajectories_matrix_line_edit.setReadOnly(True)

        self.gridLayout_4.addWidget(self.sonet__outgoing_trajectories_matrix_line_edit, 2, 0, 1, 2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.sonet_dvt_limit_qcb = QCheckBox(self.sonet_read_pcp_qgb)
        self.sonet_dvt_limit_qcb.setObjectName(u"sonet_dvt_limit_qcb")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.sonet_dvt_limit_qcb.sizePolicy().hasHeightForWidth())
        self.sonet_dvt_limit_qcb.setSizePolicy(sizePolicy3)

        self.horizontalLayout.addWidget(self.sonet_dvt_limit_qcb)

        self.sonet_dvt_limit_qdoublespinbox = QDoubleSpinBox(self.sonet_read_pcp_qgb)
        self.sonet_dvt_limit_qdoublespinbox.setObjectName(u"sonet_dvt_limit_qdoublespinbox")
        self.sonet_dvt_limit_qdoublespinbox.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.sonet_dvt_limit_qdoublespinbox.sizePolicy().hasHeightForWidth())
        self.sonet_dvt_limit_qdoublespinbox.setSizePolicy(sizePolicy3)

        self.horizontalLayout.addWidget(self.sonet_dvt_limit_qdoublespinbox)

        self.sonet_convert_pcp_2_table_format_qpb = QPushButton(self.sonet_read_pcp_qgb)
        self.sonet_convert_pcp_2_table_format_qpb.setObjectName(u"sonet_convert_pcp_2_table_format_qpb")

        self.horizontalLayout.addWidget(self.sonet_convert_pcp_2_table_format_qpb)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.gridLayout_4.addLayout(self.horizontalLayout, 7, 0, 1, 5)

        self.line_2 = QFrame(self.sonet_read_pcp_qgb)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line_2, 5, 0, 1, 5)

        self.sonet_read_pcp_qtw = QTreeWidget(self.sonet_read_pcp_qgb)
        __qtreewidgetitem1 = QTreeWidgetItem()
        __qtreewidgetitem1.setText(0, u"1");
        self.sonet_read_pcp_qtw.setHeaderItem(__qtreewidgetitem1)
        self.sonet_read_pcp_qtw.setObjectName(u"sonet_read_pcp_qtw")
        sizePolicy2.setHeightForWidth(self.sonet_read_pcp_qtw.sizePolicy().hasHeightForWidth())
        self.sonet_read_pcp_qtw.setSizePolicy(sizePolicy2)
        self.sonet_read_pcp_qtw.setMaximumSize(QSize(16777215, 160))

        self.gridLayout_4.addWidget(self.sonet_read_pcp_qtw, 0, 0, 1, 5)

        self.label_4 = QLabel(self.sonet_read_pcp_qgb)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_4.addWidget(self.label_4, 1, 0, 1, 2)

        self.label = QLabel(self.sonet_read_pcp_qgb)
        self.label.setObjectName(u"label")

        self.gridLayout_4.addWidget(self.label, 6, 0, 1, 1)

        self.label_5 = QLabel(self.sonet_read_pcp_qgb)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_4.addWidget(self.label_5, 1, 2, 1, 3)

        self.sonet_read_pcp_outgoing_trajectories_matrix_qpb = QPushButton(self.sonet_read_pcp_qgb)
        self.sonet_read_pcp_outgoing_trajectories_matrix_qpb.setObjectName(u"sonet_read_pcp_outgoing_trajectories_matrix_qpb")
        self.sonet_read_pcp_outgoing_trajectories_matrix_qpb.setEnabled(True)

        self.gridLayout_4.addWidget(self.sonet_read_pcp_outgoing_trajectories_matrix_qpb, 3, 0, 1, 2)

        self.sonet_read_pcp_incoming_trajectories_matrix_qpb = QPushButton(self.sonet_read_pcp_qgb)
        self.sonet_read_pcp_incoming_trajectories_matrix_qpb.setObjectName(u"sonet_read_pcp_incoming_trajectories_matrix_qpb")
        self.sonet_read_pcp_incoming_trajectories_matrix_qpb.setEnabled(True)

        self.gridLayout_4.addWidget(self.sonet_read_pcp_incoming_trajectories_matrix_qpb, 3, 2, 1, 3)

        self.sonet__incoming_trajectories_matrix_line_edit = QLineEdit(self.sonet_read_pcp_qgb)
        self.sonet__incoming_trajectories_matrix_line_edit.setObjectName(u"sonet__incoming_trajectories_matrix_line_edit")
        self.sonet__incoming_trajectories_matrix_line_edit.setMinimumSize(QSize(268, 0))
        self.sonet__incoming_trajectories_matrix_line_edit.setReadOnly(True)

        self.gridLayout_4.addWidget(self.sonet__incoming_trajectories_matrix_line_edit, 2, 2, 1, 3)


        self.gridLayout.addWidget(self.sonet_read_pcp_qgb, 3, 0, 1, 1)


        self.retranslateUi(sonet_pcp_manager)

        QMetaObject.connectSlotsByName(sonet_pcp_manager)
    # setupUi

    def retranslateUi(self, sonet_pcp_manager):
        sonet_pcp_manager.setWindowTitle(QCoreApplication.translate("sonet_pcp_manager", u"SONet PCP manager", None))
        self.sonet_working_pcp_qgb.setTitle(QCoreApplication.translate("sonet_pcp_manager", u"Set working PCP (Table format)", None))
        self.sonet_read_pcp_incoming_trajectories_table_qpb.setText(QCoreApplication.translate("sonet_pcp_manager", u"Read pkl file", None))
        self.label_2.setText(QCoreApplication.translate("sonet_pcp_manager", u"Outgoing trajectories", None))
        self.label_3.setText(QCoreApplication.translate("sonet_pcp_manager", u"Incoming trajectories", None))
        self.sonet_read_pcp_outgoing_trajectories_table_qpb.setText(QCoreApplication.translate("sonet_pcp_manager", u"Read pkl file", None))
        self.sonet_read_pcp_qgb.setTitle(QCoreApplication.translate("sonet_pcp_manager", u"Read PCP (Matrix format)", None))
        self.sonet_dvt_limit_qcb.setText(QCoreApplication.translate("sonet_pcp_manager", u"dvt limit", None))
        self.sonet_convert_pcp_2_table_format_qpb.setText(QCoreApplication.translate("sonet_pcp_manager", u"Convert PCP to table format", None))
        self.label_4.setText(QCoreApplication.translate("sonet_pcp_manager", u"Outgoing trajectories", None))
        self.label.setText(QCoreApplication.translate("sonet_pcp_manager", u"Post-processing options", None))
        self.label_5.setText(QCoreApplication.translate("sonet_pcp_manager", u"Incoming trajectories", None))
        self.sonet_read_pcp_outgoing_trajectories_matrix_qpb.setText(QCoreApplication.translate("sonet_pcp_manager", u"Read mat file", None))
        self.sonet_read_pcp_incoming_trajectories_matrix_qpb.setText(QCoreApplication.translate("sonet_pcp_manager", u"Read mat file", None))
    # retranslateUi
