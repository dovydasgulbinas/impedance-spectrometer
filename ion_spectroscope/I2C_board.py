import logging
import smbus

logger = logging.getLogger('i2c_board')


class BoardController:
    def __init__(self, smbus_port=1, address=0x20, reg=0x00):
        self.bus = smbus.SMBus(smbus_port)
        self.address = address
        self.reg = reg
        self.n_resistors_hf = 6
        self.n_resistors_lf = 5
        self.n_filters = 4

        self.resistors = self._resistors()

        # setting resistor registers
        self.res_reg_hf = int('00000001', 2)  # register of resistor A in High Frequency mode
        self.res_reg_hf_index = [
            int('00000001', 2),  # 0
            int('00000010', 2),
            int('00000100', 2),
            int('00001000', 2),  # 3
            int('00010000', 2),
            int('00000000', 2),  # TODO: Test me out properly #5
        ]  # sequential index of resistor registers that activate correspondingly

        self.filters = [
            int('01010000', 2),
            int('01000000', 2),
            int('00010000', 2),
            None
        ]

        self.calibration_registers = {
            "calibrate_hf": int('10000000', 2),
            "calibrate_lf": int('10000000', 2),  # FIXME: calib registers overlap
        }
        self.measurement_registers = {
            "measure_lf_rega": int('00000100', 2),
            "measure_lf_regb": int('10000000', 2),

            "measure_hf_rega": int('00000100', 2),
            "measure_hf_regb": int('00000000', 2),  # FIXME: Missing regb value
        }

        self.attenuator_registers = {
            "turn_on": int('00100000', 2),
            "turn_off": int('00000000', 2),

        }
        self.gain_registers = {
            "gain=6.8": int('00001000', 2),
            "gain=1.7": int('00000000', 2),  # fixme: find the right gain register value
        }
        self._resistors()

    def _resistors(self):
        """This method should only be called once in the constructor."""

        r = {
            "register_pairs": [[], [], [], [], [], [], [], [], [], [], []],
            "real_value": [250, 1e3, 4e3, 1.6e4, 64e3, 250e3, 1e6, 4e6, 16e6, 64e6, 240e6],
            "complex_value": [250,1e3, 4e3, 1.6e4, 64e3, 250e3, 1e6, 4e6, 16e6, 64e6, 240e6],
            "labels": ['250  om ', '1,00 kom', '4,00 kom', '16,0 kom', '64,0 kom', '256  kom', '1,00 Mom', '4,00 Mom', '16,0 Mom' ,  '64,0 Mom', '256  Mom'],
            "max_frequency": [2.2e6, 2.2e6, 2.2e6, 2.2e6, .512e6, .128e6, 32e3, 8e3, 2e3, 500, 125],
            "hf_resistor_range": range(0, 6),
            "lf_resistor_range": range(6, 11),
        }
        return r



    def read_registers(self):
        regs = self.bus.read_i2c_block_data(self.address, self.reg)
        logger.info('Red back reg. value: {}'.format(regs))

    def print_bytes(self, byte1, byte2, tag):
        logger.debug(
            '{} resistor writen values: B1 {} | B2 {}'.format(tag, byte1, byte2))

    def control_resistor_hf(self, resistor_id, read_registers=True):
       """Takes in parameters and turns on a chosen resistor.
       :param resistor_id: turns on hf resistor in range [0-5]
       :param read_registers:  optional methods for checking if register value changed
       :return: void
       """

       if resistor_id in range(0, self.n_resistors_hf):

            if resistor_id < self.n_resistors_hf - 2:  # 6 - 2 = 4
                self.print_bytes(self.res_reg_hf, self.res_reg_hf_index[resistor_id], 'HF')
                self.bus.write_i2c_block_data(
                    self.address, self.reg, [self.res_reg_hf, self.res_reg_hf_index[resistor_id]])

            # last resistor is addressed differently
            elif resistor_id == self.n_resistors_hf - 1:
                self.print_bytes(self.res_reg_hf, 'None', 'HF')
                self.bus.write_i2c_block_data(
                    self.address, self.reg, [self.res_reg_hf])

            if read_registers:
                self.read_registers()
        else:
            raise IndexError('You chose resistor that is not in range!')

    def control_resistor_lf(self, resistor_id, read_registers=True):
        """Takes in parameters and turns on a chosen resistor.
         :param resistor_id: turns on lf resistor in range [0-4]
         :param read_registers:  optional methods for checking if register value changed
         :return: void
         """

        if resistor_id in range(0, self.n_resistors_lf):

            if resistor_id == 0:
                areg = int('00000001', 2)
                breg = int('00001000', 2)
                self.print_bytes(areg, breg, 'LF')
                self.bus.write_i2c_block_data(self.address, self.reg, [areg, breg])
            elif resistor_id == 1:
                areg = int('00000010', 2)
                breg = int('00001000', 2)
                self.print_bytes(areg, breg, 'LF')
                self.bus.write_i2c_block_data(self.address, self.reg, [areg, breg])
            elif resistor_id == 2:  # FIXME: Issue is most likely to be here
                breg = int('01001000', 2)
                self.print_bytes('None', breg, 'LF')
                self.bus.write_i2c_block_data(self.address, self.reg, [breg])
            elif resistor_id == 3:  # FIXME: ERROR? because match with above?
                breg = int('01001000', 2)
                self.print_bytes('None', breg, 'LF')
                self.bus.write_i2c_block_data(self.address, self.reg, [breg])
            elif resistor_id == 4:
                breg = int('00001000', 2)
                self.print_bytes('None', breg, 'LF')
                self.bus.write_i2c_block_data(self.address, self.reg, [breg])

            if read_registers:
                self.read_registers()
        else:
            raise IndexError('You chose resistor that is not in range!')

    def control_filter(self, filter_id, read_registers=True):
        logger.debug('in control_filter, filter_id {}'.format(filter_id))

        if filter_id in range(0, self.n_filters):

            if filter_id < self.n_filters - 2:
                filter_reg = self.filters[filter_id]
                self.print_bytes(filter_reg, 'None', 'FILTER |')
                self.bus.write_i2c_block_data(self.address, self.reg, [filter_reg])

            elif filter_id == self.n_filters - 1:
                self.print_bytes('None', 'None', 'FILTER |')

        if read_registers:
            self.read_registers()
        else:
            raise IndexError('You chose filter that is not in range!')

    def enter_calibration_mode_hf(self, read_registers=True):
        logger.debug('in enter_calibration_mode_hf')
        self.bus.write_i2c_block_data(self.address, self.reg, [self.calibration_registers["calibrate_hf"]])

        if read_registers:
            self.read_registers()

    def enter_calibration_mode_lf(self, read_registers=True):
        logger.debug('in enter_calibration_mode_lf')
        self.bus.write_i2c_block_data(self.address, self.reg, [self.calibration_registers["calibrate_lf"]])

        if read_registers:
            self.read_registers()

    def enter_measurement_mode_hf(self, read_registers):
        logger.debug('in enter_measurement_mode_hf')
        rega = self.measurement_registers["measure_hf_rega"]
        regb = self.measurement_registers["measure_hf_regb"]  # FIXME: Make sure its called propery
        self.bus.write_i2c_block_data(self.address, self.reg, [rega, regb])

        if read_registers:
            self.read_registers()

    def enter_measurement_mode_lf(self, read_registers):
        logger.debug('in enter_measurement_mode_lf')
        rega = self.measurement_registers["measure_lf_rega"]
        regb = self.measurement_registers["measure_lf_regb"]
        self.bus.write_i2c_block_data(self.address, self.reg, [rega, regb])

        if read_registers:
            self.read_registers()

    def turn_attenuator_on(self, read_registers=True):
        logger.debug('in turn attenuator_on')
        on = self.attenuator_registers["turn_on"]
        self.bus.write_i2c_block_data(self.address, self.reg, [on])

        if read_registers:
            self.read_registers()

    def turn_attenuator_off(self, read_registers=True):
        logger.debug('in turn attenuator_off')
        off = self.attenuator_registers["turn_off"]
        self.bus.write_i2c_block_data(self.address, self.reg, [off])

        if read_registers:
            self.read_registers()

    def set_gain_to17(self, read_registers=True):
        logger.debug('in set_gain_to17')
        gain = self.gain_registers["gain=1.7"]  # fixme: will not work probably
        self.bus.write_i2c_block_data(self.address, self.reg, [gain])

        if read_registers:
            self.read_registers()

    def set_gain_to68(self, read_registers=True):
        logger.debug('in set_gain_to68')
        gain = self.gain_registers["gain=6.8"]
        self.bus.write_i2c_block_data(self.address, self.reg, [gain])

        if read_registers:
            self.read_registers()


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
    logger.debug('Running as main')
    import time
    bc = BoardController()

    for i in range(0, 6):
        bc.control_resistor_hf(i)
        time.sleep(1)