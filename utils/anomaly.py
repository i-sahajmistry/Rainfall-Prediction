import enum
import numpy as np
import pandas as pd
import glob
import os

mydir = 'D:/Sahaj/Raw_data/Regrid/uwnd/uwnd10.csv'

# for i, file in enumerate(glob.glob(mydir)):
df = pd.read_csv(mydir, header=[0,1], index_col=0)
data = np.array(df)
mean = np.mean(data[12:42], axis=0)
data = data - mean
df = pd.DataFrame(data, index=df.index)
df.to_csv(f'D:/Sahaj/uwnd{10}.csv')
    
