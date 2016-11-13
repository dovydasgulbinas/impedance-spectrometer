from PyQt4 import QtCore, QtGui
from base_gui import Ui_MainWindow
from pyqtgraph import PlotWidget

# boiler plate
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


class Ui_CustomisedPlots(Ui_MainWindow):
    def __init__(self):
        # initializes objects in parent class
        self.setupUi(MainWindow)
        self.customize_left_plot()

    def customize_left_plot(self):
        self.plot_left.showGrid(True, True)
        self.plot_left.setTitle('Left is not left ?')


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_CustomisedPlots()
    MainWindow.show()
    sys.exit(app.exec_())