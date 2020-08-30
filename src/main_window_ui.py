# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject,
                            QRect, QSize)
from PySide2.QtWidgets import *


class Ui_main_window(object):
    def setupUi(self, main_window):
        if not main_window.objectName():
            main_window.setObjectName(u"main_window")
        main_window.resize(1350, 650)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(main_window.sizePolicy().hasHeightForWidth())
        main_window.setSizePolicy(sizePolicy)
        main_window.setMinimumSize(QSize(1024, 600))
        main_window.setBaseSize(QSize(1024, 960))
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
        self.verticalLayout = QVBoxLayout(self.sonet_pcp_table_qgb)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.sonet_pcp_tabs_qtw = QTabWidget(self.sonet_pcp_table_qgb)
        self.sonet_pcp_tabs_qtw.setObjectName(u"sonet_pcp_tabs_qtw")
        self.sonet_pcp_table_transit_1 = QWidget()
        self.sonet_pcp_table_transit_1.setObjectName(u"sonet_pcp_table_transit_1")
        self.verticalLayout_4 = QVBoxLayout(self.sonet_pcp_table_transit_1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.sonet_pcp_table_qtv_outgoing = QTableView(self.sonet_pcp_table_transit_1)
        self.sonet_pcp_table_qtv_outgoing.setObjectName(u"sonet_pcp_table_qtv_outgoing")
        self.sonet_pcp_table_qtv_outgoing.setFrameShadow(QFrame.Sunken)
        self.sonet_pcp_table_qtv_outgoing.setLineWidth(1)
        self.sonet_pcp_table_qtv_outgoing.setMidLineWidth(1)

        self.verticalLayout_4.addWidget(self.sonet_pcp_table_qtv_outgoing)

        self.sonet_pcp_tabs_qtw.addTab(self.sonet_pcp_table_transit_1, "")
        self.sonet_pcp_table_transit_2 = QWidget()
        self.sonet_pcp_table_transit_2.setObjectName(u"sonet_pcp_table_transit_2")
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

        self.verticalLayout_3.addWidget(self.sonet_pcp_table_qtv_incoming)

        self.sonet_pcp_tabs_qtw.addTab(self.sonet_pcp_table_transit_2, "")

        self.verticalLayout.addWidget(self.sonet_pcp_tabs_qtw)


        self.gridLayout.addWidget(self.sonet_pcp_table_qgb, 0, 0, 1, 1)

        self.sonet_mission_tree_qgb = QGroupBox(self.centralwidget)
        self.sonet_mission_tree_qgb.setObjectName(u"sonet_mission_tree_qgb")
        sizePolicy.setHeightForWidth(self.sonet_mission_tree_qgb.sizePolicy().hasHeightForWidth())
        self.sonet_mission_tree_qgb.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.sonet_mission_tree_qgb)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.sonet_mission_tree_qlv = QListView(self.sonet_mission_tree_qgb)
        self.sonet_mission_tree_qlv.setObjectName(u"sonet_mission_tree_qlv")

        self.verticalLayout_2.addWidget(self.sonet_mission_tree_qlv)


        self.gridLayout.addWidget(self.sonet_mission_tree_qgb, 0, 1, 1, 1)

        self.sonet_add_spacecraft_qpb = QPushButton(self.centralwidget)
        self.sonet_add_spacecraft_qpb.setObjectName(u"sonet_add_spacecraft_qpb")

        self.gridLayout.addWidget(self.sonet_add_spacecraft_qpb, 1, 1, 1, 1)

        self.sonet_pcp_filter_qpb = QPushButton(self.centralwidget)
        self.sonet_pcp_filter_qpb.setObjectName(u"sonet_pcp_filter_qpb")

        self.gridLayout.addWidget(self.sonet_pcp_filter_qpb, 1, 0, 1, 1)

        main_window.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(main_window)
        self.statusbar.setObjectName(u"statusbar")
        main_window.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(main_window)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1350, 22))
        self.file = QMenu(self.menubar)
        self.file.setObjectName(u"file")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        main_window.setMenuBar(self.menubar)

        self.menubar.addAction(self.file.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.file.addAction(self.exit)
        self.file.addSeparator()

        self.retranslateUi(main_window)

        self.sonet_pcp_tabs_qtw.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(main_window)
    # setupUi

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(QCoreApplication.translate("main_window", u"SONET Mars Mission Timeline", None))
        self.exit.setText(QCoreApplication.translate("main_window", u"&Exit", None))
        self.open_pcp_filter.setText(QCoreApplication.translate("main_window", u"Apply filter to PCP table", None))
        self.actionHelp.setText(QCoreApplication.translate("main_window", u"Help", None))
        self.sonet_pcp_table_qgb.setTitle(QCoreApplication.translate("main_window", u"PCP table", None))
        self.sonet_pcp_tabs_qtw.setTabText(self.sonet_pcp_tabs_qtw.indexOf(self.sonet_pcp_table_transit_1), QCoreApplication.translate("main_window", u"Earth - Mars", None))
        self.sonet_pcp_tabs_qtw.setTabText(self.sonet_pcp_tabs_qtw.indexOf(self.sonet_pcp_table_transit_2), QCoreApplication.translate("main_window", u"Mars - Earth ", None))
        self.sonet_mission_tree_qgb.setTitle(QCoreApplication.translate("main_window", u"Mission tree", None))
        self.sonet_add_spacecraft_qpb.setText(QCoreApplication.translate("main_window", u"Add spacecraft", None))
        self.sonet_pcp_filter_qpb.setText(QCoreApplication.translate("main_window", u"Apply filter", None))
        self.file.setTitle(QCoreApplication.translate("main_window", u"&File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("main_window", u"Edit", None))
        self.menuHelp.setTitle(QCoreApplication.translate("main_window", u"Help", None))
    # retranslateUi

