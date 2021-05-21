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
        sonet_canvas.resize(604, 611)
        self.formLayout = QFormLayout(sonet_canvas)
        self.formLayout.setObjectName(u"formLayout")
        self.dockw_sc = QDockWidget(sonet_canvas)
        self.dockw_sc.setObjectName(u"dockw_sc")
        self.dockw_sc_contentsw = QWidget()
        self.dockw_sc_contentsw.setObjectName(u"dockw_sc_contentsw")
        self.verticalLayout_2 = QVBoxLayout(self.dockw_sc_contentsw)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.treeW_sc = QTreeWidget(self.dockw_sc_contentsw)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.treeW_sc.setHeaderItem(__qtreewidgetitem)
        self.treeW_sc.setObjectName(u"treeW_sc")

        self.verticalLayout_2.addWidget(self.treeW_sc)

        self.dockw_sc.setWidget(self.dockw_sc_contentsw)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.dockw_sc)

        self.dockw_trajectories_filter = QDockWidget(sonet_canvas)
        self.dockw_trajectories_filter.setObjectName(u"dockw_trajectories_filter")
        self.dockw_trajectories_filter.setMinimumSize(QSize(95, 117))
        self.dockw_trajectories_filter.setMaximumSize(QSize(524287, 524287))
        self.dockw_trajectories_filter.setBaseSize(QSize(0, 960))
        self.dockw_trajectories_filter_contentsw = QWidget()
        self.dockw_trajectories_filter_contentsw.setObjectName(u"dockw_trajectories_filter_contentsw")
        self.verticalLayout_3 = QVBoxLayout(self.dockw_trajectories_filter_contentsw)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.treeW_trajectories_filter = QTreeWidget(self.dockw_trajectories_filter_contentsw)
        __qtreewidgetitem1 = QTreeWidgetItem()
        __qtreewidgetitem1.setText(0, u"1");
        self.treeW_trajectories_filter.setHeaderItem(__qtreewidgetitem1)
        self.treeW_trajectories_filter.setObjectName(u"treeW_trajectories_filter")

        self.verticalLayout_3.addWidget(self.treeW_trajectories_filter)

        self.dockw_trajectories_filter.setWidget(self.dockw_trajectories_filter_contentsw)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.dockw_trajectories_filter)

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

        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.dockw_active_trips)


        self.retranslateUi(sonet_canvas)

        QMetaObject.connectSlotsByName(sonet_canvas)
    # setupUi

    def retranslateUi(self, sonet_canvas):
        sonet_canvas.setWindowTitle(QCoreApplication.translate("sonet_canvas", u"sonet_canvas", None))
        self.dockw_sc.setWindowTitle(QCoreApplication.translate("sonet_canvas", u"s/c info", None))
        self.dockw_trajectories_filter.setWindowTitle(QCoreApplication.translate("sonet_canvas", u"Trajectories filter", None))
        self.dockw_active_trips.setWindowTitle(QCoreApplication.translate("sonet_canvas", u"Active trips", None))
    # retranslateUi

