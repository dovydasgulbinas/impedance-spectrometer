from PyQt4 import QtCore, QtGui
from Ui_MainWindow import spectro_gui 
import random

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
    # Python specific type -- list
    value_updated = QtCore.pyqtSignal(list)

    def value_generator(self):
        # will generate event that will passed
        # it should be replace with real data stream
        # value emiter is crucial part of the code
        self.value_updated.emit([random.random(),random.random()]*5)


class MainWindow(QtGui.QMainWindow, spectro_gui.Ui_MainWindow):
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
        # this returns one instance of a graph plotted in left_plot
        self.graph_l0 = self.plot_left.plot()

    def handle_value_updated(self, value): # you must pass value
        # plot method takes in lists!
        self.graph_l0.setData(value)
        print(value)
        # essential line for updating
        QtGui.qApp.processEvents() # force complete redraw for every plot

    def temp_plot_always(self):
        # plot method takes in lists!
        self.graph_l0.setData(value)
        print(value)
        self.plot_left.setTitle(value)
        # essential line for updating
        QtGui.qApp.processEvents() # force complete redraw for every plot


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    # Implementing timed data polling
    timer = QtCore.QTimer()
    timer.timeout.connect(window.data_signals.value_generator)
    timer.start(20)
    # this line is not executed
    sys.exit(app.exec_())

