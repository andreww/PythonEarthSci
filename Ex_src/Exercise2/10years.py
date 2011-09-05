import readRainfall

stationName, lat, lon, years, months, rainfall = readRainfall.readRainfallFile('metoffice_data/cambornedata.txt')

data = {}
for r, m, y in zip(rainfall, months, years):
    if (int(y) > 1991):
        if y not in data:
            data[y] = [None, None, None, None, None, None, None, None, None, None, None, None]
            data[y][m-1] = r
        else:
            data[y][m-1] = r

print data
      

