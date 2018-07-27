# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Code\python\xml-validate\validator.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.xmlSchemaSelectButton = QtGui.QPushButton(self.centralwidget)
        self.xmlSchemaSelectButton.setObjectName(_fromUtf8("xmlSchemaSelectButton"))
        self.verticalLayout_2.addWidget(self.xmlSchemaSelectButton)
        self.xmlInputSelectButton = QtGui.QPushButton(self.centralwidget)
        self.xmlInputSelectButton.setObjectName(_fromUtf8("xmlInputSelectButton"))
        self.verticalLayout_2.addWidget(self.xmlInputSelectButton)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.xmlSchemaLineEdit = QtGui.QLineEdit(self.centralwidget)
        self.xmlSchemaLineEdit.setEnabled(False)
        self.xmlSchemaLineEdit.setObjectName(_fromUtf8("xmlSchemaLineEdit"))
        self.verticalLayout_3.addWidget(self.xmlSchemaLineEdit)
        self.xmlInputLineEdit = QtGui.QLineEdit(self.centralwidget)
        self.xmlInputLineEdit.setEnabled(False)
        self.xmlInputLineEdit.setObjectName(_fromUtf8("xmlInputLineEdit"))
        self.verticalLayout_3.addWidget(self.xmlInputLineEdit)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.validationOutputArea = QtGui.QPlainTextEdit(self.centralwidget)
        self.validationOutputArea.setEnabled(False)
        self.validationOutputArea.setObjectName(_fromUtf8("validationOutputArea"))
        self.verticalLayout.addWidget(self.validationOutputArea)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuValidation = QtGui.QMenu(self.menubar)
        self.menuValidation.setObjectName(_fromUtf8("menuValidation"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.fileQuitAction = QtGui.QAction(MainWindow)
        self.fileQuitAction.setObjectName(_fromUtf8("fileQuitAction"))
        self.validationValidateAction = QtGui.QAction(MainWindow)
        self.validationValidateAction.setObjectName(_fromUtf8("validationValidateAction"))
        self.validationValidateClearAction = QtGui.QAction(MainWindow)
        self.validationValidateClearAction.setObjectName(_fromUtf8("validationValidateClearAction"))
        self.menuFile.addAction(self.fileQuitAction)
        self.menuValidation.addAction(self.validationValidateAction)
        self.menuValidation.addAction(self.validationValidateClearAction)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuValidation.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.xmlSchemaSelectButton.setText(_translate("MainWindow", "XML Schema", None))
        self.xmlInputSelectButton.setText(_translate("MainWindow", "XML Input", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuValidation.setTitle(_translate("MainWindow", "Validation", None))
        self.fileQuitAction.setText(_translate("MainWindow", "Quit", None))
        self.validationValidateAction.setText(_translate("MainWindow", "Validate Document", None))
        self.validationValidateClearAction.setText(_translate("MainWindow", "Clear", None))
