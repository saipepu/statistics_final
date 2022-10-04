import numpy as np
print( np.__path__)
from statsmodels.stats.proportion import proportions_ztest

count = 524 # number of success
total = 1008 # number of sample

# To analyse this is the majority of the population
# we use null hypothesis as 0.5
h_null = 0.5
# alternative hypothesis will be not 0.5

stat, pval = proportions_ztest(count, total, h_null)

if round(pval, 2) < 0.01:
  print('Null hypothesis is false')
else:
  print('Null hypothesis is true')
