# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sonet_pcp_filter_qt.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject,
                            Qt)
from PySide2.QtGui import (QCursor)
from PySide2.QtWidgets import *


class Ui_sonet_pcp_filter(object):
    def setupUi(self, sonet_pcp_filter):
        if not sonet_pcp_filter.objectName():
            sonet_pcp_filter.setObjectName(u"sonet_pcp_filter")
        sonet_pcp_filter.setEnabled(True)
        sonet_pcp_filter.resize(697, 704)
        self.gridLayout = QGridLayout(sonet_pcp_filter)
        self.gridLayout.setObjectName(u"gridLayout")
        self.bottom_group_box = QGroupBox(sonet_pcp_filter)
        self.bottom_group_box.setObjectName(u"bottom_group_box")
        self.bottom_group_box.setEnabled(False)
        self.verticalLayout = QVBoxLayout(self.bottom_group_box)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.bottom_grid_layout = QGridLayout()
        self.bottom_grid_layout.setObjectName(u"bottom_grid_layout")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.pb_add_4 = QPushButton(self.bottom_group_box)
        self.pb_add_4.setObjectName(u"pb_add_4")
        self.pb_add_4.setEnabled(False)

        self.horizontalLayout_14.addWidget(self.pb_add_4)

        self.pb_add = QPushButton(self.bottom_group_box)
        self.pb_add.setObjectName(u"pb_add")
        self.pb_add.setEnabled(False)

        self.horizontalLayout_14.addWidget(self.pb_add)


        self.bottom_grid_layout.addLayout(self.horizontalLayout_14, 2, 0, 1, 1)

        self.label = QLabel(self.bottom_group_box)
        self.label.setObjectName(u"label")
        self.label.setEnabled(False)

        self.bottom_grid_layout.addWidget(self.label, 1, 0, 1, 2)

        self.applied_filters_table_view = QTableView(self.bottom_group_box)
        self.applied_filters_table_view.setObjectName(u"applied_filters_table_view")
        self.applied_filters_table_view.setEnabled(False)

        self.bottom_grid_layout.addWidget(self.applied_filters_table_view, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.bottom_grid_layout)


        self.gridLayout.addWidget(self.bottom_group_box, 17, 0, 1, 2)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_5, 4, 0, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_6, 10, 0, 1, 1)

        self.dialog_button_box = QDialogButtonBox(sonet_pcp_filter)
        self.dialog_button_box.setObjectName(u"dialog_button_box")
        self.dialog_button_box.setEnabled(True)
        self.dialog_button_box.setCursor(QCursor(Qt.PointingHandCursor))
        self.dialog_button_box.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.dialog_button_box, 18, 1, 1, 1)

        self.select_spacecraft = QComboBox(sonet_pcp_filter)
        self.select_spacecraft.addItem("")
        self.select_spacecraft.setObjectName(u"select_spacecraft")
        self.select_spacecraft.setEnabled(True)

        self.gridLayout.addWidget(self.select_spacecraft, 0, 0, 1, 2)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.pb_clean = QPushButton(sonet_pcp_filter)
        self.pb_clean.setObjectName(u"pb_clean")
        self.pb_clean.setEnabled(False)

        self.horizontalLayout_9.addWidget(self.pb_clean)

        self.pb_add_6 = QPushButton(sonet_pcp_filter)
        self.pb_add_6.setObjectName(u"pb_add_6")
        self.pb_add_6.setEnabled(False)

        self.horizontalLayout_9.addWidget(self.pb_add_6)


        self.gridLayout.addLayout(self.horizontalLayout_9, 8, 0, 2, 2)

        self.top_grid_layout = QGridLayout()
        self.top_grid_layout.setObjectName(u"top_grid_layout")
        self.time_of_flight_group_box = QGroupBox(sonet_pcp_filter)
        self.time_of_flight_group_box.setObjectName(u"time_of_flight_group_box")
        self.time_of_flight_group_box.setEnabled(False)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.time_of_flight_group_box.sizePolicy().hasHeightForWidth())
        self.time_of_flight_group_box.setSizePolicy(sizePolicy)
        self.gridLayout_5 = QGridLayout(self.time_of_flight_group_box)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.time_of_flight_grid_layout = QGridLayout()
        self.time_of_flight_grid_layout.setObjectName(u"time_of_flight_grid_layout")
        self.time_of_flight_grid_layout.setSizeConstraint(QLayout.SetNoConstraint)
        self.combo_time_of_flight = QComboBox(self.time_of_flight_group_box)
        self.combo_time_of_flight.addItem("")
        self.combo_time_of_flight.setObjectName(u"combo_time_of_flight")
        self.combo_time_of_flight.setEnabled(False)

        self.time_of_flight_grid_layout.addWidget(self.combo_time_of_flight, 0, 0, 1, 2)

        self.combo_time_of_flight_operator = QComboBox(self.time_of_flight_group_box)
        self.combo_time_of_flight_operator.addItem("")
        self.combo_time_of_flight_operator.addItem("")
        self.combo_time_of_flight_operator.addItem("")
        self.combo_time_of_flight_operator.setObjectName(u"combo_time_of_flight_operator")
        self.combo_time_of_flight_operator.setEnabled(False)

        self.time_of_flight_grid_layout.addWidget(self.combo_time_of_flight_operator, 1, 0, 1, 2)

        self.spin_number_2 = QSpinBox(self.time_of_flight_group_box)
        self.spin_number_2.setObjectName(u"spin_number_2")
        self.spin_number_2.setEnabled(False)

        self.time_of_flight_grid_layout.addWidget(self.spin_number_2, 3, 0, 1, 1)

        self.combo_time_scale_2 = QComboBox(self.time_of_flight_group_box)
        self.combo_time_scale_2.addItem("")
        self.combo_time_scale_2.addItem("")
        self.combo_time_scale_2.addItem("")
        self.combo_time_scale_2.addItem("")
        self.combo_time_scale_2.setObjectName(u"combo_time_scale_2")
        self.combo_time_scale_2.setEnabled(False)

        self.time_of_flight_grid_layout.addWidget(self.combo_time_scale_2, 3, 1, 1, 1)

        self.time_of_flight_grid_layout.setRowStretch(0, 10)

        self.gridLayout_5.addLayout(self.time_of_flight_grid_layout, 1, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_4, 2, 0, 1, 1)

        self.cb_time_of_flight = QCheckBox(self.time_of_flight_group_box)
        self.cb_time_of_flight.setObjectName(u"cb_time_of_flight")
        self.cb_time_of_flight.setEnabled(False)

        self.gridLayout_5.addWidget(self.cb_time_of_flight, 0, 0, 1, 1)


        self.top_grid_layout.addWidget(self.time_of_flight_group_box, 1, 2, 1, 1)

        self.energy_group_box = QGroupBox(sonet_pcp_filter)
        self.energy_group_box.setObjectName(u"energy_group_box")
        self.energy_group_box.setEnabled(False)
        self.horizontalLayout_2 = QHBoxLayout(self.energy_group_box)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.cb_energy = QCheckBox(self.energy_group_box)
        self.cb_energy.setObjectName(u"cb_energy")
        self.cb_energy.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.cb_energy)

        self.energy_grid_layout = QGridLayout()
        self.energy_grid_layout.setObjectName(u"energy_grid_layout")
        self.spin_energy_number = QSpinBox(self.energy_group_box)
        self.spin_energy_number.setObjectName(u"spin_energy_number")
        self.spin_energy_number.setEnabled(False)
        self.spin_energy_number.setMaximum(999999)

        self.energy_grid_layout.addWidget(self.spin_energy_number, 1, 2, 1, 1)

        self.combo_energy_parameter = QComboBox(self.energy_group_box)
        self.combo_energy_parameter.addItem("")
        self.combo_energy_parameter.addItem("")
        self.combo_energy_parameter.addItem("")
        self.combo_energy_parameter.addItem("")
        self.combo_energy_parameter.addItem("")
        self.combo_energy_parameter.addItem("")
        self.combo_energy_parameter.setObjectName(u"combo_energy_parameter")
        self.combo_energy_parameter.setEnabled(False)

        self.energy_grid_layout.addWidget(self.combo_energy_parameter, 1, 0, 1, 1)

        self.combo_energy_operator = QComboBox(self.energy_group_box)
        self.combo_energy_operator.addItem("")
        self.combo_energy_operator.addItem("")
        self.combo_energy_operator.addItem("")
        self.combo_energy_operator.setObjectName(u"combo_energy_operator")
        self.combo_energy_operator.setEnabled(False)

        self.energy_grid_layout.addWidget(self.combo_energy_operator, 1, 1, 1, 1)

        self.combo_energy_units = QComboBox(self.energy_group_box)
        self.combo_energy_units.addItem("")
        self.combo_energy_units.addItem("")
        self.combo_energy_units.addItem("")
        self.combo_energy_units.setObjectName(u"combo_energy_units")
        self.combo_energy_units.setEnabled(False)

        self.energy_grid_layout.addWidget(self.combo_energy_units, 1, 3, 1, 1)


        self.horizontalLayout_2.addLayout(self.energy_grid_layout)


        self.top_grid_layout.addWidget(self.energy_group_box, 2, 2, 1, 1)

        self.top_left_group_box = QGroupBox(sonet_pcp_filter)
        self.top_left_group_box.setObjectName(u"top_left_group_box")
        self.top_left_group_box.setEnabled(False)
        self.gridLayout_2 = QGridLayout(self.top_left_group_box)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.cb_time_of_flight_2 = QCheckBox(self.top_left_group_box)
        self.cb_time_of_flight_2.setObjectName(u"cb_time_of_flight_2")
        self.cb_time_of_flight_2.setEnabled(False)

        self.verticalLayout_11.addWidget(self.cb_time_of_flight_2)

        self.combo_dept_arriv = QComboBox(self.top_left_group_box)
        self.combo_dept_arriv.addItem("")
        self.combo_dept_arriv.addItem("")
        self.combo_dept_arriv.setObjectName(u"combo_dept_arriv")
        self.combo_dept_arriv.setEnabled(False)
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.combo_dept_arriv.sizePolicy().hasHeightForWidth())
        self.combo_dept_arriv.setSizePolicy(sizePolicy1)

        self.verticalLayout_11.addWidget(self.combo_dept_arriv)

        self.combo_planet = QComboBox(self.top_left_group_box)
        self.combo_planet.addItem("")
        self.combo_planet.addItem("")
        self.combo_planet.setObjectName(u"combo_planet")
        self.combo_planet.setEnabled(False)
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.combo_planet.sizePolicy().hasHeightForWidth())
        self.combo_planet.setSizePolicy(sizePolicy2)

        self.verticalLayout_11.addWidget(self.combo_planet)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetMinimumSize)
        self.checkBox = QCheckBox(self.top_left_group_box)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setEnabled(False)

        self.verticalLayout_3.addWidget(self.checkBox)

        self.spin_number = QSpinBox(self.top_left_group_box)
        self.spin_number.setObjectName(u"spin_number")
        self.spin_number.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.spin_number.sizePolicy().hasHeightForWidth())
        self.spin_number.setSizePolicy(sizePolicy1)
        self.spin_number.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.spin_number.setMaximum(999999)

        self.verticalLayout_3.addWidget(self.spin_number)

        self.combo_time_scale = QComboBox(self.top_left_group_box)
        self.combo_time_scale.addItem("")
        self.combo_time_scale.addItem("")
        self.combo_time_scale.addItem("")
        self.combo_time_scale.addItem("")
        self.combo_time_scale.addItem("")
        self.combo_time_scale.setObjectName(u"combo_time_scale")
        self.combo_time_scale.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.combo_time_scale.sizePolicy().hasHeightForWidth())
        self.combo_time_scale.setSizePolicy(sizePolicy1)

        self.verticalLayout_3.addWidget(self.combo_time_scale)

        self.combo_when = QComboBox(self.top_left_group_box)
        self.combo_when.addItem("")
        self.combo_when.addItem("")
        self.combo_when.setObjectName(u"combo_when")
        self.combo_when.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.combo_when.sizePolicy().hasHeightForWidth())
        self.combo_when.setSizePolicy(sizePolicy1)

        self.verticalLayout_3.addWidget(self.combo_when)

        self.combo_select_spacecraft = QComboBox(self.top_left_group_box)
        self.combo_select_spacecraft.addItem("")
        self.combo_select_spacecraft.setObjectName(u"combo_select_spacecraft")
        self.combo_select_spacecraft.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.combo_select_spacecraft.sizePolicy().hasHeightForWidth())
        self.combo_select_spacecraft.setSizePolicy(sizePolicy1)

        self.verticalLayout_3.addWidget(self.combo_select_spacecraft)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setSizeConstraint(QLayout.SetMinimumSize)
        self.checkBox_2 = QCheckBox(self.top_left_group_box)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setEnabled(False)

        self.verticalLayout_7.addWidget(self.checkBox_2)

        self.combo_when_2 = QComboBox(self.top_left_group_box)
        self.combo_when_2.addItem("")
        self.combo_when_2.addItem("")
        self.combo_when_2.addItem("")
        self.combo_when_2.setObjectName(u"combo_when_2")
        self.combo_when_2.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.combo_when_2.sizePolicy().hasHeightForWidth())
        self.combo_when_2.setSizePolicy(sizePolicy1)

        self.verticalLayout_7.addWidget(self.combo_when_2)

        self.dateEdit = QDateEdit(self.top_left_group_box)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.dateEdit.sizePolicy().hasHeightForWidth())
        self.dateEdit.setSizePolicy(sizePolicy1)

        self.verticalLayout_7.addWidget(self.dateEdit)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout_7)


        self.verticalLayout_11.addLayout(self.horizontalLayout_3)


        self.gridLayout_2.addLayout(self.verticalLayout_11, 0, 0, 1, 1)


        self.top_grid_layout.addWidget(self.top_left_group_box, 1, 1, 2, 1)


        self.gridLayout.addLayout(self.top_grid_layout, 3, 0, 1, 2)

        self.select_trip = QComboBox(sonet_pcp_filter)
        self.select_trip.addItem("")
        self.select_trip.setObjectName(u"select_trip")

        self.gridLayout.addWidget(self.select_trip, 1, 0, 1, 2)


        self.retranslateUi(sonet_pcp_filter)
        self.select_spacecraft.activated.connect(self.cb_time_of_flight_2.show)

        QMetaObject.connectSlotsByName(sonet_pcp_filter)
    # setupUi

    def retranslateUi(self, sonet_pcp_filter):
        sonet_pcp_filter.setWindowTitle(QCoreApplication.translate("sonet_pcp_filter", u"Apply filter to PCP table", None))
        self.bottom_group_box.setTitle(QCoreApplication.translate("sonet_pcp_filter", u"Applied filters", None))
        self.pb_add_4.setText(QCoreApplication.translate("sonet_pcp_filter", u"Delete", None))
        self.pb_add.setText(QCoreApplication.translate("sonet_pcp_filter", u"Delete all", None))
        self.label.setText(QCoreApplication.translate("sonet_pcp_filter", u"55 rows selected", None))
        self.select_spacecraft.setItemText(0, QCoreApplication.translate("sonet_pcp_filter", u"Select spacecraft", None))

        self.pb_clean.setText(QCoreApplication.translate("sonet_pcp_filter", u"Reset", None))
        self.pb_add_6.setText(QCoreApplication.translate("sonet_pcp_filter", u"Add", None))
        self.time_of_flight_group_box.setTitle(QCoreApplication.translate("sonet_pcp_filter", u"Time of flight", None))
        self.combo_time_of_flight.setItemText(0, QCoreApplication.translate("sonet_pcp_filter", u"Time of flight", None))

        self.combo_time_of_flight_operator.setItemText(0, QCoreApplication.translate("sonet_pcp_filter", u"is", None))
        self.combo_time_of_flight_operator.setItemText(1, QCoreApplication.translate("sonet_pcp_filter", u"is less than", None))
        self.combo_time_of_flight_operator.setItemText(2, QCoreApplication.translate("sonet_pcp_filter", u"is greater than", None))

        self.combo_time_scale_2.setItemText(0, QCoreApplication.translate("sonet_pcp_filter", u"Days", None))
        self.combo_time_scale_2.setItemText(1, QCoreApplication.translate("sonet_pcp_filter", u"Weeks", None))
        self.combo_time_scale_2.setItemText(2, QCoreApplication.translate("sonet_pcp_filter", u"Months", None))
        self.combo_time_scale_2.setItemText(3, QCoreApplication.translate("sonet_pcp_filter", u"Years", None))

        self.cb_time_of_flight.setText("")
        self.energy_group_box.setTitle(QCoreApplication.translate("sonet_pcp_filter", u"Energy", None))
        self.cb_energy.setText("")
        self.combo_energy_parameter.setItemText(0, QCoreApplication.translate("sonet_pcp_filter", u"dvt", None))
        self.combo_energy_parameter.setItemText(1, QCoreApplication.translate("sonet_pcp_filter", u"dvd", None))
        self.combo_energy_parameter.setItemText(2, QCoreApplication.translate("sonet_pcp_filter", u"dva", None))
        self.combo_energy_parameter.setItemText(3, QCoreApplication.translate("sonet_pcp_filter", u"c3d", None))
        self.combo_energy_parameter.setItemText(4, QCoreApplication.translate("sonet_pcp_filter", u"c3a", None))
        self.combo_energy_parameter.setItemText(5, QCoreApplication.translate("sonet_pcp_filter", u"theta", None))

        self.combo_energy_operator.setItemText(0, QCoreApplication.translate("sonet_pcp_filter", u"=", None))
        self.combo_energy_operator.setItemText(1, QCoreApplication.translate("sonet_pcp_filter", u">", None))
        self.combo_energy_operator.setItemText(2, QCoreApplication.translate("sonet_pcp_filter", u"<", None))

        self.combo_energy_units.setItemText(0, QCoreApplication.translate("sonet_pcp_filter", u"km/s", None))
        self.combo_energy_units.setItemText(1, QCoreApplication.translate("sonet_pcp_filter", u"km2/s2", None))
        self.combo_energy_units.setItemText(2, QCoreApplication.translate("sonet_pcp_filter", u"\u00ba", None))

        self.top_left_group_box.setTitle(QCoreApplication.translate("sonet_pcp_filter", u"Departure and arrival dates", None))
        self.cb_time_of_flight_2.setText("")
        self.combo_dept_arriv.setItemText(0, QCoreApplication.translate("sonet_pcp_filter", u"Departs", None))
        self.combo_dept_arriv.setItemText(1, QCoreApplication.translate("sonet_pcp_filter", u"Arrives", None))

        self.combo_planet.setItemText(0, QCoreApplication.translate("sonet_pcp_filter", u"Earth", None))
        self.combo_planet.setItemText(1, QCoreApplication.translate("sonet_pcp_filter", u"Mars", None))

        self.checkBox.setText("")
        self.combo_time_scale.setItemText(0, QCoreApplication.translate("sonet_pcp_filter", u"Days", None))
        self.combo_time_scale.setItemText(1, QCoreApplication.translate("sonet_pcp_filter", u"Weeks", None))
        self.combo_time_scale.setItemText(2, QCoreApplication.translate("sonet_pcp_filter", u"Months", None))
        self.combo_time_scale.setItemText(3, QCoreApplication.translate("sonet_pcp_filter", u"Years", None))
        self.combo_time_scale.setItemText(4, QCoreApplication.translate("sonet_pcp_filter", u"Launch opportunities", None))

#if QT_CONFIG(accessibility)
        self.combo_time_scale.setAccessibleName(QCoreApplication.translate("sonet_pcp_filter", u"accesible", None))
#endif // QT_CONFIG(accessibility)
        self.combo_when.setItemText(0, QCoreApplication.translate("sonet_pcp_filter", u"Before", None))
        self.combo_when.setItemText(1, QCoreApplication.translate("sonet_pcp_filter", u"After", None))

        self.combo_select_spacecraft.setItemText(0, QCoreApplication.translate("sonet_pcp_filter", u"Select spacecraft", None))

        self.checkBox_2.setText("")
        self.combo_when_2.setItemText(0, QCoreApplication.translate("sonet_pcp_filter", u"On", None))
        self.combo_when_2.setItemText(1, QCoreApplication.translate("sonet_pcp_filter", u"Before", None))
        self.combo_when_2.setItemText(2, QCoreApplication.translate("sonet_pcp_filter", u"After", None))

        self.select_trip.setItemText(0, QCoreApplication.translate("sonet_pcp_filter", u"Select trip", None))

    # retranslateUi

