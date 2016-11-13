# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'two_plot.ui'
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
        self.master_container = QtGui.QWidget(MainWindow)
        self.master_container.setObjectName(_fromUtf8("master_container"))
        self.gridLayout = QtGui.QGridLayout(self.master_container)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.plot_container = QtGui.QHBoxLayout()
        self.plot_container.setObjectName(_fromUtf8("plot_container"))
        self.plot_left = PlotWidget(self.master_container)
        self.plot_left.setObjectName(_fromUtf8("plot_left"))
        self.plot_container.addWidget(self.plot_left)
        self.plot_right = PlotWidget(self.master_container)
        self.plot_right.setObjectName(_fromUtf8("plot_right"))
        self.plot_container.addWidget(self.plot_right)
        self.gridLayout.addLayout(self.plot_container, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.groupBox_2 = QtGui.QGroupBox(self.master_container)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayout_2.addWidget(self.groupBox_2)
        self.groupBox = QtGui.QGroupBox(self.master_container)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout_2.addWidget(self.groupBox)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.master_container)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Board", None))
        self.groupBox.setTitle(_translate("MainWindow", "Oscilo", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))

from pyqtgraph import PlotWidget

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

