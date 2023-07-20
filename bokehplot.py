#%%
import numpy as np
from bokeh.io import curdoc
from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource, Slider, TextInput
from bokeh.plotting import figure, show

# Set up data
N = 400
x = np.linspace(0, 4*np.pi, N)
y = np.sin(x)
source = ColumnDataSource(data=dict(x=x, y=y))


# Set up plot
plot = figure(height=400, width=400, title="my sine wave",
              tools="crosshair,pan,reset,save,wheel_zoom",
              x_range=[0, 4*np.pi], y_range=[-2.5, 2.5])

plot.line('x', 'y', source=source, line_width=3, line_alpha=0.6)
show(plot)

from bokeh.layouts import gridplot
from bokeh.models import CDSView, ColumnDataSource, IndexFilter
from bokeh.plotting import figure, show
from bokeh.io import output_notebook

# create ColumnDataSource from a dict
source = ColumnDataSource(data=dict(x=[1, 2, 3, 4, 5], y=[1, 2, 3, 4, 5]))

# create a view using an IndexFilter with the index positions [0, 2, 4]
view = CDSView(filter=IndexFilter([0, 2, 4]))

# setup tools
tools = ["pan", "hover", "reset", "wheel_zoom"]

# create a first plot with all data in the ColumnDataSource
p = figure(height=300, width=300, tools=tools)
p.circle(x="x", y="y", size=10, hover_color="red", source=source)

# create a second plot with a subset of ColumnDataSource, based on view
p_filtered = figure(height=300, width=300, tools=tools)
p_filtered.circle(x="x", y="y", size=10, hover_color="red", source=source, view=view)

# show both plots next to each other in a gridplot layout
output_notebook()
show(gridplot([[p, p_filtered]]))


