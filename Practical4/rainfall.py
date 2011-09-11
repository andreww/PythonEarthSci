#!/usr/bin/env python
import datetime as dt
import read_rainfall as prrf

# You can use this for Exercise 2 and 3 if you did not get the Rainfall
# class working in Practical 3

class Rainfall:

    def __init__(self, filename):
        (monthly_data, stationName, 
        lat, lon) = prrf.read_file(filename)
        self._data = monthly_data
        self.name = stationName
        self.lat = lat
        self.lon = lon

    def annual_total(self):
        annual_data = {}
        for year, rain in zip(self._data.keys(), 
                              self._data.values()):
            annual_data[year] = sum(rain)
        return annual_data

    def avarage_month(self, month):
        """
        Returns the montly avarage rainfall 

        Month is an integer giving the month 
        (0 = Jan, 11 = Dec)

        """
        n = 0
        tot = 0 
        for rain in self._data.values():
            tot = tot + rain[month]
            n = n + 1
        return tot/n, n

    def list_data(self, start=None, end=None, months=range(1,13)):
        """
        Return a list of montly rainfall (and date objects)

        Return all rainfall data between the (optional) start
        and end dates (datetime.date objects) as a list 
        (one month per item) along with a list of date
        objects (1st of each month with data.

        """
        rain = []
        dates = []
        for year, rainl in zip(self._data.keys(), 
                              self._data.values()):
            for m, r in zip(range(1,13), rainl):
                thisdate = dt.date(year, m, 1)
                if (((start is None) or (thisdate >= start))
                      and ((end is None) or (thisdate <= end))
                      and (m in months)):
                    rain.append(r)
                    dates.append(dt.date(year, m, 1))
        return rain, dates
        
        

if __name__ == '__main__':
    import sys
    # Import plotting modules - we will cover these on Thursday
    import matplotlib
    import matplotlib.pyplot as plt
    rainfall = Rainfall(sys.argv[1])

    for m in range(12):
        av, n = rainfall.avarage_month(m)
        print str(m) + " : " + str(av) + " (n=" + str(n) + ")"

    print rainfall.list_data(start=dt.date(2000,1,1), end=dt.date(2004,2,1), months=[6])

    prrf.plot_rainfall(rainfall._data, rainfall.annual_total())
    plt.show()

    

