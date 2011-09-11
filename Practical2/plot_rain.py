#!/usr/bin/env python

# Import plotting modules - we will cover these on Thursday
import matplotlib
import matplotlib.pyplot as plt

# 18 years of data
monthly_data = {1992: [29.6, 65.0, 58.2, 103.9, 14.7, 9.9, 
                       57.7, 154.4, 93.1, 95.7, 175.1, 124.3], 
                1993: [160.8, 26.8, 28.7, 116.4, 162.9, 110.9,
                       107.1, 43.1, 214.0, 78.9, 104.5, 222.7],
                1994: [161.2, 172.1, 82.9, 66.3, 91.5, 21.6,
                       46.0, 90.1, 83.4, 103.6, 95.5, 140.6],
                1995: [169.6, 121.2, 68.8, 38.9, 41.0, 17.8,
                       25.6, 19.0, 103.2, 102.6, 96.0, 103.2],
                1996: [201.4, 121.6, 51.0, 68.4, 76.8, 20.6,
                       23.2, 68.6, 41.4, 97.8, 170.6, 46.4],
                1997: [31.0, 122.6, 27.6, 17.0, 68.8,
                       130.4, 24.8, 196.6, 48.6, 82.6, 179.4, 138.0],
                1998: [138.6, 17.2, 103.2, 179.4, 59.4, 104.6, 
                      91.8, 27.7, 77.2, 164.8, 161.6, 163.8],
                1999: [152.0, 77.0, 43.8, 98.4, 57.0, 67.8,
                       8.4, 104.4, 118.9, 34.2, 75.6, 222.2],
                2000: [52.4, 130.4, 23.6, 96.8, 80.2, 
                      22.8, 47.8, 52.8, 148.8, 185.2, 171.0, 193.4],
                2001: [137.8, 79.0, 124.6, 101.0, 21.6, 29.4, 86.2,
                       32.4, 21.8, 101.4, 60.4, 52.6],
                2002: [127.4, 121.4, 73.6, 51.6, 114.2, 47.2,
                       57.2, 42.4, 42.4, 138.6, 242.2, 180.0],
                2003: [79.7, 86.8, 34.6, 57.0, 92.4, 87.0, 
                      128.0, 25.6, 44.6, 79.2, 93.0, 102.6],
                2004: [164.6, 80.9, 78.2, 68.8, 33.6, 64.6,
                       65.2, 146.6, 54.4, 190.6, 43.2, 55.4],
                2005: [68.6, 25.8, 53.8, 88.2, 46.6, 49.6,
                       48.0, 32.0, 65.2, 132.0, 164.5, 88.4],
                2006: [62.2, 69.6, 86.0, 32.0, 85.2, 33.4,
                       34.8, 55.4, 76.6, 120.8, 155.6, 119.6],
                2007: [83.4, 212.8, 75.8, 23.8, 122.0, 117.0,
                       106.8, 43.4, 29.8, 37.4, 75.4, 80.2],
                2008: [108.4, 41.4, 82.8, 48.8, 68.4, 34.6,
                       143.4, 99.6, 76.6, 111.8, 69.8, 85.0],
                2009: [146.0, 71.3, 48.8, 144.2, 45.2, 18.8,
                       222.2, 68.8, 37.8, 93.4, 193.6, 101.8],
                2010: [108.8, 63.0, 76.6, 35.6, 56.6, 34.0,
                       78.2, 71.8, 83.6, 85.6, 164.8, 48.1]}

def plot_rainfall(rainfall, annual=None):
    # Plot the grapg - don't worry about how this function works,
    # we will look at this on Thursday
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

if __name__ == "__main__":

    # Calculate the annual rainfall here.

    plot_rainfall(monthly_data)
    plt.show()
