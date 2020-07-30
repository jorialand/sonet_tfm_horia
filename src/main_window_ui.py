# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject,
                            QRect)
from PySide2.QtWidgets import *


class Ui_main_window(object):
    def setupUi(self, main_window):
        if not main_window.objectName():
            main_window.setObjectName(u"main_window")
        main_window.resize(800, 600)
        main_window.setUnifiedTitleAndToolBarOnMac(True)
        self.exit = QAction(main_window)
        self.exit.setObjectName(u"exit")
        self.open_pcp_filter = QAction(main_window)
        self.open_pcp_filter.setObjectName(u"open_pcp_filter")
        self.centralwidget = QWidget(main_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pcp_table = QTableView(self.groupBox)
        self.pcp_table.setObjectName(u"pcp_table")
        self.pcp_table.setFrameShadow(QFrame.Sunken)
        self.pcp_table.setLineWidth(1)
        self.pcp_table.setMidLineWidth(1)

        self.verticalLayout_2.addWidget(self.pcp_table)

        self.sonet_pcp_filter_pb_qt = QPushButton(self.groupBox)
        self.sonet_pcp_filter_pb_qt.setObjectName(u"sonet_pcp_filter_pb_qt")

        self.verticalLayout_2.addWidget(self.sonet_pcp_filter_pb_qt)


        self.verticalLayout.addWidget(self.groupBox)

        main_window.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(main_window)
        self.statusbar.setObjectName(u"statusbar")
        main_window.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(main_window)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.file = QMenu(self.menubar)
        self.file.setObjectName(u"file")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menugwg = QMenu(self.menubar)
        self.menugwg.setObjectName(u"menugwg")
        self.menusadasd = QMenu(self.menubar)
        self.menusadasd.setObjectName(u"menusadasd")
        self.menudsd = QMenu(self.menubar)
        self.menudsd.setObjectName(u"menudsd")
        self.menuds = QMenu(self.menubar)
        self.menuds.setObjectName(u"menuds")
        main_window.setMenuBar(self.menubar)

        self.menubar.addAction(self.file.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menugwg.menuAction())
        self.menubar.addAction(self.menusadasd.menuAction())
        self.menubar.addAction(self.menudsd.menuAction())
        self.menubar.addAction(self.menuds.menuAction())
        self.file.addAction(self.exit)
        self.file.addSeparator()

        self.retranslateUi(main_window)

        QMetaObject.connectSlotsByName(main_window)
    # setupUi

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(QCoreApplication.translate("main_window", u"SONET Mars Mission Timeline", None))
        self.exit.setText(QCoreApplication.translate("main_window", u"&Exit", None))
        self.open_pcp_filter.setText(QCoreApplication.translate("main_window", u"Apply filter to PCP table", None))
        self.groupBox.setTitle(QCoreApplication.translate("main_window", u"PCP table", None))
        self.sonet_pcp_filter_pb_qt.setText(QCoreApplication.translate("main_window", u"Apply filter", None))
        self.file.setTitle(QCoreApplication.translate("main_window", u"&File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("main_window", u"Edit", None))
        self.menugwg.setTitle(QCoreApplication.translate("main_window", u"gwg+", None))
        self.menusadasd.setTitle(QCoreApplication.translate("main_window", u"sadasd", None))
        self.menudsd.setTitle(QCoreApplication.translate("main_window", u"dsd", None))
        self.menuds.setTitle(QCoreApplication.translate("main_window", u"ds\u00e7", None))
    # retranslateUi

