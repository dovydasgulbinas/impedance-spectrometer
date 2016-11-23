import logging
import libtiepie

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


    def do_block_measurment(self, sample_freq, nsamples, *args, **kwargs):
        """Enables you to start a block measurment.

        Arguments:
            - *args -- tuple, ((channel1, voltage1), (channel2, voltage2) ...)

        """

        self.scp.measure_mode = libtiepie.MM_STREAM
        self.scp.sample_frequency = sample_freq  # You can use the scientific notation 1e3
        self.scp.record_length = nsamples

        # All other channels must be set to False

        enable = lambda en:

        map(enable , self.scp.channels)











