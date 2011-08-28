#!/usr/bin/env python
import readRainfall

month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
               'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

def avarage_monthly_rainfall(years, months, rainfall):
    monthly_totals = 12*[0.0]
    monthly_avarage = 12*[0.0]
    number_of_months = 12*[0]
    for year, month, rain in zip(years, months, rainfall):
        if rain is None:
            # No data for this month, so do nothing
            continue
        else:
            monthly_totals[month-1] = monthly_totals[month-1] + rain
            number_of_months[month-1] = number_of_months[month-1] + 1

    for month in range(12):
        monthly_avarage[month] = monthly_totals[month] / \
                                 number_of_months[month]

    return monthly_avarage, number_of_months
        

if __name__ == "__main__":
    import sys
    datafile = sys.argv[1]
    stationName, lat, lon, years, \
        months, rainfall =  readRainfall.readRainfallFile(datafile)
    avarage, N = avarage_monthly_rainfall(years, months, rainfall)
    for month in range(12):
        print month_names[month] + ": " + str(avarage[month]) + " " + str(N[month])
    
