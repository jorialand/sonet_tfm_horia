# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sonet_pcp_filter_qt.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_sonet_pcp_filter(object):
    def setupUi(self, sonet_pcp_filter):
        if not sonet_pcp_filter.objectName():
            sonet_pcp_filter.setObjectName(u"sonet_pcp_filter")
        sonet_pcp_filter.setEnabled(True)
        sonet_pcp_filter.resize(600, 721)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(sonet_pcp_filter.sizePolicy().hasHeightForWidth())
        sonet_pcp_filter.setSizePolicy(sizePolicy)
        sonet_pcp_filter.setMinimumSize(QSize(0, 0))
        self.verticalLayout_2 = QVBoxLayout(sonet_pcp_filter)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.select_trip = QComboBox(sonet_pcp_filter)
        self.select_trip.setObjectName(u"select_trip")

        self.horizontalLayout_3.addWidget(self.select_trip)

        self.select_spacecraft = QComboBox(sonet_pcp_filter)
        self.select_spacecraft.addItem("")
        self.select_spacecraft.setObjectName(u"select_spacecraft")
        self.select_spacecraft.setEnabled(True)

        self.horizontalLayout_3.addWidget(self.select_spacecraft)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.toolBox = QToolBox(sonet_pcp_filter)
        self.toolBox.setObjectName(u"toolBox")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setGeometry(QRect(0, 0, 576, 482))
        self.verticalLayout_6 = QVBoxLayout(self.page_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.top_left_group_box = QGroupBox(self.page_3)
        self.top_left_group_box.setObjectName(u"top_left_group_box")
        self.top_left_group_box.setEnabled(False)
        self.top_left_group_box.setFlat(True)
        self.gridLayout_2 = QGridLayout(self.top_left_group_box)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setSizeConstraint(QLayout.SetMinimumSize)
        self.cb_dep_arriv_dates = QCheckBox(self.top_left_group_box)
        self.cb_dep_arriv_dates.setObjectName(u"cb_dep_arriv_dates")
        self.cb_dep_arriv_dates.setEnabled(False)
        self.cb_dep_arriv_dates.setCursor(QCursor(Qt.PointingHandCursor))
        self.cb_dep_arriv_dates.setChecked(False)

        self.verticalLayout_11.addWidget(self.cb_dep_arriv_dates)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.combo_planet = QComboBox(self.top_left_group_box)
        self.combo_planet.addItem("")
        self.combo_planet.addItem("")
        self.combo_planet.setObjectName(u"combo_planet")
        self.combo_planet.setEnabled(False)
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.combo_planet.sizePolicy().hasHeightForWidth())
        self.combo_planet.setSizePolicy(sizePolicy1)

        self.verticalLayout_14.addWidget(self.combo_planet)

        self.combo_dept_arriv = QComboBox(self.top_left_group_box)
        self.combo_dept_arriv.addItem("")
        self.combo_dept_arriv.addItem("")
        self.combo_dept_arriv.setObjectName(u"combo_dept_arriv")
        self.combo_dept_arriv.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.combo_dept_arriv.sizePolicy().hasHeightForWidth())
        self.combo_dept_arriv.setSizePolicy(sizePolicy1)

        self.verticalLayout_14.addWidget(self.combo_dept_arriv)


        self.verticalLayout_11.addLayout(self.verticalLayout_14)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_3)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setSizeConstraint(QLayout.SetMinimumSize)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setSizeConstraint(QLayout.SetMinimumSize)
        self.cb_dates_2 = QCheckBox(self.top_left_group_box)
        self.cb_dates_2.setObjectName(u"cb_dates_2")
        self.cb_dates_2.setEnabled(False)
        self.cb_dates_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_7.addWidget(self.cb_dates_2)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.combo_when_2 = QComboBox(self.top_left_group_box)
        self.combo_when_2.addItem("")
        self.combo_when_2.addItem("")
        self.combo_when_2.addItem("")
        self.combo_when_2.setObjectName(u"combo_when_2")
        self.combo_when_2.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.combo_when_2.sizePolicy().hasHeightForWidth())
        self.combo_when_2.setSizePolicy(sizePolicy1)

        self.verticalLayout_13.addWidget(self.combo_when_2)

        self.dateEdit = QDateEdit(self.top_left_group_box)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.dateEdit.sizePolicy().hasHeightForWidth())
        self.dateEdit.setSizePolicy(sizePolicy1)
        self.dateEdit.setMinimumDate(QDate(2020, 1, 1))
        self.dateEdit.setDate(QDate(2021, 5, 1))

        self.verticalLayout_13.addWidget(self.dateEdit)


        self.verticalLayout_7.addLayout(self.verticalLayout_13)


        self.verticalLayout_12.addLayout(self.verticalLayout_7)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetMinimumSize)
        self.cb_dates_1 = QCheckBox(self.top_left_group_box)
        self.cb_dates_1.setObjectName(u"cb_dates_1")
        self.cb_dates_1.setEnabled(False)
        self.cb_dates_1.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.cb_dates_1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.combo_at_least = QComboBox(self.top_left_group_box)
        self.combo_at_least.addItem("")
        self.combo_at_least.addItem("")
        self.combo_at_least.addItem("")
        self.combo_at_least.setObjectName(u"combo_at_least")
        self.combo_at_least.setEnabled(False)
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.combo_at_least.sizePolicy().hasHeightForWidth())
        self.combo_at_least.setSizePolicy(sizePolicy2)

        self.horizontalLayout_4.addWidget(self.combo_at_least)

        self.spin_number = QSpinBox(self.top_left_group_box)
        self.spin_number.setObjectName(u"spin_number")
        self.spin_number.setEnabled(False)
        sizePolicy.setHeightForWidth(self.spin_number.sizePolicy().hasHeightForWidth())
        self.spin_number.setSizePolicy(sizePolicy)
        self.spin_number.setMinimumSize(QSize(0, 26))
        self.spin_number.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.spin_number.setMaximum(999999)

        self.horizontalLayout_4.addWidget(self.spin_number)

        self.combo_time_scale = QComboBox(self.top_left_group_box)
        self.combo_time_scale.addItem("")
        self.combo_time_scale.setObjectName(u"combo_time_scale")
        self.combo_time_scale.setEnabled(False)
        sizePolicy.setHeightForWidth(self.combo_time_scale.sizePolicy().hasHeightForWidth())
        self.combo_time_scale.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.combo_time_scale)

        self.combo_when = QComboBox(self.top_left_group_box)
        self.combo_when.addItem("")
        self.combo_when.addItem("")
        self.combo_when.setObjectName(u"combo_when")
        self.combo_when.setEnabled(False)
        sizePolicy.setHeightForWidth(self.combo_when.sizePolicy().hasHeightForWidth())
        self.combo_when.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.combo_when)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.radio_mission = QRadioButton(self.top_left_group_box)
        self.radio_mission.setObjectName(u"radio_mission")
        self.radio_mission.setEnabled(False)
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.radio_mission.sizePolicy().hasHeightForWidth())
        self.radio_mission.setSizePolicy(sizePolicy3)
        self.radio_mission.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_10.addWidget(self.radio_mission)

        self.radio_spacecraft = QRadioButton(self.top_left_group_box)
        self.radio_spacecraft.setObjectName(u"radio_spacecraft")
        self.radio_spacecraft.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.radio_spacecraft.sizePolicy().hasHeightForWidth())
        self.radio_spacecraft.setSizePolicy(sizePolicy3)
        self.radio_spacecraft.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_10.addWidget(self.radio_spacecraft)


        self.verticalLayout_3.addLayout(self.horizontalLayout_10)

        self.combo_select_spacecraft = QComboBox(self.top_left_group_box)
        self.combo_select_spacecraft.setObjectName(u"combo_select_spacecraft")
        self.combo_select_spacecraft.setEnabled(False)
        sizePolicy4 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.combo_select_spacecraft.sizePolicy().hasHeightForWidth())
        self.combo_select_spacecraft.setSizePolicy(sizePolicy4)

        self.verticalLayout_3.addWidget(self.combo_select_spacecraft)

        self.combo_select_trip = QComboBox(self.top_left_group_box)
        self.combo_select_trip.setObjectName(u"combo_select_trip")
        self.combo_select_trip.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.combo_select_trip.sizePolicy().hasHeightForWidth())
        self.combo_select_trip.setSizePolicy(sizePolicy2)

        self.verticalLayout_3.addWidget(self.combo_select_trip)

        self.combo_event = QComboBox(self.top_left_group_box)
        self.combo_event.addItem("")
        self.combo_event.setObjectName(u"combo_event")
        self.combo_event.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.combo_event.sizePolicy().hasHeightForWidth())
        self.combo_event.setSizePolicy(sizePolicy2)

        self.verticalLayout_3.addWidget(self.combo_event)


        self.verticalLayout_12.addLayout(self.verticalLayout_3)


        self.verticalLayout_11.addLayout(self.verticalLayout_12)


        self.gridLayout_2.addLayout(self.verticalLayout_11, 0, 0, 1, 1)


        self.verticalLayout_6.addWidget(self.top_left_group_box)

        self.toolBox.addItem(self.page_3, u"Dates")
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.page_4.setGeometry(QRect(0, 0, 576, 220))
        self.verticalLayout_5 = QVBoxLayout(self.page_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.time_of_flight_group_box = QGroupBox(self.page_4)
        self.time_of_flight_group_box.setObjectName(u"time_of_flight_group_box")
        self.time_of_flight_group_box.setEnabled(False)
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.time_of_flight_group_box.sizePolicy().hasHeightForWidth())
        self.time_of_flight_group_box.setSizePolicy(sizePolicy5)
        self.time_of_flight_group_box.setFlat(True)
        self.gridLayout_5 = QGridLayout(self.time_of_flight_group_box)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.cb_time_of_flight = QCheckBox(self.time_of_flight_group_box)
        self.cb_time_of_flight.setObjectName(u"cb_time_of_flight")
        self.cb_time_of_flight.setEnabled(False)
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.cb_time_of_flight.sizePolicy().hasHeightForWidth())
        self.cb_time_of_flight.setSizePolicy(sizePolicy6)
        self.cb_time_of_flight.setCursor(QCursor(Qt.PointingHandCursor))
        self.cb_time_of_flight.setChecked(False)

        self.gridLayout_5.addWidget(self.cb_time_of_flight, 0, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_4, 2, 1, 1, 1)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setSizeConstraint(QLayout.SetMinimumSize)
        self.combo_time_of_flight = QComboBox(self.time_of_flight_group_box)
        self.combo_time_of_flight.addItem("")
        self.combo_time_of_flight.setObjectName(u"combo_time_of_flight")
        self.combo_time_of_flight.setEnabled(False)
        sizePolicy6.setHeightForWidth(self.combo_time_of_flight.sizePolicy().hasHeightForWidth())
        self.combo_time_of_flight.setSizePolicy(sizePolicy6)

        self.verticalLayout_10.addWidget(self.combo_time_of_flight)

        self.combo_time_of_flight_operator = QComboBox(self.time_of_flight_group_box)
        self.combo_time_of_flight_operator.addItem("")
        self.combo_time_of_flight_operator.addItem("")
        self.combo_time_of_flight_operator.setObjectName(u"combo_time_of_flight_operator")
        self.combo_time_of_flight_operator.setEnabled(False)
        sizePolicy6.setHeightForWidth(self.combo_time_of_flight_operator.sizePolicy().hasHeightForWidth())
        self.combo_time_of_flight_operator.setSizePolicy(sizePolicy6)

        self.verticalLayout_10.addWidget(self.combo_time_of_flight_operator)

        self.spin_number_2 = QSpinBox(self.time_of_flight_group_box)
        self.spin_number_2.setObjectName(u"spin_number_2")
        self.spin_number_2.setEnabled(False)
        self.spin_number_2.setMaximum(10000)

        self.verticalLayout_10.addWidget(self.spin_number_2)

        self.combo_time_scale_2 = QComboBox(self.time_of_flight_group_box)
        self.combo_time_scale_2.addItem("")
        self.combo_time_scale_2.addItem("")
        self.combo_time_scale_2.addItem("")
        self.combo_time_scale_2.addItem("")
        self.combo_time_scale_2.setObjectName(u"combo_time_scale_2")
        self.combo_time_scale_2.setEnabled(False)
        sizePolicy6.setHeightForWidth(self.combo_time_scale_2.sizePolicy().hasHeightForWidth())
        self.combo_time_scale_2.setSizePolicy(sizePolicy6)

        self.verticalLayout_10.addWidget(self.combo_time_scale_2)


        self.gridLayout_5.addLayout(self.verticalLayout_10, 1, 1, 1, 1)


        self.verticalLayout_5.addWidget(self.time_of_flight_group_box)

        self.toolBox.addItem(self.page_4, u"Time Of Flight")
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.page_5.setGeometry(QRect(0, 0, 561, 205))
        self.verticalLayout_4 = QVBoxLayout(self.page_5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.energy_group_box = QGroupBox(self.page_5)
        self.energy_group_box.setObjectName(u"energy_group_box")
        self.energy_group_box.setEnabled(False)
        self.energy_group_box.setFlat(True)
        self.horizontalLayout_2 = QHBoxLayout(self.energy_group_box)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.cb_energy = QCheckBox(self.energy_group_box)
        self.cb_energy.setObjectName(u"cb_energy")
        self.cb_energy.setEnabled(False)
        sizePolicy7 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.cb_energy.sizePolicy().hasHeightForWidth())
        self.cb_energy.setSizePolicy(sizePolicy7)
        self.cb_energy.setCursor(QCursor(Qt.PointingHandCursor))
        self.cb_energy.setChecked(False)

        self.horizontalLayout_2.addWidget(self.cb_energy)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.combo_energy_parameter = QComboBox(self.energy_group_box)
        self.combo_energy_parameter.addItem("")
        self.combo_energy_parameter.addItem("")
        self.combo_energy_parameter.addItem("")
        self.combo_energy_parameter.addItem("")
        self.combo_energy_parameter.addItem("")
        self.combo_energy_parameter.addItem("")
        self.combo_energy_parameter.setObjectName(u"combo_energy_parameter")
        self.combo_energy_parameter.setEnabled(False)

        self.verticalLayout_15.addWidget(self.combo_energy_parameter)

        self.combo_energy_operator = QComboBox(self.energy_group_box)
        self.combo_energy_operator.addItem("")
        self.combo_energy_operator.addItem("")
        self.combo_energy_operator.setObjectName(u"combo_energy_operator")
        self.combo_energy_operator.setEnabled(False)
        sizePolicy6.setHeightForWidth(self.combo_energy_operator.sizePolicy().hasHeightForWidth())
        self.combo_energy_operator.setSizePolicy(sizePolicy6)
        self.combo_energy_operator.setMinimumSize(QSize(0, 0))

        self.verticalLayout_15.addWidget(self.combo_energy_operator)

        self.spin_energy_number = QSpinBox(self.energy_group_box)
        self.spin_energy_number.setObjectName(u"spin_energy_number")
        self.spin_energy_number.setEnabled(False)
        self.spin_energy_number.setMaximum(10000)

        self.verticalLayout_15.addWidget(self.spin_energy_number)

        self.combo_energy_units = QComboBox(self.energy_group_box)
        self.combo_energy_units.addItem("")
        self.combo_energy_units.addItem("")
        self.combo_energy_units.addItem("")
        self.combo_energy_units.setObjectName(u"combo_energy_units")
        self.combo_energy_units.setEnabled(False)

        self.verticalLayout_15.addWidget(self.combo_energy_units)


        self.horizontalLayout_2.addLayout(self.verticalLayout_15)


        self.verticalLayout_4.addWidget(self.energy_group_box)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_7)

        self.toolBox.addItem(self.page_5, u"Energy")
        self.auto_trajectory_page = QWidget()
        self.auto_trajectory_page.setObjectName(u"auto_trajectory_page")
        self.auto_trajectory_page.setGeometry(QRect(0, 0, 576, 165))
        self.verticalLayout_8 = QVBoxLayout(self.auto_trajectory_page)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.auto_trajectory_gb = QGroupBox(self.auto_trajectory_page)
        self.auto_trajectory_gb.setObjectName(u"auto_trajectory_gb")
        self.auto_trajectory_gb.setEnabled(False)
        self.auto_trajectory_gb.setFlat(True)
        self.verticalLayout_9 = QVBoxLayout(self.auto_trajectory_gb)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.auto_traj_sel_cb_enabled = QCheckBox(self.auto_trajectory_gb)
        self.auto_traj_sel_cb_enabled.setObjectName(u"auto_traj_sel_cb_enabled")
        self.auto_traj_sel_cb_enabled.setEnabled(False)

        self.verticalLayout_9.addWidget(self.auto_traj_sel_cb_enabled)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.auto_traj_sel_cmb_min_max = QComboBox(self.auto_trajectory_gb)
        self.auto_traj_sel_cmb_min_max.addItem("")
        self.auto_traj_sel_cmb_min_max.addItem("")
        self.auto_traj_sel_cmb_min_max.setObjectName(u"auto_traj_sel_cmb_min_max")
        self.auto_traj_sel_cmb_min_max.setEnabled(False)

        self.horizontalLayout_5.addWidget(self.auto_traj_sel_cmb_min_max)

        self.auto_traj_sel_cmb_item = QComboBox(self.auto_trajectory_gb)
        self.auto_traj_sel_cmb_item.addItem("")
        self.auto_traj_sel_cmb_item.addItem("")
        self.auto_traj_sel_cmb_item.addItem("")
        self.auto_traj_sel_cmb_item.addItem("")
        self.auto_traj_sel_cmb_item.addItem("")
        self.auto_traj_sel_cmb_item.addItem("")
        self.auto_traj_sel_cmb_item.addItem("")
        self.auto_traj_sel_cmb_item.addItem("")
        self.auto_traj_sel_cmb_item.addItem("")
        self.auto_traj_sel_cmb_item.setObjectName(u"auto_traj_sel_cmb_item")
        self.auto_traj_sel_cmb_item.setEnabled(False)

        self.horizontalLayout_5.addWidget(self.auto_traj_sel_cmb_item)


        self.verticalLayout_9.addLayout(self.horizontalLayout_5)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_5)


        self.gridLayout_3.addWidget(self.auto_trajectory_gb, 1, 0, 1, 1)


        self.verticalLayout_8.addLayout(self.gridLayout_3)

        self.toolBox.addItem(self.auto_trajectory_page, u"Auto Trajectory Selection")

        self.verticalLayout_2.addWidget(self.toolBox)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.pb_reset = QPushButton(sonet_pcp_filter)
        self.pb_reset.setObjectName(u"pb_reset")
        self.pb_reset.setEnabled(True)

        self.horizontalLayout_9.addWidget(self.pb_reset)

        self.pb_add = QPushButton(sonet_pcp_filter)
        self.pb_add.setObjectName(u"pb_add")
        self.pb_add.setEnabled(False)

        self.horizontalLayout_9.addWidget(self.pb_add)


        self.verticalLayout_2.addLayout(self.horizontalLayout_9)

        self.bottom_group_box = QGroupBox(sonet_pcp_filter)
        self.bottom_group_box.setObjectName(u"bottom_group_box")
        self.bottom_group_box.setEnabled(False)
        self.bottom_group_box.setFlat(True)
        self.verticalLayout = QVBoxLayout(self.bottom_group_box)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.bottom_grid_layout = QGridLayout()
        self.bottom_grid_layout.setObjectName(u"bottom_grid_layout")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.pb_delete = QPushButton(self.bottom_group_box)
        self.pb_delete.setObjectName(u"pb_delete")
        self.pb_delete.setEnabled(False)

        self.horizontalLayout_14.addWidget(self.pb_delete)

        self.pb_delete_all = QPushButton(self.bottom_group_box)
        self.pb_delete_all.setObjectName(u"pb_delete_all")
        self.pb_delete_all.setEnabled(False)

        self.horizontalLayout_14.addWidget(self.pb_delete_all)


        self.bottom_grid_layout.addLayout(self.horizontalLayout_14, 1, 0, 1, 1)

        self.applied_filters_table_view = QTableView(self.bottom_group_box)
        self.applied_filters_table_view.setObjectName(u"applied_filters_table_view")
        self.applied_filters_table_view.setEnabled(False)
        sizePolicy8 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Maximum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.applied_filters_table_view.sizePolicy().hasHeightForWidth())
        self.applied_filters_table_view.setSizePolicy(sizePolicy8)
        self.applied_filters_table_view.setMinimumSize(QSize(100, 0))
        self.applied_filters_table_view.setAlternatingRowColors(True)
        self.applied_filters_table_view.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.applied_filters_table_view.horizontalHeader().setStretchLastSection(True)
        self.applied_filters_table_view.verticalHeader().setStretchLastSection(False)

        self.bottom_grid_layout.addWidget(self.applied_filters_table_view, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.bottom_grid_layout)


        self.verticalLayout_2.addWidget(self.bottom_group_box)

        self.dialog_button_box = QDialogButtonBox(sonet_pcp_filter)
        self.dialog_button_box.setObjectName(u"dialog_button_box")
        self.dialog_button_box.setEnabled(True)
        self.dialog_button_box.setCursor(QCursor(Qt.PointingHandCursor))
        self.dialog_button_box.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout_2.addWidget(self.dialog_button_box)

        self.status_bar_HLayout = QHBoxLayout()
        self.status_bar_HLayout.setObjectName(u"status_bar_HLayout")

        self.verticalLayout_2.addLayout(self.status_bar_HLayout)


        self.retranslateUi(sonet_pcp_filter)
        self.select_spacecraft.activated.connect(self.cb_dep_arriv_dates.show)

        self.toolBox.setCurrentIndex(2)
        self.combo_when.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(sonet_pcp_filter)
    # setupUi

    def retranslateUi(self, sonet_pcp_filter):
        sonet_pcp_filter.setWindowTitle(QCoreApplication.translate("sonet_pcp_filter", u"SONet s/c filter editor", None))
#if QT_CONFIG(accessibility)
        sonet_pcp_filter.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.select_spacecraft.setItemText(0, QCoreApplication.translate("sonet_pcp_filter", u"Select s/c", None))

        self.top_left_group_box.setTitle("")
        self.cb_dep_arriv_dates.setText("")
        self.combo_planet.setItemText(0, QCoreApplication.translate("sonet_pcp_filter", u"Earth", None))
        self.combo_planet.setItemText(1, QCoreApplication.translate("sonet_pcp_filter", u"Mars", None))

        self.combo_dept_arriv.setItemText(0, QCoreApplication.translate("sonet_pcp_filter", u"Departs", None))
        self.combo_dept_arriv.setItemText(1, QCoreApplication.translate("sonet_pcp_filter", u"Arrives", None))

        self.cb_dates_2.setText("")
        self.combo_when_2.setItemText(0, QCoreApplication.translate("sonet_pcp_filter", u"On", None))
        self.combo_when_2.setItemText(1, QCoreApplication.translate("sonet_pcp_filter", u"Before", None))
        self.combo_when_2.setItemText(2, QCoreApplication.translate("sonet_pcp_filter", u"After", None))

        self.cb_dates_1.setText("")
        self.combo_at_least.setItemText(0, QCoreApplication.translate("sonet_pcp_filter", u"At least", None))
        self.combo_at_least.setItemText(1, QCoreApplication.translate("sonet_pcp_filter", u"At maximum", None))
        self.combo_at_least.setItemText(2, QCoreApplication.translate("sonet_pcp_filter", u"At the same time", None))

        self.combo_time_scale.setItemText(0, QCoreApplication.translate("sonet_pcp_filter", u"Days", None))

#if QT_CONFIG(accessibility)
        self.combo_time_scale.setAccessibleName(QCoreApplication.translate("sonet_pcp_filter", u"accesible", None))
#endif // QT_CONFIG(accessibility)
        self.combo_when.setItemText(0, QCoreApplication.translate("sonet_pcp_filter", u"Before", None))
        self.combo_when.setItemText(1, QCoreApplication.translate("sonet_pcp_filter", u"After", None))

        self.radio_mission.setText(QCoreApplication.translate("sonet_pcp_filter", u"Mission", None))
        self.radio_spacecraft.setText(QCoreApplication.translate("sonet_pcp_filter", u"S/C", None))
        self.combo_event.setItemText(0, QCoreApplication.translate("sonet_pcp_filter", u"Select event", None))

        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), QCoreApplication.translate("sonet_pcp_filter", u"Dates", None))
        self.time_of_flight_group_box.setTitle("")
        self.cb_time_of_flight.setText("")
        self.combo_time_of_flight.setItemText(0, QCoreApplication.translate("sonet_pcp_filter", u"Time of flight", None))

        self.combo_time_of_flight_operator.setItemText(0, QCoreApplication.translate("sonet_pcp_filter", u"<=", None))
        self.combo_time_of_flight_operator.setItemText(1, QCoreApplication.translate("sonet_pcp_filter", u">=", None))

        self.combo_time_scale_2.setItemText(0, QCoreApplication.translate("sonet_pcp_filter", u"Days", None))
        self.combo_time_scale_2.setItemText(1, QCoreApplication.translate("sonet_pcp_filter", u"Weeks", None))
        self.combo_time_scale_2.setItemText(2, QCoreApplication.translate("sonet_pcp_filter", u"Months", None))
        self.combo_time_scale_2.setItemText(3, QCoreApplication.translate("sonet_pcp_filter", u"Years", None))

        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), QCoreApplication.translate("sonet_pcp_filter", u"Time Of Flight", None))
        self.energy_group_box.setTitle("")
        self.cb_energy.setText("")
        self.combo_energy_parameter.setItemText(0, QCoreApplication.translate("sonet_pcp_filter", u"dvt", None))
        self.combo_energy_parameter.setItemText(1, QCoreApplication.translate("sonet_pcp_filter", u"dvd", None))
        self.combo_energy_parameter.setItemText(2, QCoreApplication.translate("sonet_pcp_filter", u"dva", None))
        self.combo_energy_parameter.setItemText(3, QCoreApplication.translate("sonet_pcp_filter", u"c3d", None))
        self.combo_energy_parameter.setItemText(4, QCoreApplication.translate("sonet_pcp_filter", u"c3a", None))
        self.combo_energy_parameter.setItemText(5, QCoreApplication.translate("sonet_pcp_filter", u"theta", None))

        self.combo_energy_operator.setItemText(0, QCoreApplication.translate("sonet_pcp_filter", u"<=", None))
        self.combo_energy_operator.setItemText(1, QCoreApplication.translate("sonet_pcp_filter", u">=", None))

        self.combo_energy_units.setItemText(0, QCoreApplication.translate("sonet_pcp_filter", u"km/s", None))
        self.combo_energy_units.setItemText(1, QCoreApplication.translate("sonet_pcp_filter", u"km2/s2", None))
        self.combo_energy_units.setItemText(2, QCoreApplication.translate("sonet_pcp_filter", u"deg", None))

        self.toolBox.setItemText(self.toolBox.indexOf(self.page_5), QCoreApplication.translate("sonet_pcp_filter", u"Energy", None))
        self.auto_trajectory_gb.setTitle("")
        self.auto_traj_sel_cb_enabled.setText("")
        self.auto_traj_sel_cmb_min_max.setItemText(0, QCoreApplication.translate("sonet_pcp_filter", u"Min", None))
        self.auto_traj_sel_cmb_min_max.setItemText(1, QCoreApplication.translate("sonet_pcp_filter", u"Max", None))

        self.auto_traj_sel_cmb_item.setItemText(0, QCoreApplication.translate("sonet_pcp_filter", u"Departure date", None))
        self.auto_traj_sel_cmb_item.setItemText(1, QCoreApplication.translate("sonet_pcp_filter", u"Arrival date", None))
        self.auto_traj_sel_cmb_item.setItemText(2, QCoreApplication.translate("sonet_pcp_filter", u"tof", None))
        self.auto_traj_sel_cmb_item.setItemText(3, QCoreApplication.translate("sonet_pcp_filter", u"theta", None))
        self.auto_traj_sel_cmb_item.setItemText(4, QCoreApplication.translate("sonet_pcp_filter", u"dvt", None))
        self.auto_traj_sel_cmb_item.setItemText(5, QCoreApplication.translate("sonet_pcp_filter", u"dvd", None))
        self.auto_traj_sel_cmb_item.setItemText(6, QCoreApplication.translate("sonet_pcp_filter", u"dva", None))
        self.auto_traj_sel_cmb_item.setItemText(7, QCoreApplication.translate("sonet_pcp_filter", u"c3d", None))
        self.auto_traj_sel_cmb_item.setItemText(8, QCoreApplication.translate("sonet_pcp_filter", u"c3a", None))

        self.toolBox.setItemText(self.toolBox.indexOf(self.auto_trajectory_page), QCoreApplication.translate("sonet_pcp_filter", u"Auto Trajectory Selection", None))
        self.pb_reset.setText(QCoreApplication.translate("sonet_pcp_filter", u"Reset", None))
        self.pb_add.setText(QCoreApplication.translate("sonet_pcp_filter", u"Add", None))
        self.bottom_group_box.setTitle(QCoreApplication.translate("sonet_pcp_filter", u"Filter", None))
        self.pb_delete.setText(QCoreApplication.translate("sonet_pcp_filter", u"Delete", None))
        self.pb_delete_all.setText(QCoreApplication.translate("sonet_pcp_filter", u"Delete all", None))
    # retranslateUi

