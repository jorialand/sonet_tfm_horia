# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sonet_main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_main_window(object):
    def setupUi(self, main_window):
        if not main_window.objectName():
            main_window.setObjectName(u"main_window")
        main_window.resize(1100, 800)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(main_window.sizePolicy().hasHeightForWidth())
        main_window.setSizePolicy(sizePolicy)
        main_window.setMinimumSize(QSize(900, 600))
        main_window.setBaseSize(QSize(1024, 960))
        main_window.setWindowOpacity(1.000000000000000)
        main_window.setTabShape(QTabWidget.Rounded)
        main_window.setUnifiedTitleAndToolBarOnMac(True)
        self.exit = QAction(main_window)
        self.exit.setObjectName(u"exit")
        self.open_pcp_filter = QAction(main_window)
        self.open_pcp_filter.setObjectName(u"open_pcp_filter")
        self.actionHelp = QAction(main_window)
        self.actionHelp.setObjectName(u"actionHelp")
        self.centralwidget = QWidget(main_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.sonet_pcp_table_qgb = QGroupBox(self.centralwidget)
        self.sonet_pcp_table_qgb.setObjectName(u"sonet_pcp_table_qgb")
        self.sonet_pcp_table_qgb.setMaximumSize(QSize(16777215, 16777215))
        self.sonet_pcp_table_qgb.setFlat(True)
        self.verticalLayout = QVBoxLayout(self.sonet_pcp_table_qgb)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.sonet_pcp_tabs_qtw = QTabWidget(self.sonet_pcp_table_qgb)
        self.sonet_pcp_tabs_qtw.setObjectName(u"sonet_pcp_tabs_qtw")
        self.sonet_pcp_tabs_qtw.setEnabled(True)
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(236, 236, 236, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(245, 245, 245, 0))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush2)
        brush3 = QBrush(QColor(191, 191, 191, 0))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush3)
        brush4 = QBrush(QColor(169, 169, 169, 0))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush5 = QBrush(QColor(255, 255, 255, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
        brush6 = QBrush(QColor(0, 0, 0, 0))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.NoRole, brush6)
        brush7 = QBrush(QColor(255, 255, 255, 0))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.NoRole, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.NoRole, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.sonet_pcp_tabs_qtw.setPalette(palette)
        self.sonet_pcp_tabs_qtw.setCursor(QCursor(Qt.PointingHandCursor))
        self.sonet_pcp_tabs_qtw.setAutoFillBackground(False)
        self.sonet_pcp_tabs_qtw.setTabPosition(QTabWidget.North)
        self.sonet_pcp_tabs_qtw.setTabShape(QTabWidget.Rounded)
        self.sonet_pcp_tabs_qtw.setElideMode(Qt.ElideLeft)
        self.sonet_pcp_table_transit_1 = QWidget()
        self.sonet_pcp_table_transit_1.setObjectName(u"sonet_pcp_table_transit_1")
        self.sonet_pcp_table_transit_1.setAutoFillBackground(False)
        self.verticalLayout_4 = QVBoxLayout(self.sonet_pcp_table_transit_1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.sonet_pcp_table_qtv_outgoing = QTableView(self.sonet_pcp_table_transit_1)
        self.sonet_pcp_table_qtv_outgoing.setObjectName(u"sonet_pcp_table_qtv_outgoing")
        self.sonet_pcp_table_qtv_outgoing.setFrameShadow(QFrame.Sunken)
        self.sonet_pcp_table_qtv_outgoing.setLineWidth(1)
        self.sonet_pcp_table_qtv_outgoing.setMidLineWidth(1)
        self.sonet_pcp_table_qtv_outgoing.setSelectionMode(QAbstractItemView.SingleSelection)
        self.sonet_pcp_table_qtv_outgoing.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.sonet_pcp_table_qtv_outgoing.setSortingEnabled(True)
        self.sonet_pcp_table_qtv_outgoing.horizontalHeader().setProperty("showSortIndicator", True)
        self.sonet_pcp_table_qtv_outgoing.horizontalHeader().setStretchLastSection(True)
        self.sonet_pcp_table_qtv_outgoing.verticalHeader().setProperty("showSortIndicator", False)
        self.sonet_pcp_table_qtv_outgoing.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_4.addWidget(self.sonet_pcp_table_qtv_outgoing)

        self.sonet_pcp_tabs_qtw.addTab(self.sonet_pcp_table_transit_1, "")
        self.sonet_pcp_table_transit_2 = QWidget()
        self.sonet_pcp_table_transit_2.setObjectName(u"sonet_pcp_table_transit_2")
        self.sonet_pcp_table_transit_2.setAutoFillBackground(False)
        self.verticalLayout_3 = QVBoxLayout(self.sonet_pcp_table_transit_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.sonet_pcp_table_qtv_incoming = QTableView(self.sonet_pcp_table_transit_2)
        self.sonet_pcp_table_qtv_incoming.setObjectName(u"sonet_pcp_table_qtv_incoming")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.sonet_pcp_table_qtv_incoming.sizePolicy().hasHeightForWidth())
        self.sonet_pcp_table_qtv_incoming.setSizePolicy(sizePolicy1)
        self.sonet_pcp_table_qtv_incoming.setFrameShadow(QFrame.Sunken)
        self.sonet_pcp_table_qtv_incoming.setLineWidth(1)
        self.sonet_pcp_table_qtv_incoming.setMidLineWidth(1)
        self.sonet_pcp_table_qtv_incoming.setSelectionMode(QAbstractItemView.SingleSelection)
        self.sonet_pcp_table_qtv_incoming.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.sonet_pcp_table_qtv_incoming.setSortingEnabled(True)
        self.sonet_pcp_table_qtv_incoming.horizontalHeader().setProperty("showSortIndicator", True)
        self.sonet_pcp_table_qtv_incoming.horizontalHeader().setStretchLastSection(True)
        self.sonet_pcp_table_qtv_incoming.verticalHeader().setProperty("showSortIndicator", False)
        self.sonet_pcp_table_qtv_incoming.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_3.addWidget(self.sonet_pcp_table_qtv_incoming)

        self.sonet_pcp_tabs_qtw.addTab(self.sonet_pcp_table_transit_2, "")

        self.verticalLayout.addWidget(self.sonet_pcp_tabs_qtw)

        self.sonet_label_rows_filtered_visible = QLabel(self.sonet_pcp_table_qgb)
        self.sonet_label_rows_filtered_visible.setObjectName(u"sonet_label_rows_filtered_visible")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.sonet_label_rows_filtered_visible.sizePolicy().hasHeightForWidth())
        self.sonet_label_rows_filtered_visible.setSizePolicy(sizePolicy2)

        self.verticalLayout.addWidget(self.sonet_label_rows_filtered_visible)

        self.sonet_label_selected_trajectory = QLabel(self.sonet_pcp_table_qgb)
        self.sonet_label_selected_trajectory.setObjectName(u"sonet_label_selected_trajectory")

        self.verticalLayout.addWidget(self.sonet_label_selected_trajectory)

        self.sonet_trajectory_selection_qprogrbar = QProgressBar(self.sonet_pcp_table_qgb)
        self.sonet_trajectory_selection_qprogrbar.setObjectName(u"sonet_trajectory_selection_qprogrbar")
        self.sonet_trajectory_selection_qprogrbar.setValue(0)
        self.sonet_trajectory_selection_qprogrbar.setTextVisible(False)

        self.verticalLayout.addWidget(self.sonet_trajectory_selection_qprogrbar)


        self.gridLayout.addWidget(self.sonet_pcp_table_qgb, 0, 0, 1, 1)

        self.sonet_mission_tree_qgb = QGroupBox(self.centralwidget)
        self.sonet_mission_tree_qgb.setObjectName(u"sonet_mission_tree_qgb")
        sizePolicy.setHeightForWidth(self.sonet_mission_tree_qgb.sizePolicy().hasHeightForWidth())
        self.sonet_mission_tree_qgb.setSizePolicy(sizePolicy)
        self.sonet_mission_tree_qgb.setMinimumSize(QSize(0, 0))
        self.sonet_mission_tree_qgb.setMaximumSize(QSize(260, 16777215))
        self.sonet_mission_tree_qgb.setBaseSize(QSize(0, 0))
        self.sonet_mission_tree_qgb.setFlat(True)
        self.verticalLayout_2 = QVBoxLayout(self.sonet_mission_tree_qgb)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.sonet_mission_tree_qlv = QListView(self.sonet_mission_tree_qgb)
        self.sonet_mission_tree_qlv.setObjectName(u"sonet_mission_tree_qlv")
        self.sonet_mission_tree_qlv.setMaximumSize(QSize(16777215, 200))
        self.sonet_mission_tree_qlv.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.sonet_mission_tree_qlv.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.verticalLayout_2.addWidget(self.sonet_mission_tree_qlv)

        self.toolBox = QToolBox(self.sonet_mission_tree_qgb)
        self.toolBox.setObjectName(u"toolBox")
        self.page_mission = QWidget()
        self.page_mission.setObjectName(u"page_mission")
        self.page_mission.setGeometry(QRect(0, 0, 230, 345))
        self.verticalLayout_8 = QVBoxLayout(self.page_mission)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.sonet_load_mission_qpb = QPushButton(self.page_mission)
        self.sonet_load_mission_qpb.setObjectName(u"sonet_load_mission_qpb")
        self.sonet_load_mission_qpb.setEnabled(False)
        self.sonet_load_mission_qpb.setMaximumSize(QSize(170, 16777215))
        self.sonet_load_mission_qpb.setFlat(False)

        self.verticalLayout_11.addWidget(self.sonet_load_mission_qpb)

        self.sonet_save_mission_qpb = QPushButton(self.page_mission)
        self.sonet_save_mission_qpb.setObjectName(u"sonet_save_mission_qpb")
        self.sonet_save_mission_qpb.setEnabled(False)
        self.sonet_save_mission_qpb.setMaximumSize(QSize(170, 16777215))

        self.verticalLayout_11.addWidget(self.sonet_save_mission_qpb)

        self.sonet_view_mission_qpb = QPushButton(self.page_mission)
        self.sonet_view_mission_qpb.setObjectName(u"sonet_view_mission_qpb")
        self.sonet_view_mission_qpb.setMinimumSize(QSize(0, 0))
        self.sonet_view_mission_qpb.setMaximumSize(QSize(170, 16777215))

        self.verticalLayout_11.addWidget(self.sonet_view_mission_qpb)


        self.verticalLayout_8.addLayout(self.verticalLayout_11)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer)

        self.toolBox.addItem(self.page_mission, u"Mission")
        self.page_spacecraft = QWidget()
        self.page_spacecraft.setObjectName(u"page_spacecraft")
        self.page_spacecraft.setGeometry(QRect(0, 0, 230, 345))
        self.verticalLayout_7 = QVBoxLayout(self.page_spacecraft)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.sonet_sc_name_le = QLineEdit(self.page_spacecraft)
        self.sonet_sc_name_le.setObjectName(u"sonet_sc_name_le")

        self.verticalLayout_7.addWidget(self.sonet_sc_name_le)

        self.sonet_spacecraft_type_qhbox = QHBoxLayout()
        self.sonet_spacecraft_type_qhbox.setObjectName(u"sonet_spacecraft_type_qhbox")
        self.sonet_spacecraft_type_qcmb = QComboBox(self.page_spacecraft)
        self.sonet_spacecraft_type_qcmb.addItem("")
        self.sonet_spacecraft_type_qcmb.addItem("")
        self.sonet_spacecraft_type_qcmb.setObjectName(u"sonet_spacecraft_type_qcmb")

        self.sonet_spacecraft_type_qhbox.addWidget(self.sonet_spacecraft_type_qcmb)

        self.sonet_spacecraft_type_has_return_trajectory_qcmb = QComboBox(self.page_spacecraft)
        self.sonet_spacecraft_type_has_return_trajectory_qcmb.addItem("")
        self.sonet_spacecraft_type_has_return_trajectory_qcmb.addItem("")
        self.sonet_spacecraft_type_has_return_trajectory_qcmb.setObjectName(u"sonet_spacecraft_type_has_return_trajectory_qcmb")

        self.sonet_spacecraft_type_qhbox.addWidget(self.sonet_spacecraft_type_has_return_trajectory_qcmb)


        self.verticalLayout_7.addLayout(self.sonet_spacecraft_type_qhbox)

        self.sonet_add_rm_sc_qhbox = QHBoxLayout()
        self.sonet_add_rm_sc_qhbox.setObjectName(u"sonet_add_rm_sc_qhbox")
        self.sonet_add_spacecraft_qpb = QPushButton(self.page_spacecraft)
        self.sonet_add_spacecraft_qpb.setObjectName(u"sonet_add_spacecraft_qpb")
        self.sonet_add_spacecraft_qpb.setMaximumSize(QSize(170, 16777215))

        self.sonet_add_rm_sc_qhbox.addWidget(self.sonet_add_spacecraft_qpb)

        self.sonet_remove_spacecraft_qpb = QPushButton(self.page_spacecraft)
        self.sonet_remove_spacecraft_qpb.setObjectName(u"sonet_remove_spacecraft_qpb")
        self.sonet_remove_spacecraft_qpb.setMaximumSize(QSize(170, 16777215))

        self.sonet_add_rm_sc_qhbox.addWidget(self.sonet_remove_spacecraft_qpb)


        self.verticalLayout_7.addLayout(self.sonet_add_rm_sc_qhbox)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)

        self.toolBox.addItem(self.page_spacecraft, u"S/C")
        self.page_commands = QWidget()
        self.page_commands.setObjectName(u"page_commands")
        self.page_commands.setGeometry(QRect(0, 0, 230, 345))
        self.verticalLayout_6 = QVBoxLayout(self.page_commands)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.sonet_pcp_filter_qpb = QPushButton(self.page_commands)
        self.sonet_pcp_filter_qpb.setObjectName(u"sonet_pcp_filter_qpb")
        self.sonet_pcp_filter_qpb.setMaximumSize(QSize(170, 16777215))

        self.verticalLayout_10.addWidget(self.sonet_pcp_filter_qpb)

        self.sonet_open_matlab_pcp_viewer = QPushButton(self.page_commands)
        self.sonet_open_matlab_pcp_viewer.setObjectName(u"sonet_open_matlab_pcp_viewer")
        self.sonet_open_matlab_pcp_viewer.setMaximumSize(QSize(170, 16777215))

        self.verticalLayout_10.addWidget(self.sonet_open_matlab_pcp_viewer)


        self.verticalLayout_6.addLayout(self.verticalLayout_10)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.sonet_select_trajectory_qpb = QPushButton(self.page_commands)
        self.sonet_select_trajectory_qpb.setObjectName(u"sonet_select_trajectory_qpb")
        self.sonet_select_trajectory_qpb.setMaximumSize(QSize(170, 16777215))

        self.verticalLayout_9.addWidget(self.sonet_select_trajectory_qpb)

        self.sonet_unselect_trajectory_qpb = QPushButton(self.page_commands)
        self.sonet_unselect_trajectory_qpb.setObjectName(u"sonet_unselect_trajectory_qpb")
        self.sonet_unselect_trajectory_qpb.setMaximumSize(QSize(170, 16777215))

        self.verticalLayout_9.addWidget(self.sonet_unselect_trajectory_qpb)


        self.verticalLayout_6.addLayout(self.verticalLayout_9)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_3)

        self.toolBox.addItem(self.page_commands, u"Actions")
        self.page_others = QWidget()
        self.page_others.setObjectName(u"page_others")
        self.page_others.setGeometry(QRect(0, 0, 230, 345))
        self.verticalLayout_5 = QVBoxLayout(self.page_others)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.sonet_pcp_generator_qpb = QPushButton(self.page_others)
        self.sonet_pcp_generator_qpb.setObjectName(u"sonet_pcp_generator_qpb")

        self.verticalLayout_5.addWidget(self.sonet_pcp_generator_qpb)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_4)

        self.toolBox.addItem(self.page_others, u"PCP Manager")

        self.verticalLayout_2.addWidget(self.toolBox)


        self.gridLayout.addWidget(self.sonet_mission_tree_qgb, 0, 1, 1, 1)

        main_window.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(main_window)
        self.statusbar.setObjectName(u"statusbar")
        main_window.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(main_window)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1100, 22))
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        main_window.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(main_window)

        self.sonet_pcp_tabs_qtw.setCurrentIndex(0)
        self.toolBox.setCurrentIndex(1)
        self.sonet_spacecraft_type_qcmb.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(main_window)
    # setupUi

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(QCoreApplication.translate("main_window", u"SONet Mars Mission Flight Sequence Planner", None))
        self.exit.setText(QCoreApplication.translate("main_window", u"&Exit", None))
        self.open_pcp_filter.setText(QCoreApplication.translate("main_window", u"Apply filter to PCP table", None))
        self.actionHelp.setText(QCoreApplication.translate("main_window", u"Help", None))
        self.sonet_pcp_table_qgb.setTitle(QCoreApplication.translate("main_window", u"PCP Table", None))
        self.sonet_pcp_tabs_qtw.setTabText(self.sonet_pcp_tabs_qtw.indexOf(self.sonet_pcp_table_transit_1), QCoreApplication.translate("main_window", u"Earth - Mars", None))
        self.sonet_pcp_tabs_qtw.setTabText(self.sonet_pcp_tabs_qtw.indexOf(self.sonet_pcp_table_transit_2), QCoreApplication.translate("main_window", u"Mars - Earth ", None))
        self.sonet_label_rows_filtered_visible.setText("")
        self.sonet_label_selected_trajectory.setText("")
        self.sonet_mission_tree_qgb.setTitle(QCoreApplication.translate("main_window", u"S/C List", None))
#if QT_CONFIG(tooltip)
        self.sonet_load_mission_qpb.setToolTip(QCoreApplication.translate("main_window", u"Create new mission", None))
#endif // QT_CONFIG(tooltip)
        self.sonet_load_mission_qpb.setText(QCoreApplication.translate("main_window", u"Load mission", None))
#if QT_CONFIG(tooltip)
        self.sonet_save_mission_qpb.setToolTip(QCoreApplication.translate("main_window", u"Remove mission", None))
#endif // QT_CONFIG(tooltip)
        self.sonet_save_mission_qpb.setText(QCoreApplication.translate("main_window", u"Save mission", None))
        self.sonet_view_mission_qpb.setText(QCoreApplication.translate("main_window", u"View mission", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_mission), QCoreApplication.translate("main_window", u"Mission", None))
#if QT_CONFIG(tooltip)
        self.sonet_sc_name_le.setToolTip(QCoreApplication.translate("main_window", u"Enter new s/c name", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.sonet_sc_name_le.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.sonet_sc_name_le.setPlaceholderText(QCoreApplication.translate("main_window", u"Enter new s/c name", None))
        self.sonet_spacecraft_type_qcmb.setItemText(0, QCoreApplication.translate("main_window", u"Crewed", None))
        self.sonet_spacecraft_type_qcmb.setItemText(1, QCoreApplication.translate("main_window", u"Cargo", None))

#if QT_CONFIG(tooltip)
        self.sonet_spacecraft_type_qcmb.setToolTip(QCoreApplication.translate("main_window", u"Select payload", None))
#endif // QT_CONFIG(tooltip)
        self.sonet_spacecraft_type_has_return_trajectory_qcmb.setItemText(0, QCoreApplication.translate("main_window", u"One way", None))
        self.sonet_spacecraft_type_has_return_trajectory_qcmb.setItemText(1, QCoreApplication.translate("main_window", u"Two way", None))

#if QT_CONFIG(tooltip)
        self.sonet_spacecraft_type_has_return_trajectory_qcmb.setToolTip(QCoreApplication.translate("main_window", u"Select type of trip", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.sonet_add_spacecraft_qpb.setToolTip(QCoreApplication.translate("main_window", u"Create new s/c", None))
#endif // QT_CONFIG(tooltip)
        self.sonet_add_spacecraft_qpb.setText(QCoreApplication.translate("main_window", u"Add s/c", None))
#if QT_CONFIG(tooltip)
        self.sonet_remove_spacecraft_qpb.setToolTip(QCoreApplication.translate("main_window", u"Remove s/c", None))
#endif // QT_CONFIG(tooltip)
        self.sonet_remove_spacecraft_qpb.setText(QCoreApplication.translate("main_window", u"Remove s/c", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_spacecraft), QCoreApplication.translate("main_window", u"S/C", None))
#if QT_CONFIG(tooltip)
        self.sonet_pcp_filter_qpb.setToolTip(QCoreApplication.translate("main_window", u"Apply filter", None))
#endif // QT_CONFIG(tooltip)
        self.sonet_pcp_filter_qpb.setText(QCoreApplication.translate("main_window", u"Edit s/c filter", None))
#if QT_CONFIG(tooltip)
        self.sonet_open_matlab_pcp_viewer.setToolTip(QCoreApplication.translate("main_window", u"Create new s/c", None))
#endif // QT_CONFIG(tooltip)
        self.sonet_open_matlab_pcp_viewer.setText(QCoreApplication.translate("main_window", u"View s/c trajectories", None))
#if QT_CONFIG(tooltip)
        self.sonet_select_trajectory_qpb.setToolTip(QCoreApplication.translate("main_window", u"Select trajectory", None))
#endif // QT_CONFIG(tooltip)
        self.sonet_select_trajectory_qpb.setText(QCoreApplication.translate("main_window", u"Select trajectory", None))
#if QT_CONFIG(tooltip)
        self.sonet_unselect_trajectory_qpb.setToolTip(QCoreApplication.translate("main_window", u"Select trajectory", None))
#endif // QT_CONFIG(tooltip)
        self.sonet_unselect_trajectory_qpb.setText(QCoreApplication.translate("main_window", u"Unselect trajectory", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_commands), QCoreApplication.translate("main_window", u"Actions", None))
#if QT_CONFIG(tooltip)
        self.sonet_pcp_generator_qpb.setToolTip(QCoreApplication.translate("main_window", u"Remove s/c", None))
#endif // QT_CONFIG(tooltip)
        self.sonet_pcp_generator_qpb.setText(QCoreApplication.translate("main_window", u"PCP manager", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_others), QCoreApplication.translate("main_window", u"PCP Manager", None))
        self.menuHelp.setTitle(QCoreApplication.translate("main_window", u"Help", None))
    # retranslateUi

