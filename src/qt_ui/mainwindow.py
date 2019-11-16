# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(564, 524)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(1000, 605))
        MainWindow.setStyleSheet("background-color:#cccccc")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.navigation = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.navigation.sizePolicy().hasHeightForWidth())
        self.navigation.setSizePolicy(sizePolicy)
        self.navigation.setMinimumSize(QtCore.QSize(180, 0))
        self.navigation.setStyleSheet("background-color:#aaaaaa")
        self.navigation.setObjectName("navigation")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.navigation)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.like = QtWidgets.QPushButton(self.navigation)
        self.like.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.like.setFont(font)
        self.like.setFocusPolicy(QtCore.Qt.NoFocus)
        self.like.setStyleSheet("border:none;background-color:#F65F5F")
        self.like.setObjectName("like")
        self.verticalLayout.addWidget(self.like)
        self.follow = QtWidgets.QPushButton(self.navigation)
        self.follow.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.follow.setFont(font)
        self.follow.setFocusPolicy(QtCore.Qt.NoFocus)
        self.follow.setStyleSheet("border:none;background-color:#F65F5F")
        self.follow.setObjectName("follow")
        self.verticalLayout.addWidget(self.follow)
        self.comment = QtWidgets.QPushButton(self.navigation)
        self.comment.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comment.setFont(font)
        self.comment.setFocusPolicy(QtCore.Qt.NoFocus)
        self.comment.setStyleSheet("border:none;background-color:#F65F5F")
        self.comment.setObjectName("comment")
        self.verticalLayout.addWidget(self.comment)
        self.filter = QtWidgets.QPushButton(self.navigation)
        self.filter.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.filter.setFont(font)
        self.filter.setFocusPolicy(QtCore.Qt.NoFocus)
        self.filter.setStyleSheet("border:none;background-color:#0099cc")
        self.filter.setObjectName("filter")
        self.verticalLayout.addWidget(self.filter)
        self.status = QtWidgets.QPushButton(self.navigation)
        self.status.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.status.setFont(font)
        self.status.setFocusPolicy(QtCore.Qt.NoFocus)
        self.status.setStyleSheet("border:none;background-color:#0099cc")
        self.status.setObjectName("status")
        self.verticalLayout.addWidget(self.status)
        self.log = QtWidgets.QPushButton(self.navigation)
        self.log.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.log.setFont(font)
        self.log.setFocusPolicy(QtCore.Qt.NoFocus)
        self.log.setStyleSheet("border:none;background-color:#0099cc")
        self.log.setObjectName("log")
        self.verticalLayout.addWidget(self.log)
        self.logout = QtWidgets.QPushButton(self.navigation)
        self.logout.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.logout.setFont(font)
        self.logout.setFocusPolicy(QtCore.Qt.NoFocus)
        self.logout.setStyleSheet("border:none;background-color:#0099cc")
        self.logout.setObjectName("logout")
        self.verticalLayout.addWidget(self.logout)
        self.exit = QtWidgets.QPushButton(self.navigation)
        self.exit.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.exit.setFont(font)
        self.exit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.exit.setStyleSheet("border:none;background-color:#0099cc")
        self.exit.setObjectName("exit")
        self.verticalLayout.addWidget(self.exit)
        self.horizontalLayout.addWidget(self.navigation)
        self.display_area = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.display_area.sizePolicy().hasHeightForWidth())
        self.display_area.setSizePolicy(sizePolicy)
        self.display_area.setObjectName("display_area")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.display_area)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.display = QtWidgets.QStackedWidget(self.display_area)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.display.sizePolicy().hasHeightForWidth())
        self.display.setSizePolicy(sizePolicy)
        self.display.setMinimumSize(QtCore.QSize(0, 300))
        self.display.setMaximumSize(QtCore.QSize(16777215, 300))
        self.display.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.display.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.display.setObjectName("display")
        self.stackArea = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackArea.sizePolicy().hasHeightForWidth())
        self.stackArea.setSizePolicy(sizePolicy)
        self.stackArea.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.stackArea.setObjectName("stackArea")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.stackArea)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.loginArea = QtWidgets.QFrame(self.stackArea)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loginArea.sizePolicy().hasHeightForWidth())
        self.loginArea.setSizePolicy(sizePolicy)
        self.loginArea.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.loginArea.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.loginArea.setFrameShadow(QtWidgets.QFrame.Raised)
        self.loginArea.setObjectName("loginArea")
        self.gridLayout_2.addWidget(self.loginArea, 0, 0, 1, 1)
        self.display.addWidget(self.stackArea)
        self.verticalLayout_2.addWidget(self.display)
        self.groupBox = QtWidgets.QGroupBox(self.display_area)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setFocusPolicy(QtCore.Qt.NoFocus)
        self.scrollArea.setStyleSheet("background-color:#eeeeee;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.mainWidget = QtWidgets.QWidget()
        self.mainWidget.setGeometry(QtCore.QRect(0, 0, 314, 180))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainWidget.sizePolicy().hasHeightForWidth())
        self.mainWidget.setSizePolicy(sizePolicy)
        self.mainWidget.setObjectName("mainWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.mainWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.logBrowser = QtWidgets.QPlainTextEdit(self.mainWidget)
        self.logBrowser.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logBrowser.sizePolicy().hasHeightForWidth())
        self.logBrowser.setSizePolicy(sizePolicy)
        self.logBrowser.setMinimumSize(QtCore.QSize(0, 0))
        self.logBrowser.setStyleSheet("vertical-align:bottom;")
        self.logBrowser.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.logBrowser.setReadOnly(True)
        self.logBrowser.setObjectName("logBrowser")
        self.verticalLayout_3.addWidget(self.logBrowser)
        self.scrollArea.setWidget(self.mainWidget)
        self.horizontalLayout_2.addWidget(self.scrollArea)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.horizontalLayout.addWidget(self.display_area)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 564, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.exit.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.like.setText(_translate("MainWindow", "Like"))
        self.follow.setText(_translate("MainWindow", "Follow/Unfollow"))
        self.comment.setText(_translate("MainWindow", "Comment"))
        self.filter.setText(_translate("MainWindow", "Filters"))
        self.status.setText(_translate("MainWindow", "Show Status"))
        self.log.setText(_translate("MainWindow", "Show Logs"))
        self.logout.setText(_translate("MainWindow", "Log Out"))
        self.exit.setText(_translate("MainWindow", "Exit"))
        self.groupBox.setTitle(_translate("MainWindow", "Log Messages"))
