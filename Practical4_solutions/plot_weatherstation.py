#!/usr/bin/env python
from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
import rainfall


def plot_point(lats, lons):
    # llcrnrlat,llcrnrlon,urcrnrlat,urcrnrlon
    # are the lat/lon values of the lower left and upper right corners
    # of the map.
    # resolution = 'i' means use intermediate resolution coastlines.
    # lon_0, lat_0 are the central longitude and latitude of the projection.
    m = Basemap(llcrnrlon=-8.5,llcrnrlat=49.5,urcrnrlon=3.5,urcrnrlat=60.5,
            resolution='i',projection='tmerc',lon_0=-4.36,lat_0=54.7)
    # can get the identical map this way (by specifying width and
    # height instead of lat/lon corners)
    #m = Basemap(width=894887,height=1116766,\
    #            resolution='i',projection='tmerc',lon_0=-4.36,lat_0=54.7)
    m.drawcoastlines()
    m.fillcontinents(color='coral',lake_color='aqua')
    # draw parallels and meridians.
    m.drawparallels(np.arange(-40,61.,2.))
    m.drawmeridians(np.arange(-15.,21.,2.))
    m.drawmapboundary(fill_color='aqua') 
    for lat, lon in zip(lats, lons):
       (x, y) = m(lon, lat)
       m.plot(x,y,'wo')
    plt.show()

if __name__=="__main__":
    import sys
    lats = []
    lons = []
    for file in sys.argv[1:]:
        station = rainfall.Rainfall(file)
        lats.append(station.lat)
        lons.append(station.lon)
    plot_point(lats, lons)
