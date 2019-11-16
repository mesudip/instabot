# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'filters.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(702, 436)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.widget_3 = QtWidgets.QWidget(Form)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.frame = QtWidgets.QFrame(self.widget_3)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget_2 = QtWidgets.QWidget(self.groupBox)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.black_list_text = QtWidgets.QPlainTextEdit(self.widget_2)
        self.black_list_text.setObjectName("black_list_text")
        self.verticalLayout_2.addWidget(self.black_list_text)
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.horizontalLayout_3.addWidget(self.widget_2)
        self.widget = QtWidgets.QWidget(self.groupBox)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tag_text = QtWidgets.QPlainTextEdit(self.widget)
        self.tag_text.setObjectName("tag_text")
        self.verticalLayout.addWidget(self.tag_text)
        self.allow_radio = QtWidgets.QRadioButton(self.widget)
        self.allow_radio.setChecked(True)
        self.allow_radio.setObjectName("allow_radio")
        self.verticalLayout.addWidget(self.allow_radio)
        self.skip_radio = QtWidgets.QRadioButton(self.widget)
        self.skip_radio.setObjectName("skip_radio")
        self.verticalLayout.addWidget(self.skip_radio)
        self.horizontalLayout_3.addWidget(self.widget)
        self.horizontalLayout.addWidget(self.groupBox)
        self.horizontalLayout_2.addWidget(self.frame)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout_3.addWidget(self.widget_3)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.black_list_text, self.tag_text)
        Form.setTabOrder(self.tag_text, self.allow_radio)
        Form.setTabOrder(self.allow_radio, self.skip_radio)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "BlackList and Tag Settings"))
        self.label_2.setText(_translate("Form", "Black List"))
        self.label_3.setText(_translate("Form", "The posts by the users in black list \n"
                                                " will be filtered out."))
        self.label.setText(_translate("Form", "Tags"))
        self.allow_radio.setToolTip(_translate("Form",
                                               "<html><head/><body><p align=\"center\">Only the posts which contain above tags will be considered by the program.</p></body></html>"))
        self.allow_radio.setText(_translate("Form", "A&llow above tags only"))
        self.skip_radio.setToolTip(_translate("Form",
                                              "<html><head/><body><p>Posts containing above tags will be skipped. All other posts will be considered.</p></body></html>"))
        self.skip_radio.setText(_translate("Form", "S&kip above tags only"))
