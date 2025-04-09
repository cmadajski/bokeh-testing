from bokeh.plotting import figure, show, save

# https://docs.bokeh.org/en/latest/docs/user_guide/basic/lines.html
x = [1, 2, 3, 4, 5, 6]
y = [2, 4, 6, 9, 14, 21]

f1 = figure(
    title='line chart example',
    x_axis_label='x axis thingy',
    y_axis_label='y axis thingy'
)
f1.line(x, y, legend_label='thingy', line_width=2)
show(f1)

#save(f1)

# https://docs.bokeh.org/en/latest/docs/user_guide/basic/bars.html
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
income = [7088, 6296, 4317, 5400, 6100, 4300, 4400, 4200, 5100, 3200, 4300, 4800]

f2 = figure(x_range=months, height=350, title='Monthly Income')
f2.vbar(x=months, top=income, width=0.8)
f2.xgrid.grid_line_color = None
f2.y_range.start = 2000
show(f2)

# widgets: https://docs.bokeh.org/en/latest/docs/first_steps/first_steps_9.html
