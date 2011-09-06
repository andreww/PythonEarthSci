#!/usr/bin/env python
"""
All matplotlib date plotting is done by converting date instances into
days since the 0001-01-01 UTC.  The conversion, tick locating and
formatting is done behind the scenes so this is most transparent to
you.  The dates module provides several converter functions date2num
and num2date

"""
# Import plotting modules - we will cover these on Thursday
import matplotlib
import matplotlib.pyplot as plt

import metloc

def plot_rainfall(rainfall, annual=None):
    import datetime
    m_dates = []
    m_rain = []
    y_dates = []
    y_rain = []

    for year, monthrain in zip(rainfall.keys(), rainfall.values()):  
        for rain, month in zip(monthrain, range(1,13)):
            m_dates.append(datetime.date(year, month, 1))
            m_rain.append(rain)

    if annual is not None:
        for year, rain in zip(annual.keys(), annual.values()):
            y_dates.append(datetime.date(year, 6, 1))
            y_rain.append(rain)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(m_dates, m_rain)
    ax.set_ylabel('Monthly rainfall (mm)')
    ax.set_xlabel('Date')
    fig.autofmt_xdate()

    if annual is not None:
        ax2 = ax.twinx()
        ax2.plot(y_dates, y_rain, 'g--')
        ax2.plot(y_dates, y_rain, 'go')
        ax2.set_ylabel('Annual rainfall (mm)')


    return fig

def read_file(filename):
    """
    Read a metoffice data file

    The data file, filename, can have a 
    header and approximated rainfall data.
    A dictionary of montly rainfall data is 
    returned with years as the key and 
    Jan - Dec rainfall in a list (0 - 11) in 
    the values.

    """
    data = {} # Somewhere to put the output data
    file = open(filename, 'r') # Open in 'read' mode
    header = 7 # Count down in the header.
    for line in file:  # read the file one line at a time
        if header > 0:
            # We are in the header, process it.
            if header == 7:
                # First line - the name
                stationName = line.strip()
            elif header == 6:
                # Second line: this is a bit nasty, get data out
                # of a helper function
                (lat, lon) = metloc.parselocationlinelatlon(line)
            header = header - 1
        else:
            words = line.split() # Split on spaces
            y = int(words[0]) # Remember to change the data types
            m = int(words[1])

            # Handle (and ignore) any '*' after the rainfall.
            # ot '---' in it
            rain = words[5]
            if rain == '---':
                r = 0.0 # Missing data.
            elif rain[-1] == '*':
                # estimated rainfall - we will use this
                r = float(rain[0:-2])
            else:
                r = float(rain)

            if y not in data:
                data[y] = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                           0.0, 0.0, 0.0, 0.0, 0.0, 0.0] # Place holder 
                data[y][m-1] = r # We need to count the monts from 0.
            else:
                data[y][m-1] = r

    return (data, stationName, lat, lon)

   

if __name__ == "__main__":
    import sys
  
    (monthly_data, stationName, lat, lon) = read_file(sys.argv[1])
    annual_data = {}
    for year, rain in zip(monthly_data.keys(), monthly_data.values()):
        annual_data[year] = sum(rain)

    plot_rainfall(monthly_data, annual_data)
    plt.show()
