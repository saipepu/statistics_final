import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import statsmodels.stats.api as sms

patient = pd.read_csv('http://stat4ds.rwth-aachen.de/data/Anorexia.dat', sep='\s+')
print(patient.head(3))

diff = patient['after'] - patient['before']
patient['diff'] = diff

# a) mean and std changes (difference between before and after)
changes = patient.loc[patient['therapy'] == 'cb']['diff'].describe()
print(changes)
print(changes.loc['min'])

# conduct 95% confidence mean change
print(sms.DescrStatsW(changes).tconfint_mean()) # default 0.05

# conduct 99% confidence mean change
print(sms.DescrStatsW(changes).tconfint_mean(alpha = 0.01))
bins = list(range(-10, 30, 5)) # histrogram with pre-specifited bins:
# plt.hist(patient.loc[patient['therapy'] == 'cb']['diff'], bins, edgecolor='k')
# plt.xlabel('Weight Change')
# plt.ylabel('Frequency')
# plt.show()

# changes =  patient.loc[patient['therapy'] == 'cb']['diff'].describe()  - patient.loc[patient['therapy'] == 'c']['diff'].describe()
# changes =  patient.loc[patient['therapy'] == 'cb']['diff'].describe()
# print(changes)
# patient['diff 1'] = changes
# print(sms.DescrStatsW(changes).tconfint_mean(alpha = 0.05))