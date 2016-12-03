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

        # setting resistor registers
        self.res_reg_hf = int('00000001', 2)  # register of resistor A in High Frequency mode
        self.res_reg_hf_index = [
            int('00000001', 2),  # 0
            int('00000010', 2),
            int('00000100', 2),
            int('00001000', 2),  # 3
            int('00010000', 2),
            int('00000000', 2),  # TODO: Test me out properly #5
        ]  # sequential index of resistor registers that activate correspondinglyi

        self.filters = [
            int('01010000', 2),
            int('01000000', 2),
            int('00010000', 2),
            None
        ]

        self.calibration_registers = {
            "calibrate_hf": int('10000000', 2),
            "calibrate_lf": int('10000000', 2), # FIXME: calib registers overlap
        }
        self.measurement_registers = {
            "measure_lf_rega": int('00000100', 2),
            "measure_lf_regb": int('10000000', 2),

            "measure_hf_rega": int('00000100', 2),
            "measure_hf_regb": int('00000000', 2), # FIXME: Missing regb value
        }

        self.attenuator_registers = {
            "turn_on": int('00100000', 2),
            "turn_off": int('00000000', 2),

        }

    def read_registers(self):
        regs = bus.read_i2c_block_data(self.address, self.reg)
        logger.info('Red back reg. value: {}'.format(regs))

    def print_bytes(self, byte1, byte2, tag):
        logger.debug(
            '{} resistor writen values: B1 {} | B2 {}'.format(tag, byte1, byte2))

    def control_resistor_hf(self, resistor_id, read_registers=True):
        """Takes in parameters and turns on a chosen resistor.
        :param resistor_id: integer, [0-5] for chosing a resistor
        :return:
        """

        if resistor_id in range(0, self.n_resistors_hf):

            if resistor_id < self.n_resistors_hf - 2:  # 6 - 2 = 4
                self.print_bytes(self.res_reg_hf, self.res_reg_hf_index[resistor_id], 'HF')
                bus.write_i2c_block_data(
                    self.address, self.reg, [self.res_reg_hf, self.res_reg_hf_index[resistor_id]])

            # last resistor is addressed differently
            elif resistor_id == self.n_resistors_hf - 1:
                self.print_bytes(self.res_reg_hf, 'None', 'HF')
                bus.write_i2c_block_data(
                    self.address, self.reg, [self.res_reg_hf])

            if read_registers:
                self.read_registers()
        else:
            raise IndexError('You chose resistor that is not in range!')

    def control_resistor_lf(self, resistor_id, read_registers=True):
        """

        :param resistor_id:
        :param read_registers:
        :return:
        """

        if resistor_id in range(0, self.n_resistors_lf):

            if resistor_id == 6:
                areg = int('00000001', 2)
                breg = int('00001000', 2)
                self.print_bytes(areg,breg,'LF')
                bus.write_i2c_block_data(self.address, self.reg, [areg, breg])
            elif resistor_id == 7:
                areg = int('00000010', 2)
                breg = int('00001000', 2)
                self.print_bytes(areg,breg,'LF')
                bus.write_i2c_block_data(self.address, self.reg, [areg, breg])
            elif resistor_id == 8: # FIXME: Issue is most likely to be here
                breg = int('01001000', 2)
                self.print_bytes('None', breg, 'LF')
                bus.write_i2c_block_data(self.address, self.reg, [breg])
            elif resistor_id == 9: # FIXME: ERROR? because match with above?
                breg = int('01001000', 2)
                self.print_bytes('None', breg, 'LF')
                bus.write_i2c_block_data(self.address, self.reg, [breg])
            elif resistor_id == 10:
                breg = int('00001000', 2)
                self.print_bytes('None', breg, 'LF')
                bus.write_i2c_block_data(self.address, self.reg, [breg])

            if read_registers:
                self.read_registers()
        else:
            raise IndexError('You chose resistor that is not in range!')

    def control_filter(self, filter_id, read_registers=True):
        logger.debug('in control_filter, filter_id {}'.format(filter_id))

        if filter_id in range(0, self.n_filters):

            if filter_id < self.n_filters -2:
                filter_reg = self.filters[filter_id]
                self.print_bytes(filter_reg, 'None', 'FILTER |')
                bus.write_i2c_block_data(self.address, self.reg, [filter_reg])

            elif filter_id == self.n_filters - 1:
                self.print_bytes('None', 'None', 'FILTER |')

        if read_registers:
            self.read_registers()
        else:
            raise IndexError('You chose filter that is not in range!')

    def enter_calibration_mode_hf(self, read_registers=True):
        logger.debug('in enter_calibration_mode_hf')
        bus.write_i2c_block_data(self.address, self.reg, [self.calibration_registers["calibrate_hf"]])

        if read_registers:
            self.read_registers()

    def enter_calibration_mode_lf(self, read_registers=True):
        logger.debug('in enter_calibration_mode_lf')
        bus.write_i2c_block_data(self.address, self.reg, [self.calibration_registers["calibrate_lf"]])

        if read_registers:
            self.read_registers()

    def enter_measurement_mode_hf(self, read_registers):
        logger.debug('in enter_measurement_mode_hf')
        rega = self.measurement_registers["measure_hf_rega"]
        regb = self.measurement_registers["measure_hf_regb"]  # FIXME: Make sure its called propery
        bus.write_i2c_block_data(self.address, self.reg, [rega, regb])

        if read_registers:
            self.read_registers()

    def enter_measurement_mode_lf(self, read_registers):
        logger.debug('in enter_measurement_mode_lf')
        rega = self.measurement_registers["measure_lf_rega"]
        regb = self.measurement_registers["measure_lf_regb"]
        bus.write_i2c_block_data(self.address, self.reg, [rega, regb])

        if read_registers:
            self.read_registers()

    def turn_attenuator_on(self, read_registers=True):
        logger.debug('in turn attenuator_on')
        on = self.attenuator_registers["turn_on"]
        bus.write_i2c_block_data(self.address, self.reg, [on])

        if read_registers:
            self.read_registers()

    def turn_attenuator_off(self, read_registers=True):
        logger.debug('in turn attenuator_off')
        off = self.attenuator_registers["turn_off"]
        bus.write_i2c_block_data(self.address, self.reg, [off])

        if read_registers:
            self.read_registers()




# Gain

def gain():
    gain = raw_input("Pasirinkite gain veikimo rezima (1.7/6.8): ")
    if gain == "6.8":
        regA = int('00001000', 2)
        bus.write_i2c_block_data(address, reg, [regA])
        print
        "Registro ID: " + str(bus.read_i2c_block_data(address, reg))
        print
        "regA: " + str(regA)
        print
        "Pasirinkote %r gain veikimo rezima. " % gain
    elif gain == "1.7":
        print
        "regA bit is not set for 1.7"
        print
        "Pasirinkote %r gain veikimo rezima. " % gain
    else:
        print
        "IVConverter: Invalid gain specified. Value was not modified. "


# Properties

resistor()  # Resistors, ranging from 1 to 11. Also determines range variable.
filtras()  # Filters, ranging from 1 to 4.
# setrange()             # Range is determined by the chosen resistor.
mode()  # 'MEAS' for measurement and 'CAL' for calibration modes.
attenuator()  # Signal, coming from the generator, can be attenuated. Variable is either 'ON' or 'OFF'.
gain()  # Available gains after I-V conversion are 1.7 and 6.8.

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
    logger.debug('Running as main')

    bc = BoardController()
