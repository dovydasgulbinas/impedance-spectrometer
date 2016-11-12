from PyQt4 import QtGui
import pyqtgraph as pg

# all programs begin win initialization of single app
app = QtGui.QApplication([])  # why is the empty list for?

# define a containter widget that will contain all other widgets
w = QtGui.QWidget()

# create some random widgets to be contained in w widget
btn = QtGui.QPushButton('press me')
text = QtGui.QLineEdit('Enter some text')
listw = QtGui.QListWidget()
# here we use our plot widget
plot = pg.PlotWidget()

# we generate a grid layout. There are other layouts eg. horizontal etc..
layout = QtGui.QGridLayout()
w.setLayout(layout)

# add widgets to the layout:
layout.addWidget(btn,0,0)
layout.addWidget(text,1,0)
layout.addWidget(listw, 2,0)
layout.addWidget(plot, 0,1,3,1)

# display our container widget
w.show()

# start qt event loop
app.exec_()

"""
- app
- QWidget
- QtGui.QGridLayout
- QWidget.setLayout
"""