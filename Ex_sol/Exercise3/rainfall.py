#!/usr/bin/env python
import plot_rain_read_full as prrf

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
        

if __name__ == '__main__':
    import sys
    # Import plotting modules - we will cover these on Thursday
    import matplotlib
    import matplotlib.pyplot as plt
    rainfall = Rainfall(sys.argv[1])

    for m in range(12):
        av, n = rainfall.avarage_month(m)
        print str(m) + " : " + str(av) + " (n=" + str(n) + ")"

    prrf.plot_rainfall(rainfall._data, rainfall.annual_total())
    plt.show()

    

