import logging
import time
import libtiepie
from printinfo import *

logger = logging.getLogger('TiePieClass')
logger.debug('The module has been started')


class SpectroscopeManager:
    def __init__(self, init_scp=True, init_gen=False):
        self.scp = None  # osciloscope object
        self.gen = None  # generator object
        if init_scp:
            self.init_scp()
        if init_gen:
            self.init_generator()

    def init_scp(self):
        """Adds all methods need for starting oscilloscope."""
        libtiepie.device_list.update()

        # search for oscilloscopes

        for item in libtiepie.device_list:
            if item.can_open(libtiepie.DEVICETYPE_OSCILLOSCOPE):
                self.scp = item.open_oscilloscope()
                if self.scp.measure_modes & libtiepie.MM_STREAM:
                    break
                else:
                    raise IOError("Could initialize oscilloscope")

    def init_generator(self):
        """Adds all methods need for starting oscilloscope."""
        libtiepie.device_list.update()
        # search for generator
        for item in libtiepie.device_list:
            if item.can_open(libtiepie.DEVICETYPE_GENERATOR):
                self.gen = item.open_generator()
                if self.gen:
                    logger.info('Found a generator!')
                    break
                else:
                    logger.error("Could initialize generator")

    def setup_generator(self, frequency, amplitude, offset=0, output_on=True, info=True):
        if self.gen:
            self.gen.signal_type = libtiepie.ST_SINE

            # Set frequency:
            self.gen.frequency = frequency

            # Set amplitude:
            self.gen.amplitude = amplitude

            # Set offset:
            self.gen.offset = offset  # 0 V

            # Enable output:
            self.gen.output_on = output_on

            # Print generator info:
            if info:
                print_device_info(self.gen)
        else:
            logger.error('Generator is not initialized, try running init_generator()')
            raise IOError("Generator object not initialized")

    def start_generator(self):
        self.gen.start()

    def stop_generator(self):
        self.gen.stop()

    def setup_block_measurment(self, sample_freq, nsamples, setups, **kwargs):
        """Sets you up for block measurment.

        Arguments:
            - setups -- tuple, ((channel_id, range1, coupling1), (channel_id, range2) ...)

        """
        logger.debug('Starting a block measurment!')

        self.scp.measure_mode = libtiepie.MM_STREAM
        self.scp.sample_frequency = sample_freq  # You can use the scientific notation 1e3
        self.scp.record_length = nsamples

        for setup in setups:
            if setup[0]:
                # channel must be enabled
                # grabs channel object
                ch = self.scp.channels[setups.index(setup)]
                ch.enabled = True
                ch.range = setup[1]
                ch.coupling = libtiepie.CK_DCV  # DC Volt

        if kwargs is not None:
            keys = kwargs.keys()
            if 'info' in keys:
                # Print oscillosscope info:
                if kwargs['info']:
                    print_device_info(self.scp)
                    # add kwargs here!

    def set_new_data_handler(self, func):
        self.new_data_handler = func

    @staticmethod
    def new_data_handler(data, **kwargs):
        logger.warning('Please overrirde new_data_handler')

    def do_block_measurment(self, nblocks=10, sleep_period=0.01):
        logger.info('Starting a block measurment')
        self.scp.start()
        try:
            for block in range(nblocks):
                logger.debug('Processing block: {}'.format(block))
                while not (self.scp.is_data_ready or self.scp.is_data_overflow):
                    time.sleep(sleep_period)  # saving processor some workload

                if self.scp.is_data_overflow:
                    logger.warning('Data overflow occured!')
                    break

                data = self.scp.get_data()
                # this will call a new data handler when there is new data
                self.new_data_handler(data)

        except Exception as e:
            logger.error('Error occured during block measurment: {}'.format(e))

        finally:
            self.scp.stop()
            logger.warning('Stopping TiePie processes')

            # make sure deletion of the object is needed

    def stop_everything(self):
        logger.info('Stopping all processes')
        if self.gen:
            self.gen.stop()

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
    logger.debug('Running as main')
    def test_handler(data):
      logger.debug('Here is the data {}'.format(data))
      #  for block in data:
      #      logger.debug("block {}".format(block))

    scopes = SpectroscopeManager()
    scopes.set_new_data_handler(test_handler)
    scopes.setup_block_measurment(1000, 100,[[0, 8]], info=True)
    scopes.do_block_measurment()
