import pandas as pd
import numpy as np

df = pd.read_csv('D:/Sahaj/Raw_data/Regrid/uwnd/uwnd_regrid.csv', header=None)
# print(df[0:18])
# months = [np.array([0 for i in range(324)]).reshape(1, 324) for j in range(12)]
mon = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
x = 0
months = []
i = 0
count = 0
while(count < 876):
    for _ in range(10):
        # print(count, end=' ')
        # print(np.array([np.array(df[x:x+18]).flatten()]).shape)
        # if _ == 9:
        try: months = np.concatenate((months, np.array([np.array(df[x:x+18]).flatten()])), axis=0)
        except: months = np.array([np.array(df[x:x+18]).flatten()])
        i += 1
        x+=19
    count += 1
    print(x/19/876)
    break
index = [i for i in range(1949,2022)]
index = [f'{i}-{j}' for i in range(1949,2022) for j in mon]
index = [1000, 925, 850, 700, 600, 500, 400, 300, 250, 200]#, 150, 100, 70, 50, 30, 20, 10]
# print(index)
# print(len(index))

months = pd.DataFrame(months, index=index)
# months.to_csv('D:/Sahaj/Raw_data/Regrid/uwnd/uwnd.csv')
print(months)

# for i, month in enumerate(months):
#     # print(month[1:].shape, len(index))
#     months[i] = pd.DataFrame(month[1:], index=index)
#     # print(months[i])
#     months[i].to_csv(f'D:/Sahaj/Raw_data/Regrid/uwnd/uwnd{i+1}.csv')

# print(months[0])