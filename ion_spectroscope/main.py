import logging
import array
from PyQt4 import QtCore, QtGui
from Ui_MainWindow import v7_export as spectro_gui
from tiepie_hs5 import SpectroscopeManager

from board_values import resistors

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
        self.customize_right_plot()
        self.populate_combo_boxes()
        self.init_checkboxes()
        self.init_buttons()
        # create a empty array buffer for extending 
        self.plot1_buffer = array.array('f', [])

    def customize_left_plot(self):
        self.plot_left.showGrid(True, True)
        self.plot_left.setTitle('Left is not left ?')
        # this returns one instance of a graph plotted in left_plot
        self.graph_l0 = self.plot_left.plot()

    def customize_right_plot(self):
        self.plot_right.showGrid(True, True)
        self.plot_right.setTitle('Left is not RIGHT? ?')
        # this returns one instance of a graph plotted in left_plot
        self.graph_l0 = self.plot_right.plot()

    def handle_value_updated(self, value):  # you must pass value
        # plot method takes in lists!
        # fixme: a hardcoded value index should be removed
        self.plot1_buffer.extend(value[0])
        self.graph_l0.setData(self.plot1_buffer)
        print(value)
        # essential line for updating
        QtGui.qApp.processEvents()  # force complete redraw for every plot

    def populate_combo_boxes(self):
        # todo: add an argument which is list of lists and auto populate this
        self.populate_dif_amp()
        self.populate_pos_amp()
        self.populate_neg_amp()

        self.populate_gain(values=resistors['labels'])
        self.populate_pos_input()
        self.populate_neg_input()

        self.populate_control()
        self.populate_measrate()
        self.populate_ref_channel()

        self.populate_c1_range()
        self.populate_c1_coupling()
        self.populate_c2_range()
        self.populate_c2_coupling()
        self.populate_c3_range()
        self.populate_c3_coupling()
        self.populate_c4_range()
        self.populate_c4_coupling()

    def init_checkboxes(self):
        # attach checkbox handlers
        self.tbox_u1.stateChanged.connect(self.action_u1_ticked)
        self.tbox_u2.stateChanged.connect(self.action_u2_ticked)
        self.tbox_u3.stateChanged.connect(self.action_u3_ticked)
        self.tbox_u4.stateChanged.connect(self.action_u4_ticked)

        self.tbox_cont.stateChanged.connect(self.action_cont_ticked)

    def init_buttons(self):
        self.but_start.clicked.connect(self.action_start_clicked)

        # COMBOBOX HANDLER SECTION

    def populate_dif_amp(self, values=("ON", "OFF")):
        self.cbox_dif_amp.addItems(values)
        self.cbox_dif_amp.currentIndexChanged.connect(self.action_dif_amp)

    def action_dif_amp(self, index):
        logger.debug('action_dif_amp: {}'.format(index))

    def populate_pos_amp(self, values=("ON", "OFF")):
        self.cbox_pos_amp.addItems(values)
        self.cbox_pos_amp.currentIndexChanged.connect(self.action_pos_amp)

    def action_pos_amp(self, index):
        logger.debug('action_pos_amp: {}'.format(index))

    def populate_neg_amp(self, values=("ON", "OFF")):
        self.cbox_neg_amp.addItems(values)
        self.cbox_neg_amp.currentIndexChanged.connect(self.action_neg_amp)

    def action_neg_amp(self, index):
        logger.debug('action_neg_amp: {}'.format(index))

    def populate_gain(self, values=("K = 6.8", "K=99.99")):
        self.cbox_gain.addItems(values)
        self.cbox_gain.currentIndexChanged.connect(self.action_gain)

    def action_gain(self, index):
        logger.debug('action_gain: {}'.format(index))

    def populate_pos_input(self, values=("GND", "XXX")):
        self.cbox_pos_input.addItems(values)
        self.cbox_pos_input.currentIndexChanged.connect(self.action_pos_input)

    def action_pos_input(self, index):
        logger.debug('action_pos_input: {}'.format(index))

    def populate_neg_input(self, values=("GND", "YYY")):
        self.cbox_neg_input.addItems(values)
        self.cbox_neg_input.currentIndexChanged.connect(self.action_neg_input)

    def action_neg_input(self, index):
        logger.debug('action_neg_input: {}'.format(index))

    def populate_control(self, values=("Appl.", "JJJ")):
        self.cbox_control.addItems(values)
        self.cbox_control.currentIndexChanged.connect(self.action_control)

    def action_control(self, index):
        logger.debug('action_control: {}'.format(index))

    def populate_measrate(self, values=("Fast", "JJJ")):
        self.cbox_measrate.addItems(values)
        self.cbox_measrate.currentIndexChanged.connect(self.action_measrate)

    def action_measrate(self, index):
        logger.debug('action_measrate: {}'.format(index))

    def populate_ref_channel(self, values=("Ch4", "JJJ")):
        self.cbox_ref_channel.addItems(values)
        self.cbox_ref_channel.currentIndexChanged.connect(self.action_ref_channel)

    def action_ref_channel(self, index):
        logger.debug('action_ref_channel: {}'.format(index))

    def populate_c1_range(self, values=("0.2", "JJJ")):
        self.cbox_c1_range.addItems(values)
        self.cbox_c1_range.currentIndexChanged.connect(self.action_c1_range)

    def action_c1_range(self, index):
        logger.debug('action_c1_range: {}'.format(index))

    def populate_c1_coupling(self, values=("ACV", "JJJ")):
        self.cbox_c1_coupling.addItems(values)
        self.cbox_c1_coupling.currentIndexChanged.connect(self.action_c1_coupling)

    def action_c1_coupling(self, index):
        logger.debug('action_c1_coupling: {}'.format(index))

    def populate_c2_range(self, values=("0.2", "JJJ")):
        self.cbox_c2_range.addItems(values)
        self.cbox_c2_range.currentIndexChanged.connect(self.action_c2_range)

    def action_c2_range(self, index):
        logger.debug('action_c2_range: {}'.format(index))

    def populate_c2_coupling(self, values=("ACV", "JJJ")):
        self.cbox_c2_coupling.addItems(values)
        self.cbox_c2_coupling.currentIndexChanged.connect(self.action_c2_coupling)

    def action_c2_coupling(self, index):
        logger.debug('action_c2_coupling: {}'.format(index))

    def populate_c3_range(self, values=("0.2", "JJJ")):
        self.cbox_c3_range.addItems(values)
        self.cbox_c3_range.currentIndexChanged.connect(self.action_c3_range)

    def action_c3_range(self, index):
        logger.debug('action_c3_range: {}'.format(index))

    def populate_c3_coupling(self, values=("ACV", "JJJ")):
        self.cbox_c3_coupling.addItems(values)
        self.cbox_c3_coupling.currentIndexChanged.connect(self.action_c3_coupling)

    def action_c3_coupling(self, index):
        logger.debug('action_c3_coupling: {}'.format(index))

    def populate_c4_range(self, values=("0.2", "JJJ")):
        self.cbox_c4_range.addItems(values)
        self.cbox_c4_range.currentIndexChanged.connect(self.action_c4_range)

    def action_c4_range(self, index):
        logger.debug('action_c4_range: {}'.format(index))

    def populate_c4_coupling(self, values=("ACV", "JJJ")):
        self.cbox_c4_coupling.addItems(values)
        self.cbox_c4_coupling.currentIndexChanged.connect(self.action_c4_coupling)

    def action_c4_coupling(self, index):
        logger.debug('action_c4_coupling: {}'.format(index))

        # CHECKBOX EVENTS

    def action_c1_ticked(self, state):
        logger.debug('action_c1_ticked: {}'.format(state))

        if state == QtCore.Qt.Checked:
            logger.debug('c1 has been checked: {}'.format(state))

        else:
            logger.debug('c1 has been un-checked: {}'.format(state))

    def action_u1_ticked(self, state):
        logger.debug('action_u1_ticked: {}'.format(state))

        if state == QtCore.Qt.Checked:
            logger.debug('been checked: {}'.format(state))

        else:
            logger.debug('been un-checked: {}'.format(state))

    def action_u2_ticked(self, state):
        logger.debug('action_u2_ticked: {}'.format(state))

        if state == QtCore.Qt.Checked:
            logger.debug('been checked: {}'.format(state))

        else:
            logger.debug('been un-checked: {}'.format(state))

    def action_u3_ticked(self, state):
        logger.debug('action_u3_ticked: {}'.format(state))

        if state == QtCore.Qt.Checked:
            logger.debug('been checked: {}'.format(state))

        else:
            logger.debug('been un-checked: {}'.format(state))

    def action_u4_ticked(self, state):
        logger.debug('action_u4_ticked: {}'.format(state))

        if state == QtCore.Qt.Checked:
            logger.debug('been checked: {}'.format(state))

        else:
            logger.debug('been un-checked: {}'.format(state))

    def action_cont_ticked(self, state):
        logger.debug('action_cont_ticked: {}'.format(state))

        if state == QtCore.Qt.Checked:
            logger.debug('been checked: {}'.format(state))

        else:
            logger.debug('been un-checked: {}'.format(state))

    def action_start_clicked(self, state):
        logger.debug('action_start_clicked: {}'.format(state))


if __name__ == "__main__":
    import sys

    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s - %(levelname)s - %(message)s')
    logger.debug('Running as main')

    app = QtGui.QApplication(sys.argv)
    app.setStyle(QtGui.QStyleFactory.create("Windows"))
    window = MainWindow()
    window.show()
    logger.debug('Style: {}'.format(window.style().objectName()))

    # adding osciloscope instance

    # scopes = SpectroscopeManager(init_gen=True)
    # # attaching a handler
    # scopes.set_new_data_handler(window.handle_value_updated)
    # logger.info('Setting up generator')
    # scopes.setup_generator(900, 7)
    # logger.info('Starting generator')
    # scopes.start_generator()
    # logger.info('starting block measurment')
    # scopes.setup_block_measurment(1000, 50, [[0, 8]], info=True)
    # scopes.do_block_measurment(400)
    # scopes.stop_everything()

    # this line is not executed
    sys.exit(app.exec_())
