import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('./Anorexia_1.txt', sep='\s+')
data.head(3)
print(data.head(3))
x = np.array(data.head(3)['after'])
x = pd.DataFrame({ 'after' : x})
print(x)
change = data['after'] - data['before']
# print(change)
data['change'] = change

# showing only n and mean and standard deviation of change
print(data.loc[data['therapy'] == 'cb']['change'].describe)

bins = list(range(-10, 30, 5)) # histogram with pre-sepcified bins:
plt.hist(data.loc[data['therapy'] == 'cb']['change'], bins, edgecolor='k')
plt.xlabel('Weight change')
plt.ylabel('Frequency')
plt.show()


import statsmodels.stats.api as sms
changeCB = data.loc[data['therapy'] == 'cb']['change']
# 95% confidence interval for mean
print(sms.DescrStatsW(changeCB).tconfint_mean(alpha=0.05))

# 99% confidence interval for mean
print(sms.DescrStatsW(changeCB).tconfint_mean(alpha=0.01))
