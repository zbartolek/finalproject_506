"""

Read in SST satellite data

"""
import numpy as np
import matplotlib.pyplot as plt
import netCDF4
import math
import xarray as xr
import pandas as pd
import datetime
import cartopy.crs as ccrs
import cartopy.feature as cf

path_in='/Users/MMStoll/Python/Data/EffectiveComputing_Data/NOAA_SST_Daily.nc'
data_xr = xr.open_dataset(path_in)

# Data dimensions
print('\n')
print(data_xr.dims)

# Data coordinates
print('\n')
print(data_xr.coords)

# Data variables
print('\n')
print(data_xr.data_vars)

# Extended information on variables
# print(SST_xr.variables)

# pd.to_datetime(data_xr['time'], format='%Y-%m-%d %H:%M:%S')

# SST_today = data_xr.sel(time=slice(2020-05-23 : 2020-05-26))
# SST_today = data_xr.where((data_xr['latitude'] == 40.025) and (data_xr['longitude'] == -125.025))

SST_today = data_xr.loc[dict(time = '2020-05-26')]

fig = plt.figure()
plt.plot(SST_today['analysed_sst'])
plt.show()
# plt.scatter(lon, lat, c=pH_90, cmap='jet')
# cbar = plt.colorbar()
# cbar.set_label('pH')



fig = plt.figure()
# ax = plt.axes(projection = ccrs.PlateCarree())
# ax.set_extent([-130, -120, 40, 50])
# ax1 = ax.scatter(lon, lat, c=pH_90, cmap='jet', transform = ccrs.PlateCarree())
# ax.add_feature(cf.COASTLINE)
plt.scatter(data_xr['latitude'], data_xr['longitude'], c=SST_today['analysed_sst'])
# ax.set_xlabel('Latitude')
plt.ylabel('Longitude')
plt.show()


# 