import netCDF4
import xarray
import numpy as np
import pandas as pd

dataset =  xarray.open_dataset("./sst/sst_mnmean.nc", decode_times=False)
regrid_lat = np.arange(-90, 90, 10)
regrid_lon = np.arange(0, 360, 20)
# print(len(regrid_lat)* len(regrid_lon))
dataset= dataset.interp(lat= regrid_lat, lon= regrid_lon, method= "nearest")
dataset.to_netcdf('./sst/sst_regrid.nc')