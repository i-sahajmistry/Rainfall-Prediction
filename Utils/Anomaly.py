from email import header
import numpy as np
import pandas as pd
import glob

data = './sst/sst_flattend.csv'
file = './sst/sst05.csv'
# print(glob.glob(mydir))
# for i, file in enumerate(glob.glob(mydir)):
#     print(i)
df = pd.read_csv(file, header=[0,1], index_col=0)
df = np.array(df)
mean = np.mean(df[12:42], axis=0)
data = np.array(pd.read_csv(data, header=None))
print(data.shape)
data = data - mean
print(mean, pd.DataFrame(data))
data = pd.DataFrame(data)
data.to_csv(f'./sst/sst_flattend_a.csv')
    
