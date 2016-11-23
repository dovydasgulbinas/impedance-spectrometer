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
        scp.record_length = 1000  # 1 kS
 
        # Allows to enable any channel:
        for ch in scp.channels:
            # Enable channel to measure it:
            ch.enabled = True
 
            # Set range:
            ch.range = 8  # 8 V
 
            # Set coupling:
            ch.coupling = libtiepie.CK_DCV  # DC Volt
 
        # Print oscilloscope info:
        # scp is a class instance with representation 
        print_device_info(scp)
 
        # Start measurement:
        scp.start()
 
        # Generate a text file headers
        csv_file = open('OscilloscopeStream.csv', 'w')
        try:
            # Create a text file headers:
            csv_file.write('Sample')
            for i in range(len(scp.channels)):
                csv_file.write(';Ch' + str(i + 1))
            csv_file.write(os.linesep)
            
            # TODO: what is a block?
            # Measure 10 blocks:
            print()
            sample = 0
            for block in range(10):
                # Print a message, to inform the user that we still do something:
                print('Data block ' + str(block + 1))
 
                # Wait for measurement to complete:
                while not (scp.is_data_ready or scp.is_data_overflow):
                    time.sleep(0.01)  # 10 ms delay, to save CPU time
 
                if scp.is_data_overflow:
                    print('Data overflow!')
                    break
 
                # Get data:
                data = scp.get_data()
 
                # Output CSV data:
                for i in range(len(data[0])):
                    csv_file.write(str(sample + i))
                    for j in range(len(data)):
                        csv_file.write(';' + str(data[j][i]))
                    csv_file.write(os.linesep)
 
                sample += len(data[0])
 
            print()
            print('Data written to: ' + csv_file.name)
        finally:
            csv_file.close()
 
        # Stop stream:
        scp.stop()
 
    except Exception as e:
        print('Exception: ' + e.message)
        sys.exit(1)
 
    # Close oscilloscope:
    del scp
 
else:
    print('No oscilloscope available with stream measurement support!')
    sys.exit(1)
 
sys.exit(0)