# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wid_embed.ui'
#
# Created: Sun Nov 13 00:37:38 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import pyqtgraph as pg

# here we use our plot widget
# plot = pg.PlotWidget()


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
    def __init__(self, plot_wid):
        self.plot_wid = plot_wid

    @property
    def plot_wid(self):
        return self._plot_wid

    @plot_wid.setter
    def plot_wid(self, plot):
        if not plot: ValueError("Widget object is None")
        self._plot_wid = plot

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.container_wid = QtGui.QWidget(MainWindow)
        self.container_wid.setObjectName(_fromUtf8("container_wid"))
        self.gridLayout = QtGui.QGridLayout(self.container_wid)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))


        # we must override this widget
        # --
        # self.plot_wid = QtGui.QWidget(self.container_wid)
        # self.plot_wid =
        # --
        self.plot_wid.setObjectName(_fromUtf8("plot_wid"))
        self.gridLayout.addWidget(self.plot_wid, 0, 0, 1, 1)


        self.plot_btn = QtGui.QPushButton(self.container_wid)
        self.plot_btn.setObjectName(_fromUtf8("plot_btn"))
        self.gridLayout.addWidget(self.plot_btn, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.container_wid)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuSystem = QtGui.QMenu(self.menubar)
        self.menuSystem.setObjectName(_fromUtf8("menuSystem"))
        self.menuTools = QtGui.QMenu(self.menubar)
        self.menuTools.setObjectName(_fromUtf8("menuTools"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSystem.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.plot_btn.setText(_translate("MainWindow", "PushButton", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuSystem.setTitle(_translate("MainWindow", "System", None))
        self.menuTools.setTitle(_translate("MainWindow", "Tools", None))


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()

    # We pass an object of plot widget to our class
    ui = Ui_MainWindow(pg.PlotWidget())


    ui.setupUi(MainWindow)
    MainWindow.show()
    print("Im running?")
    # -- Customization starts here:

    # acessing grid attributes here!
    ui.plot_wid.showGrid(True, True)
    # --





    sys.exit(app.exec_())

