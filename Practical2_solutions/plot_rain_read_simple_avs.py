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

def read_simple_file(filename):
    """
    Read a simplified metoffice data file

    The data file, filename, must not have a 
    header, or any approximated rainfall data.
    A dictionary of montly rainfall data is 
    returned with years as the key and 
    Jan - Dec rainfall in a list (0 - 11) in 
    the values.

    """
    data = {} # Somewhere to put the output data
    file = open(filename, 'r') # Open in 'read' mode
    for line in file: # read the file one line at a time
        words = line.split() # Split on spaces
        y = int(words[0]) # Remember to change the data types
        m = int(words[1])
        r = float(words[5])
        if y not in data:
            data[y] = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                       0.0, 0.0, 0.0, 0.0, 0.0, 0.0] # Place holder 
            data[y][m-1] = r # We need to count the monts from 0.
        else:
            data[y][m-1] = r

    return data

def avarage_monthly_rainfall(rainfall_data):
    """
    Calculate the avarage rainfall in each month

    Takes several years of rainfall data and computes the 
    rainfall in each month (ignoring missing data where 
    rain == 0.0 or is None). Returns two lists with 
    month index (from 0 -- 11) and values giving the 
    number of months included and the mean rainfall.

    """
    monthly_totals = 12*[0.0]
    monthly_avarage = 12*[0.0]
    number_of_months = 12*[0]
    for year, rainlist in zip(rainfall_data.keys(), rainfall_data.values()):
        for month, rain in zip(range(12), rainlist):
            if (rain is None) or (rain == 0.0):
                # No data for this month, so do nothing
                continue
            else:
                monthly_totals[month] = monthly_totals[month] + rain
                number_of_months[month] = number_of_months[month] + 1

    for month in range(12):
        monthly_avarage[month] = monthly_totals[month] / \
                             number_of_months[month]

    return monthly_avarage, number_of_months


   

if __name__ == "__main__":

    monthly_data = read_simple_file('cambornedata_simple.txt')
    annual_data = {}
    for year, rain in zip(monthly_data.keys(), monthly_data.values()):
        annual_data[year] = sum(rain)

    plot_rainfall(monthly_data, annual_data)
    plt.show()

    month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    (av, nu) = avarage_monthly_rainfall(monthly_data)
    for i, r, n in zip(range(12), av, nu):
        print month_names[i] + " " + str(r) + " " + str(n)
