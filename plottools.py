#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tools for plotting in Jupyter notebooks with Bokeh.
"""

#...for the Bokeh figure functionality.
from bokeh.plotting import figure

#...for setting up the x axis (time).
from bokeh.models import FixedTicker, NumeralTickFormatter, Range1d

#...mmm... pi.
from math import pi

# Time constants.
from timevals import *

def get_hour_tickmarks_for_one_day():
    """ Returns a list of second values required for one per hour for a day. """
    return range(0, SECONDS_IN_A_DAY+1, SECONDS_IN_AN_HOUR)

def get_day_plot_figure(max_y):
    """ Make a blank plot with a 24-hour x axis with units of seconds. """

    ## The figure.
    p = figure(width=800, height=300, x_range=Range1d(0, SECONDS_IN_A_DAY), y_range=Range1d(0, max_y))

    # Set the axis labels.
    p.xaxis.axis_label = "Time"
    p.yaxis.axis_label = "Pixels / s"

    # Here's the first trick: set the format of the ticker labels to time
    # using a NumeralTickFormatter and the time format string.
    p.xaxis.formatter = NumeralTickFormatter(format="00:00:00")

    # This tilts the time value displayed to avoid overlaps.
    p.xaxis.major_label_orientation = pi/4

    # Here's the second trick: use a custom set of ticker values to make
    # sure only hour values are displayed. The second values are converted
    # to a time by the NumeralTickFormatter.
    p.xaxis.ticker=FixedTicker(ticks=get_hour_tickmarks_for_one_day())

    # However - Boker's grid tends to use nice round numbers for the major
    # and minor grid lines, and I can't see how to configure this - so
    # for now we just switch them off.
    p.xgrid.grid_line_color = None

    return p
