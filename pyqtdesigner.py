# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyqtdesigner.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication






class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(565, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.main_cb = QtWidgets.QCheckBox(self.centralwidget)
        self.main_cb.setObjectName("main_cb")
        self.gridLayout.addWidget(self.main_cb, 2, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 2, 1, 1)
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setObjectName("toolButton")
        self.gridLayout.addWidget(self.toolButton, 0, 0, 1, 1)
        self.push_BT = QtWidgets.QPushButton(self.centralwidget)
        self.push_BT.setObjectName("push_BT")
        self.gridLayout.addWidget(self.push_BT, 3, 0, 1, 1)
        self.hit_BT = QtWidgets.QPushButton(self.centralwidget)
        self.hit_BT.setObjectName("hit_BT")
        self.gridLayout.addWidget(self.hit_BT, 3, 1, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 565, 27))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuKill = QtWidgets.QMenu(self.menubar)
        self.menuKill.setObjectName("menuKill")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionCyka = QtWidgets.QAction(MainWindow)
        self.actionCyka.setObjectName("actionCyka")
        self.actionKebab = QtWidgets.QAction(MainWindow)
        self.actionKebab.setObjectName("actionKebab")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionFile = QtWidgets.QAction(MainWindow)
        self.actionFile.setObjectName("actionFile")
        self.actionSuck = QtWidgets.QAction(MainWindow)
        self.actionSuck.setObjectName("actionSuck")
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionCyka)
        self.menuFile.addAction(self.actionKebab)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionFile)
        self.menuKill.addAction(self.actionSuck)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuKill.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.main_cb.setText(_translate("MainWindow", "Check me Out"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.push_BT.setText(_translate("MainWindow", "Click ME"))

        # TODO: Check this event attachment
        self.push_BT.clicked.connect(self.print_kyca)


        self.hit_BT.setText(_translate("MainWindow", "Hit ME"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuKill.setTitle(_translate("MainWindow", "Kill"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionCyka.setText(_translate("MainWindow", "Cyka"))
        self.actionKebab.setText(_translate("MainWindow", "Kebab"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionFile.setText(_translate("MainWindow", "File"))
        self.actionSuck.setText(_translate("MainWindow", "Suck"))

    def print_kyca(self):
        print("Americaaaa fuck yeah!")

app = QApplication(sys.argv)
print("HELLO")
ex = Ui_MainWindow()
ex.print_kyca()
ex.show()
sys.exit(app.exec_())

