import numpy as np
from statsmodels.stats.proportion import proportions_ztest

alpha = 0.02
success_a, size_a = (560, 1000) # AIS
success_b, size_b = (500, 1000) # TRUE
success = np.array([success_a, success_b])
size = np.array([size_a, size_b])

z_stats, p_value = proportions_ztest(success, size, alternative='two-sided')
print('Z value: ', z_stats)
print('P value: ', p_value)

if p_value < alpha:
  print('Reject Null Hypothesis')
else:
  print('Failed to Reject Null Hypothesis')