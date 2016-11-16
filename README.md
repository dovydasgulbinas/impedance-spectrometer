## Running

# Win, Mac, Linux(RPI exclued)
1. Install virtual env from file: `conda env create -f pyqtgraphev.yml`
2. Activate env: `source activate qt4qtgraph`

# Rasberry pi
1. sudo apt-get install python3-scipy
2. sudo apt-get install python3-pyqt4
3. git clone https://github.com/pyqtgraph/pyqtgraph.git pyqtgraph
4. cd pyqtgraph
5. python3 setup.py install

## Conclusions on this lib

- Its a really fast-lib that has potencial
- It has dynamic zooming
- I can use some code from `Flowchar.py PlotSpeedTest.py plotAutoRange.py ScrollingPlot.py LinkedViews.py MultiplePlots.py`
- Lib is good for science projects
- lib has EZ to read documentation


## Installing editor tools
```
apt-get install pyqt4-dev-tools
pyuic4 -x two_plot.ui -o base_gui_vx.py
```
## How you can redraw plots
There are two ways of graphing any data in a plot:
1. By waiting for **data** change occurs and only then plotting
2. By constantly calling a method and **polling** for data


## Conclsions

1. If you pass a list of `n` elements then the x axis range will be `0 to n`
2. A single plot space can have multiple line graphs painted on it all you have to do is to call `.plot()` method for a new instance 



## References
[redraw_events](http://stackoverflow.com/questions/20873259/pyqt-how-to-dynamically-update-widget-property-on-outer-variable-value-change)

[documentation](http://www.pyqtgraph.org/documentation/graphicsItems/plotitem.html#pyqtgraph.PlotItem.showGrid)
