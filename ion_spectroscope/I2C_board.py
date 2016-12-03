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

    def read_registers(self):
        regs = bus.read_i2c_block_data(self.address, self.reg)
        logger.info('Red back reg. value: {}'.format(regs))

    def print_bytes(self, byte1, byte2, tag):
        logger.debug(
            '{} resistor writen values: B1 {} | B2 {}'.format(tag, byte1, byte2))

    def address_resistor_hf(self, resistor_id, read_registers=True):
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

    def address_resistor_lf(self, resistor_id, read_registers=True):
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
            elif resistor_id == 9:
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






        # Rezistoriai





# Filtrai

def filtras():
    filtras = raw_input("Pasirinkite filtra (1-4): ")
    if filtras == "1":
        regA = int('01010000', 2)
        bus.write_i2c_block_data(address, reg, [regA])
        print
        "Registro ID : " + str(bus.read_i2c_block_data(address, reg))
        print
        "regA: " + str(regA)
        print
        "Pasirinkote %r filtra. " % filtras
    elif filtras == "2":
        regA = int('01000000', 2)
        bus.write_i2c_block_data(address, reg, [regA])
        print
        "Registro ID: " + str(bus.read_i2c_block_data(address, reg))
        print
        "regA: " + str(regA)
        print
        "Pasirinkote %r filtra. " % filtras
    elif filtras == "3":
        regA = int('00010000', 2)
        bus.write_i2c_block_data(address, reg, [regA])
        print
        "Registro ID: " + str(bus.read_i2c_block_data(address, reg))
        print
        "regA: " + str(regA)
        print
        "Pasirinkote %r filtra. " % filtras
    elif filtras == "4":
        print
        "no bits set for position 4. "
        print
        "Pasirinkote %r filtra. " % filtras
    else:
        print
        "IVConverter: Invalid filter index specified. Value was not modified. "


# Matavimas/ Kalibravimas

def mode():
    mode = raw_input("Pasirinkite veikimo rezima (MEAS/CAL): ")
    if mode == "MEAS":
        MEAS = raw_input("Pasirinkite dazniu intervala (LF, HF): ")
        if MEAS == "LF":
            regA = int('00000100', 2)
            regB = int('10000000', 2)
            bus.write_i2c_block_data(address, reg, [regA, regB])
            print
            "Registro ID: " + str(bus.read_i2c_block_data(address, reg))
            print
            "regB: " + str(regB), "regA: " + str(regA)
            print
            "Pasirinkote matavimo rezima veikianti %r dazniu intervale. " % MEAS

        elif MEAS == "HF":
            regA = int('10000100', 2)
            bus.write_i2c_block_data(address, reg, [regA, regB])
            print
            "Registro ID: " + str(bus.read_i2c_block_data(address, reg))
            print
            "regA: " + str(regA)
            print
            "Pasirinkote matavimo rezima veikianti %r dazniu intervale. " % MEAS
        else:
            print
            "IVConverter: Range can only be 'HF' or 'LF'. Value was not modified. "

    elif mode == "CAL":
        CAL = raw_input("Pasirinkite dazniu intervala (LF, HF): ")
        if CAL == "LF":
            regB = int('10000000', 2)
            bus.write_i2c_block_data(address, reg, [regB])
            print
            "Registro ID: " + str(bus.read_i2c_block_data(address, reg))
            print
            "regB: " + str(regB)
            print
            "Pasirinkote kalibravimo rezima veikianti %r dazniu intervale. " % CAL

        elif CAL == "HF":
            regA = int('10000000', 2)
            bus.write_i2c_block_data(address, reg, [regA])
            print
            "Registro ID: " + str(bus.read_i2c_block_data(address, reg))
            print
            "regA: " + str(regA)
            print
            "regB bits are not set for HF measurement"
            print
            "Pasirinkote kalibravimo rezima veikianti %r dazniu intervale. " % CAL
        else:
            print
            "IVConverter: Range can only be 'HF' or 'LF'. Value was not modified. "
    else:
        print
        "IVConverter: Mode can only be 'CAL' or 'MEAS'. Value was not modified. "


# Ateniuatorius

def attenuator():
    attenuator = raw_input("Pasirinkite ateniuatoriaus veikimo rezima (ON/OFF): ")
    if attenuator == "ON":
        regA = int('00100000', 2)
        bus.write_i2c_block_data(address, reg, [regA])
        print
        "Registro ID: " + str(bus.read_i2c_block_data(address, reg))
        print
        "regA: " + str(regA)
        print
        "Pasirinkote %r ateniuatoriaus veikimo rezima" % attenuator
    elif attenuator == "OFF":
        print
        "bit is not set for 'OFF'"
        print
        "Pasirinkote %r ateniuatoriaus veikimo rezima" % attenuator
    else:
        print
        "IVConverter: Attenuator can only be 'ON' or 'OFF'. Value was not modified. "


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
