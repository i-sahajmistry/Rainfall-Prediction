import pandas as pd
import numpy as np

df = pd.read_csv("./sst/sst_new.csv", header=None)
data = [[]]
df = np.array(df)
for row in df:
    for i in row:
        data[0].append(i)

pd.DataFrame(data).to_csv("./sst/sst_flattend.csv")