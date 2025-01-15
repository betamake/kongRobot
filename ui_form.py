# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QPushButton,
    QSizePolicy, QTabWidget, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 600)
        self.gridLayout = QGridLayout(Widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.TaskConfigurationPushButton = QPushButton(Widget)
        self.TaskConfigurationPushButton.setObjectName(u"TaskConfigurationPushButton")

        self.horizontalLayout.addWidget(self.TaskConfigurationPushButton)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.tabWidget = QTabWidget(Widget)
        self.tabWidget.setObjectName(u"tabWidget")

        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)


        self.retranslateUi(Widget)

        self.tabWidget.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.TaskConfigurationPushButton.setText(QCoreApplication.translate("Widget", u"\u4efb\u52a1\u914d\u7f6e", None))
    # retranslateUi

