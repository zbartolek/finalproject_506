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
print(data_xr.variables)

# I think one of the problems with filtering for a specific day is the format of the 
# date. I tried to conver to datetime using pandas (which it sounds like you should be 
# able to do) but it hasn't worked for me.

# pd.to_datetime(data_xr['time'], format='%Y-%m-%d %H:%M:%S')


# Also tried filtering using different methods: sel, where, and loc
# It looks like the loc method did find the individual day 2020-05-26
# but I still haven't been able to plot anything

# SST_today_sel = data_xr.sel(time=slice(2020-05-23 : 2020-05-26))
# SST_today_where = data_xr.wSST_here((data_xr['latitude'] == 40.025) and (data_xr['longitude'] == -125.025))
SST_today_loc = data_xr.loc[dict(time = '2020-05-26')]
# SST_today_loc_arr = SST_today_loc.to_array

fig = plt.figure()
# plt.plot(SST_today_loc_arr['analysed_sst'])
plt.show()

fig = plt.figure()
# plt.scatter(data_xr['latitude'], data_xr['longitude'], c=SST_today_loc['analysed_sst'])
# ax.set_xlabel('Latitude')
# plt.ylabel('Longitude')
plt.show()
