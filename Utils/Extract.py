#importing libraries
from netCDF4 import Dataset
import pandas as pd
import os

#Paste the directory of the folder that your nc files are in it, instead of "XXXXX"
mydir="D:/Sahaj/Raw_data/New/nearest_sst.nc"
# os.chdir(mydir)

#List your files that are in the path (directory)
# names=[]
# for file in os.listdir(mydir):
#     if file.endswith(".nc"):
#         names = file
# print(names)

names = [mydir]

#Get the variables that the NC files have
data = Dataset(mydir)
print(data.variables.keys())

###Next step is: By Printing the variable names you can choose the title of the column you want to use it. Lets assume the variable that you want, is called "u".
sst = data.variables['sst'][:]

time = data.variables['time'][:]
longitude = data.variables['lon'][:]
latitude = data.variables['lat'][:]
# pressure = data.variables['P'][9]
print(sst.shape)

final_data = [[] for _ in range(12)]
for t in range((95*12)+1, len(time)):
    temp = []
    for lat in range(len(latitude)):
        for lon in range(len(longitude)):
            value = sst[t, lat, lon]
            # print(value, t, lat, lon)
            temp.append(value)
    final_data[t%12].append(temp)

index = [i for i in range(1949,2022)]
print(len(index))
# mon = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
# index = [f'{i}-{j}' for i in range(1949,2022) for j in mon]

# df = pd.DataFrame(final_data[:-2], index=index)
for i in range(12):
    try: df = pd.DataFrame(final_data[i], index=index)
    except: df = pd.DataFrame(final_data[i][:-1], index=index)
    s = '0'*(2-len(str(i)))
    df.to_csv(f'D:/Sahaj/Raw_data/New/Nearest/sst{s}{i}.csv', index=True)