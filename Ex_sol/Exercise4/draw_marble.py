from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

# Set up the basemap
m = Basemap(projection='nsper',lon_0=-10,lat_0=40,resolution='l',
            satellite_height=15000000)

# draw parallels and meridians.
m.drawparallels(np.arange(-90.,120.,30.),'white')
m.drawmeridians(np.arange(0.,420.,60.),'white')

# Draw the image
m.bluemarble()

# Plot a city
x, y = m(-2.58, 51.54)
m.plot(x,y,'wo')

# Show the image.
plt.show()
