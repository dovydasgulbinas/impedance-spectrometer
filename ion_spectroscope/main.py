import logging
from PyQt4 import QtCore, QtGui
from Ui_MainWindow import spectro_gui
from tiepie_hs5 import SpectroscopeManager

logger = logging.getLogger()

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


class MainWindow(QtGui.QMainWindow, spectro_gui.Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        # Since MainWindow class is inherited you must pass self
        self.setupUi(self)
        self.customize_left_plot()

    def customize_left_plot(self):
        self.plot_left.showGrid(True, True)
        self.plot_left.setTitle('Left is not left ?')
        # this returns one instance of a graph plotted in left_plot
        self.graph_l0 = self.plot_left.plot()

    def handle_value_updated(self, value):  # you must pass value
        # plot method takes in lists!
        # fixme: a hardcoded value index should be removed
        self.graph_l0.setData(value[0])
        print(value)
        # essential line for updating
        QtGui.qApp.processEvents()  # force complete redraw for every plot


if __name__ == "__main__":
    import sys

    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
    logger.debug('Running as main')

    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()

    # adding osciloscope instance

    scopes = SpectroscopeManager(init_generator=True)
    # attaching a handler
    scopes.set_new_data_handler(window.handle_value_updated)
    logger.info('Setting up generator')
    scopes.setup_generator()
    logger.info('Starting generator')
    scopes.start_generator()
    logger.info('starting block measurment')
    scopes.setup_block_measurment(1000, 100, [[0, 8]], info=True)
    scopes.do_block_measurment(400)
    scopes.stop_everything()

    # this line is not executed
    sys.exit(app.exec_())
