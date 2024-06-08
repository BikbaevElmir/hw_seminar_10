import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
lst1 = []
arr = data.to_numpy()
for value in arr:
    if value == 'robot':
        lst1.append({'whoAmI_robot':1,'whoAmI_human':0})
    else:
        lst1.append({'whoAmI_robot':0,'whoAmI_human':1})
data1 = pd.DataFrame(lst1)
data1.head()
print(data)
print(data1)