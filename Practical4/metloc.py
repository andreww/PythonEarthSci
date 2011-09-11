#!/usr/bin/env python
"""
    Metloc: converts the Met Office location data to global location

    The Met Office historical data files seem to give station locations
    in a rather odd format: hundreds of meters north and east of the 
    botom left corner of the OS national grid box. Furthermore, it 
    seems that they may be using some other geoid. Never mind, we
    don't need particually acurate data and there is a Python module 
    we can use to convert the location (but all within the OSGB36 
    reference, not WGS84. We'll be < 1 km out I expect (seems to 
    work to ~0.01 degrees).

    Also provide functions to extract locations (as 100's of m
    N and E of the corner of the OS box, or lat/lon in degrees,
    from the second line of the header file.

    This module make use of osgb.py to convert met office data to 
    a location we can plot. One function is provided (met2latlon).
    Running the code as a script reads two arguments (E, N) and 
    prints the location (lat, lon).

"""
import re # Need regex for parsing
import osgb

def parselocationlinelatlon(line):
    """
    Extract easting and westing, and return lat and lon

    """
    (easting, northing) = parselocationlineeastnorth(line)
    (lat, lon) = met2latlon(easting, northing)
    return (lat, lon)

def parselocationlineeastnorth(line):
    """
    Extract easting and northing from second line format

    """
    mo = re.match('Location:? (\d+)[EW] (\d+)[NS]',line)
    if mo:
        easting = int(mo.group(1))
        northing = int(mo.group(2))
    else:
        raise ValueError("Could not find location")
    return (easting, northing)



def met2latlon(east, north, verbose=False):
    """
    Convert nasty numbers using osgb as a back-end

    Input location east and north from the OSGR corner and 
    return the lat, lon (in degrees). 
    
    """
    gridref = osgb.eastnorth_to_osgb(east*100, north*100)
    if verbose: 
        print "Grid reference: " + gridref
    lon, lat = osgb.osgb_to_lonlat(gridref)
    return lat, lon

def plot_location(lat, lon, stationName):
    """
    Use Matplotlib's basemap to plot a weather station location

    Based on http://matplotlib.sourceforge.net/basemap/doc/html/users/tmerc.html

    """
    from mpl_toolkits.basemap import Basemap
    import numpy as np
    import matplotlib.pyplot as plt
    m = Basemap(llcrnrlon=-10.5,llcrnrlat=49.5,urcrnrlon=3.5,urcrnrlat=59.5,
             resolution='i',projection='tmerc',lon_0=-4.36,lat_0=54.7)
    m.drawcoastlines()
    m.fillcontinents(color='coral',lake_color='aqua')
    # draw parallels and meridians.
    m.drawparallels(np.arange(-40,61.,2.))
    m.drawmeridians(np.arange(-20.,21.,2.))
    m.drawmapboundary(fill_color='aqua') 
    x, y = m(lon,lat)
    m.plot(x,y,'o')
    plt.title(stationName)
    plt.show()

if __name__ == "__main__":
    import sys

    east = float(sys.argv[1])
    north = float(sys.argv[2])
    lat, lon = met2latlon(east, north, verbose=True)
    print "Latitude: " + str(lat) + "N (degrees)"
    print "Longitude: " + str(lon) + "E (degrees)"
    

