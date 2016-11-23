# OscilloscopeStream.py - for LibTiePie 0.5+
#
# This example performs a stream mode measurement and writes the data to OscilloscopeStream.csv.
#
# Find more information on http://www.tiepie.com/LibTiePie .

from __future__ import print_function
import time
import os
import sys
import libtiepie
from printinfo import *


# Print library info:
print_library_info()

# Search for devices:
libtiepie.device_list.update()

# Try to open an oscilloscope with stream measurement support:
scp = None
for item in libtiepie.device_list:
    if item.can_open(libtiepie.DEVICETYPE_OSCILLOSCOPE):
        scp = item.open_oscilloscope()
        if scp.measure_modes & libtiepie.MM_STREAM:
            break
        else:
            scp = None

if scp:
    try:
        # Set measure mode:
        scp.measure_mode = libtiepie.MM_STREAM

        # Set sample frequency:
        scp.sample_frequency = 1e3  # 1 kHz

        # TODO: How to Get infinite amount of samples
        # Sets how many samples it will take. Defined in register.
        scp.record_length = 8 # 1 kS

        # Allows to enable any channel:
        ch = scp.channels[0]
            # Enable channel to measure it:
        ch.enabled = True

        # Set range:
        ch.range = 8  # 8 V

        # Set coupling:
        ch.coupling = libtiepie.CK_DCV  # DC Volt
    except Exception as e:
        print("Exception: {}".format(e))
            
    else:

        # scp is a class instance with representation
        print_device_info(scp)

        # Start measurement:
        scp.start()

        # Generate a text file headers
        try:
            # TODO: what is a block?

            print()
            sample = 0
            for take in range(3):

                print("DataBlock:".format(take))

                # Wait for measurement to complete:
                while not (scp.is_data_ready or scp.is_data_overflow):
                    time.sleep(0.10)  # Qt timer can be used

                if scp.is_data_overflow:
                    print('Data overflow!')
                    break

                #:: Get data:
                data = scp.get_data()
                print(data[0])

        except Exception as e:
            print('Exception:{}'.format(e))
            sys.exit(1)

        else:
            print("data-received")
        finally:
            scp.stop()
            del scp


else:
    print('No oscilloscope available with stream measurement support!')
    sys.exit(1)


sys.exit(0)
