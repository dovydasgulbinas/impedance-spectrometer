from PyQt4 import QtCore, QtGui
from base_gui import Ui_MainWindow
from pyqtgraph import PlotWidget


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

class DataSignals(QtCore.QObject):
    """All data that must be processed in real time and updated is added here"""
    value_updated = QtCore.pyqtSignal(int)

    def value_generator(self):
        for i in range(10000):
            # will generate event that will passed
            self.value_updated.emit(i)

class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        # Since MainWindow class is inherited you must pass self
        self.setupUi(self)
        self.customize_left_plot()
        # -- Data refresh configuration
        # Must use self!
        self.data_signals = DataSignals(self)
        self.data_signals.value_updated.connect(self.handle_value_updated)

    def customize_left_plot(self):
        self.plot_left.showGrid(True, True)
        self.plot_left.setTitle('Left is not left ?')

    def handle_value_updated(self, value):
        self.plot_left.setTitle(str(value))
        print(value)
        # essential line for updating
        QtGui.qApp.processEvents()


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()

    window.data_signals.value_generator()

    sys.exit(app.exec_())