#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Update a simple plot as rapidly as possible to measure speed.
"""

from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg
from pyqtgraph.ptime import time


app = QtGui.QApplication([])

p = pg.plot()
p.setWindowTitle('pyqtgraph example: PlotSpeedTest')
# TODO: Investigate http://pyqtgraph.org/documentation/widgets/plotwidget.html
p.setRange(QtCore.QRectF(0, -10, 5000, 20))



# My edit
p.showGrid(True, True)
p.setLabel('bottom', text='Voltage', units='V')
p.setLabel('left', text='Current', units='A')
# --
from basic_iterator import SineIterable
sin_data = SineIterable(0,20)

# end my edit

# visual plot data you pass in args here
curve = p.plot()

# renders a huge numpy array
data = np.random.normal(size=(50, 5000))

# a global counter variable
ptr = 0

lastTime = time()
fps = None


def update():
    global curve, data, ptr, p, lastTime, fps

    # p.plot().setData() -- sets data that will be plotted
    # TODO: Inject sensor data here:
    curve.setData(data[ptr % 10])

    # itterated on demmand
    # curve.setData([y for y in sin_data])
    # END

    ptr += 1
    now = time()
    dt = now - lastTime
    lastTime = now
    if fps is None:
        fps = 1.0 / dt
    else:
        s = np.clip(dt * 3., 0, 1)
        fps = fps * (1 - s) + (1.0 / dt) * s
    p.setTitle('%0.2f fps' % fps)
    app.processEvents()  # force complete redraw for every plot


timer = QtCore.QTimer()
# attach method that will be called as fast as possible
timer.timeout.connect(update)
timer.start(0)

# Start Qt event loop unless running in interactive mode.
if __name__ == '__main__':
    import sys

    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
