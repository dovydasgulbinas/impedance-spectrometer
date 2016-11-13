from PyQt4 import QtCore, QtGui
from base_gui import Ui_MainWindow
from basic_iterator import SineIterable


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
        si = SineIterable(0, 200)
        for i in range(0,2):
            self.value_updated.emit(list(si))

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
        # plot method takes in lists!
        self.plot_left.plot().setData(value)
        print(value)
        # essential line for updating
        QtGui.qApp.processEvents() # force complete redraw for every plot


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.data_signals.value_generator()
    # this line is not executed
    sys.exit(app.exec_())

