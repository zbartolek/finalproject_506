"""

This file plots temperature data from the PMEL Carbon cruise in 2007.

""" 

# imports
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import cartopy.crs as ccrs
import cartopy.feature as cf

#read in the data file
data = pd.read_csv('/Users/MMStoll/Python/Data/Masters_Data/PMELCarbon_Data/PMELCarbon2007.csv', skiprows = 30)

lat = data.LATITUDE
lon = data.LONGITUDE
temp = data.CTDTMP

# plt.close('all')

# plot temperature along the west Coast
tstr = 'Temperature ($^\circ$C) along the West Coast'
fig = plt.figure()
ax = plt.axes(projection = ccrs.PlateCarree())
ax.set_extent([-128, -112, 25, 50]) #specify the longitude bounds, latitude bounds
ax1 = ax.scatter(lon, lat, c=temp, cmap='jet', transform = ccrs.PlateCarree())
cbar = fig.colorbar(ax1)
cbar.set_label('Temperature ($^\circ$C)')
ax.add_feature(cf.COASTLINE) #plot coastline
ax.set_title(tstr)
plt.xlabel('Latitude')
plt.ylabel('Longitude')
plt.show()
