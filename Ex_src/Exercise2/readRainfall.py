#!/usr/bin/env python
import re
import metloc

def readRainfallFile(filename):
    """
    Wrapper around readRainfallData to deal with files

    """
    file = open(filename, 'r')
    (stationName, lat, lon, years, months, 
        rainfall) = readRainfallData(file)
    file.close()
    return stationName, lat, lon, years, months, rainfall
    

def readRainfallData(fh):
    """
    Extract metoffice historic rainfall data from a file object

    The file format is 7 lines of header followed by N lines
    of column oriented data. We need data from column 1 (the 
    year), 2 (the month) and 6 (the rainfall, in mm). Return 
    this data in three lists. Rain of '---' is a lack of 
    data so return None for these months. We also need the 
    location name (first line of the header) and the position 
    (from the second line). This is processed and returned as
    latitude and longitude (floats, in degrees).

    """
    # Empty lists for output
    years = []
    months = []
    rainfall = []
    header = 7 # Count down in the header.
    for line in fh:
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
            # Split on spaces (words in a list)
            words = line.split()
            # Years and months should be ints
            year = int(words[0])
            month = int(words[1])
            # Rainfall is a float, or None:
            rain = words[5]
            if rain == '---':
                rain = None
            elif rain[-1] == '*':
                # estimated rainfall - we will use this
                rain = float(rain[0:-2])
            else:
                rain = float(rain)
            # Append this month's data to output array:
            years.append(year)
            months.append(month)
            rainfall.append(rain)

    return stationName, lat, lon, years, months, rainfall

if __name__ == '__main__':
    import sys

    for filename in sys.argv[1:]:
        stationName, lat, lon, years, \
            months, rainfall =  readRainfallFile(filename)
        print
        print "Rainfall data from: " + stationName
        print "(" + str(lon) + " degrees E, " + str(lat) + " degrees N)"
        print "First year / month: " + str(years[0]) + " / " + str(months[0]) + \
            " " + str(rainfall[0]) + " mm of rain"
        print "Last year / month: " + str(years[-1]) + " / " + str(months[-1]) + \
        " " + str(rainfall[-1]) + " mm of rain"
    print
