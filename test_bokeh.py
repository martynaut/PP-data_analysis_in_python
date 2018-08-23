# run serves as
# bokeh serve --show test_bokeh.py --port 8000 --allow-websocket-origin=IP:8000


from bokeh.layouts import column, widgetbox
from bokeh.models.widgets import Select, Button
from bokeh.models import FuncTickFormatter, SingleIntervalTicker, LinearAxis, Span, HoverTool
from bokeh.plotting import figure, curdoc

import datetime
import numpy as np


years = np.arange(2017, datetime.datetime.now().year+1, 1)

months = np.arange(1,13,1)

years = list(map(lambda x: str(x), years))

months = list(map(lambda x: str(x).zfill(2), months))



p = figure(title="Title", plot_height=300, plot_width=600,
           y_range=(-10, 100000000), x_axis_type=None)

hover = HoverTool(tooltips=[("y", "@height")])
p.add_tools(hover)


ticker = SingleIntervalTicker(interval=1, num_minor_ticks=0)
xaxis = LinearAxis(ticker=ticker)
p.add_layout(xaxis, 'below')

hline = Span(location=90000000, dimension='width', line_color='green', line_width=3)
hline2 = Span(location=10000000, dimension='width', line_color='red', line_width=3)

p.renderers.extend([hline, hline2])

p.border_fill_color = None
p.background_fill_color = 'white'
p.outline_line_color = None
p.left[0].formatter.use_scientific = False

p.min_border_left = 10
p.min_border_right = 10
p.min_border_top = 10
p.min_border_bottom = 10

height = np.array([69158597, 2517252, 2866574, 2517252+2866574])

r = p.rect(x=[0,1,2, 3], y=height/2, width=0.5, height=height, color="#CAB2D6")

names = ['A', 'B', 'C', 'D']
label_dict = {}
for i, s in enumerate(names):
    label_dict[i] = s

p.xaxis.formatter = FuncTickFormatter(code="""
    var labels = %s;
    return labels[tick];
""" % label_dict)

def update():

    values = [0, 0, 0, 0]

    r.data_source.data['y'] = np.array(values)/2
    r.data_source.data['height'] = values





menu1 = Select(title="Year", value="2018", options=years)


menu2 = Select(title="Month", value="01", options=months)

button1 = Button(label='Refresh')


button1.on_click(update)


curdoc().add_root(column(widgetbox(menu1, menu2, button1), p))

