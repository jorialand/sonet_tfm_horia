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
        sonet_canvas.resize(800, 600)
        self.verticalLayout = QVBoxLayout(sonet_canvas)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.sonet_canvas_view = QGraphicsView(sonet_canvas)
        self.sonet_canvas_view.setObjectName(u"sonet_canvas_view")

        self.verticalLayout.addWidget(self.sonet_canvas_view)


        self.retranslateUi(sonet_canvas)

        QMetaObject.connectSlotsByName(sonet_canvas)
    # setupUi

    def retranslateUi(self, sonet_canvas):
        sonet_canvas.setWindowTitle(QCoreApplication.translate("sonet_canvas", u"sonet_canvas", None))
    # retranslateUi

