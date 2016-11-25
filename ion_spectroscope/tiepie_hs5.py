import logging
import libtiepie
from printinfo import *

logger = logging.getLogger('TiePieClass')

class SpectroscopeManager:

    def __init__(self):
        self.scp = None  # osciloscope object


    def init_tiepie(self):
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


    def setup_block_measurment(self, sample_freq, nsamples, *args, **kwargs):
        """Sets you up for block measurment.

        Arguments:
            - *args -- tuple, ((channel_id, range1, coupling1), (channel_id, range2) ...)

        """

        self.scp.measure_mode = libtiepie.MM_STREAM
        self.scp.sample_frequency = sample_freq  # You can use the scientific notation 1e3
        self.scp.record_length = nsamples

        for setup in args:
            if setup[0]:
                # channel must be enabled
                # grabs channel object
                ch = self.scp.channels[args.index(setup)]
                ch.enabled = True
                ch. range = setup[1]
                ch.coupling = libtiepie.CK_DCV # DC Volt

        if kwargs is not None:
            keys = kwargs.keys()
            if 'info' in keys:
                # Print oscilloscope info:
                print_device_info(scp)
                # add kwargs here!



    def start_block_measurment(self):
        scp.start()

        # add code here!!!






#TODO: 1. De
#TODO:
#TODO:
#TODO:
#TODO:
#TODO:
#TODO:
#TODO:
#TODO:
#TODO:
#TODO:





