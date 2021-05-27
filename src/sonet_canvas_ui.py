# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sonet_canvas.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_sonet_canvas(object):
    def setupUi(self, sonet_canvas):
        if not sonet_canvas.objectName():
            sonet_canvas.setObjectName(u"sonet_canvas")
        sonet_canvas.resize(530, 683)
        sonet_canvas.setBaseSize(QSize(0, 0))
        self.verticalLayout_2 = QVBoxLayout(sonet_canvas)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.dockw_sc_info = QDockWidget(sonet_canvas)
        self.dockw_sc_info.setObjectName(u"dockw_sc_info")
        self.dockw_sc_info.setMinimumSize(QSize(119, 244))
        self.dockw_sc_info.setMaximumSize(QSize(524287, 524287))
        self.dockw_sc_info.setBaseSize(QSize(0, 0))
        self.dockw_sc_info_contentsw = QWidget()
        self.dockw_sc_info_contentsw.setObjectName(u"dockw_sc_info_contentsw")
        self.verticalLayout_4 = QVBoxLayout(self.dockw_sc_info_contentsw)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.treeW_sc_info_filter = QTreeWidget(self.dockw_sc_info_contentsw)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.treeW_sc_info_filter.setHeaderItem(__qtreewidgetitem)
        self.treeW_sc_info_filter.setObjectName(u"treeW_sc_info_filter")

        self.verticalLayout_4.addWidget(self.treeW_sc_info_filter)

        self.dockw_sc_info.setWidget(self.dockw_sc_info_contentsw)

        self.verticalLayout_2.addWidget(self.dockw_sc_info)

        self.dockw_trajectories_filter = QDockWidget(sonet_canvas)
        self.dockw_trajectories_filter.setObjectName(u"dockw_trajectories_filter")
        self.dockw_trajectories_filter.setMinimumSize(QSize(95, 117))
        self.dockw_trajectories_filter.setMaximumSize(QSize(524287, 524287))
        self.dockw_trajectories_filter.setBaseSize(QSize(0, 0))
        self.dockw_trajectories_contentsw = QWidget()
        self.dockw_trajectories_contentsw.setObjectName(u"dockw_trajectories_contentsw")
        self.verticalLayout_3 = QVBoxLayout(self.dockw_trajectories_contentsw)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.treeW_trajectories_filter = QTreeWidget(self.dockw_trajectories_contentsw)
        __qtreewidgetitem1 = QTreeWidgetItem()
        __qtreewidgetitem1.setText(0, u"1");
        self.treeW_trajectories_filter.setHeaderItem(__qtreewidgetitem1)
        self.treeW_trajectories_filter.setObjectName(u"treeW_trajectories_filter")

        self.verticalLayout_3.addWidget(self.treeW_trajectories_filter)

        self.dockw_trajectories_filter.setWidget(self.dockw_trajectories_contentsw)

        self.verticalLayout_2.addWidget(self.dockw_trajectories_filter)

        self.dockw_active_trips = QDockWidget(sonet_canvas)
        self.dockw_active_trips.setObjectName(u"dockw_active_trips")
        self.dockw_active_trips.setMaximumSize(QSize(524287, 150))
        self.dockw_active_trips.setAllowedAreas(Qt.AllDockWidgetAreas)
        self.dockw_active_trips_contentsw = QWidget()
        self.dockw_active_trips_contentsw.setObjectName(u"dockw_active_trips_contentsw")
        self.verticalLayout = QVBoxLayout(self.dockw_active_trips_contentsw)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.treeW_active_trips = QTreeWidget(self.dockw_active_trips_contentsw)
        __qtreewidgetitem2 = QTreeWidgetItem()
        __qtreewidgetitem2.setText(0, u"1");
        self.treeW_active_trips.setHeaderItem(__qtreewidgetitem2)
        self.treeW_active_trips.setObjectName(u"treeW_active_trips")
        self.treeW_active_trips.setMaximumSize(QSize(16777215, 150))

        self.verticalLayout.addWidget(self.treeW_active_trips)

        self.dockw_active_trips.setWidget(self.dockw_active_trips_contentsw)

        self.verticalLayout_2.addWidget(self.dockw_active_trips)


        self.retranslateUi(sonet_canvas)

        QMetaObject.connectSlotsByName(sonet_canvas)
    # setupUi

    def retranslateUi(self, sonet_canvas):
        sonet_canvas.setWindowTitle(QCoreApplication.translate("sonet_canvas", u"SONet Mars Mission Viewer", None))
        self.dockw_sc_info.setWindowTitle(QCoreApplication.translate("sonet_canvas", u"S/C Info", None))
        self.dockw_trajectories_filter.setWindowTitle(QCoreApplication.translate("sonet_canvas", u"Trajectories Filter", None))
        self.dockw_active_trips.setWindowTitle(QCoreApplication.translate("sonet_canvas", u"Active Trips", None))
    # retranslateUi

