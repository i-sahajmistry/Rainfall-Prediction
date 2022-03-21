#importing libraries
from netCDF4 import Dataset
import pandas as pd
import os

#Paste the directory of the folder that your nc files are in it, instead of "XXXXX"
mydir="D:/Sahaj/Raw_data/Regrid/uwnd"
os.chdir(mydir)

#List your files that are in the path (directory)
names=[]
for file in os.listdir(mydir):
    if file.endswith(".nc"):
        names = file

#Get the variables that the NC files have
data = Dataset(names)
print(data.variables.keys())

###Next step is: By Printing the variable names you can choose the title of the column you want to use it. Lets assume the variable that you want, is called "u".
u_wind = data.variables['u'][:]

time = data.variables['T'][:]
longitude = data.variables['X'][:]
latitude = data.variables['Y'][:]
pressure = data.variables['P'][9]
print(u_wind.shape)

final_data = []
for t in range(len(time)):
    temp = []
    for lat in range(len(latitude)):
        for lon in range(len(longitude)):
            value = u_wind[t, 9, lat, lon]
            temp.append(value)
    final_data.append(temp)

mon = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
index = [f'{i}-{j}' for i in range(1949,2022) for j in mon]

df = pd.DataFrame(final_data[:-2], index=index)
df.to_csv('D:/Sahaj/Raw_data/Regrid/uwnd/uwnd.csv', index=True)