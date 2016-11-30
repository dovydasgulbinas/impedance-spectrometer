import logging
import smbus

logger = logging.getLogger('i2c_board')


class BoardController:
    def __init__(self, smbus_port=1, address=0x20, reg=0x00):
        self.bus = smbus.SMBus(smbus_port)
        self.address = address
        self.reg = reg

        # setting resistor registers
        self.res_reg_HF = int('00000001', 2)  # register of resistor A in High Frequency mode
        self.res_reg_HF_index = [
            int('00000001', 2),
            int('00000010', 2),
            int('00000100', 2),
            int('00001000', 2)

        ]  # sequential index of resistor registers that activate correspondingly

    def address_resistor(self, resistor_id, frequency_range='LF'):
        """Takes in parameters and turns on a chosen resistor.
        :param resistor_id: integer, [1-6] for chosing a resistor
        :param frequency_range: string, two states -- LF, HF
        :return:
        """


# Rezistoriai

def resistor():
    resistor = raw_input("Pasirinkite dazniu intervala (LF, HF): ")
    if resistor == "HF":
        res = raw_input("Pasirinkite rezistoriu (1-6): ")
        if res == "1":
            regB = int('00000001', 2)
            regA = int('00000001', 2)
            bus.write_i2c_block_data(address, reg, [regA, regB])
            print
            "Registro ID: " + str(bus.read_i2c_block_data(address, reg))
            print
            "regB: " + str(regB), "regA: " + str(regA)
            print
            "Pasirinkote %r rezistoriu veikianti HF dazniu intervale. " % res
        elif res == "2":
            regB = int('00000010', 2)
            regA = int('00000001', 2)
            bus.write_i2c_block_data(address, reg, [regA, regB])
            print
            "Registro ID: " + str(bus.read_i2c_block_data(address, reg))
            print
            "regB: " + str(regB), "regA: " + str(regA)
            print
            "Pasirinkote %r rezistoriu veikianti HF dazniu intervale. " % res
        elif res == "3":
            regB = int('00000010', 2)
            regA = int('00000001', 2)
            bus.write_i2c_block_data(address, reg, [regA, regB])
            print
            "Registro ID: " + str(bus.read_i2c_block_data(address, reg))
            print
            "regB: " + str(regB), "regA: " + str(regA)
            print
            "Pasirinkote %r rezistoriu veikianti HF dazniu intervale. " % res
        elif res == "4":
            regB = int('00001000', 2)
            regA = int('00000001', 2)
            bus.write_i2c_block_data(address, reg, [regA, regB])
            print
            "Registro ID: " + str(bus.read_i2c_block_data(address, reg))
            print
            "regB: " + str(regB), "regA: " + str(regA)
            print
            "Pasirinkote %r rezistoriu veikianti HF dazniu intervale. " % res
        elif res == "5":
            regB = int('00010000', 2)
            regA = int('00000001', 2)
            bus.write_i2c_block_data(address, reg, [regA, regB])
            print
            "Registro ID: " + str(bus.read_i2c_block_data(address, reg))
            print
            "regB: " + str(regB), "regA: " + str(regA)
            print
            "Pasirinkote %r rezistoriu veikianti HF dazniu intervale. " % res
        elif res == "6":
            regA = int('00000001', 2)
            bus.write_i2c_block_data(address, reg, [regA])
            print
            "Registro ID: " + str(bus.read_i2c_block_data(address, reg))
            print
            "regA: " + str(regA)
            print
            "regB bits not set for permanently connected resistors"
            print
            "Pasirinkote %r rezistoriu veikianti HF dazniu intervale. " % res
        else:
            print
            "IVConverter: Invalid resistor index specified. Value was not modified."

    elif resistor == "LF":
        res = raw_input("Pasirinkite rezistoriu (7-11): ")
        if res == "7":
            regA = int('00000001', 2)
            regB = int('00001000', 2)
            bus.write_i2c_block_data(address, reg, [regA, regB])
            print
            "Registro ID: " + str(bus.read_i2c_block_data(address, reg))
            print
            "regB: " + str(regB), "regA: " + str(regA)
            print
            "Pasirinkote %r rezistoriu veikianti LF dazniu intervale. " % res
        elif res == "8":
            regA = int('00000010', 2)
            regB = int('00001000', 2)
            bus.write_i2c_block_data(address, reg, [regA, regB])
            print
            "Registro ID: " + str(bus.read_i2c_block_data(address, reg))
            print
            "regB: " + str(regB), "regA: " + str(regA)
            print
            "Pasirinkote %r rezistoriu veikianti LF dazniu intervale. " % res
        elif res == "9":
            regB = int('01001000', 2)
            bus.write_i2c_block_data(address, reg, [regB])
            print
            "Registro ID: " + str(bus.read_i2c_block_data(address, reg))
            print
            "regB: " + str(regB)
            print
            "Pasirinkote %r rezistoriu veikianti LF dazniu intervale. " % res
        elif res == "10":
            regB = int('01001000', 2)
            bus.write_i2c_block_data(address, reg, [regB])
            print
            "Registro ID: " + str(bus.read_i2c_block_data(address, reg))
            print
            "regB: " + str(regB)
            print
            "Pasirinkote %r rezistoriu veikianti LF dazniu intervale. " % res
        elif res == "11":
            regB = int('00001000', 2)
            bus.write_i2c_block_data(address, reg, [regB])
            print
            "Registro ID: " + str(bus.read_i2c_block_data(address, reg))
            print
            "regB: " + str(regB)
            print
            "regA bits not set for permanently connected resistors. "
            print
            "Pasirinkote %r rezistoriu veikianti LF dazniu intervale. " % res
        else:
            print
            "IVConverter: Invalid resistor index specified. Value was not modified. "
    else:
        print
        "IVConverter: Range can only be 'HF' or 'LF'. Value was not modified. "


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
