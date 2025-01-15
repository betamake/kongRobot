# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoginForm.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.softwareLabel = QLabel(Form)
        self.softwareLabel.setObjectName(u"softwareLabel")

        self.horizontalLayout_6.addWidget(self.softwareLabel)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)


        self.gridLayout.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 81, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.usernameLabel = QLabel(Form)
        self.usernameLabel.setObjectName(u"usernameLabel")

        self.horizontalLayout.addWidget(self.usernameLabel)

        self.usernameLineEdit = QLineEdit(Form)
        self.usernameLineEdit.setObjectName(u"usernameLineEdit")

        self.horizontalLayout.addWidget(self.usernameLineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.passwordLabel = QLabel(Form)
        self.passwordLabel.setObjectName(u"passwordLabel")

        self.horizontalLayout_2.addWidget(self.passwordLabel)

        self.passwordLineEdit = QLineEdit(Form)
        self.passwordLineEdit.setObjectName(u"passwordLineEdit")

        self.horizontalLayout_2.addWidget(self.passwordLineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.registerPushButton = QPushButton(Form)
        self.registerPushButton.setObjectName(u"registerPushButton")

        self.horizontalLayout_4.addWidget(self.registerPushButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.loginPushButton = QPushButton(Form)
        self.loginPushButton.setObjectName(u"loginPushButton")

        self.horizontalLayout_4.addWidget(self.loginPushButton)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.ForgotPasswordPushButton = QPushButton(Form)
        self.ForgotPasswordPushButton.setObjectName(u"ForgotPasswordPushButton")

        self.horizontalLayout_5.addWidget(self.ForgotPasswordPushButton)


        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.gridLayout.addLayout(self.verticalLayout, 2, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.softwareLabel.setText(QCoreApplication.translate("Form", u"diaoMTech\u81ea\u52a8\u5316\u673a\u5668\u4eba", None))
        self.usernameLabel.setText(QCoreApplication.translate("Form", u"\u7528\u6237\u540d:", None))
        self.passwordLabel.setText(QCoreApplication.translate("Form", u"  \u5bc6\u7801  :", None))
        self.registerPushButton.setText(QCoreApplication.translate("Form", u"\u6ce8\u518c", None))
        self.loginPushButton.setText(QCoreApplication.translate("Form", u"\u767b\u5f55", None))
        self.ForgotPasswordPushButton.setText(QCoreApplication.translate("Form", u"\u5fd8\u8bb0\u5bc6\u7801", None))
    # retranslateUi

