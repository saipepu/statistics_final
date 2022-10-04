import numpy as np
from statsmodels.stats.proportion import proportions_ztest

alpha = 0.05
success_a, sizea = (410, 500)
success_b, sizeb = (370, 500)

success = np.array([success_a, success_b])
size = np.array([sizea, sizeb])
z_stat,p_value = proportions_ztest(success, size, alternative='two-sided')

print('Z-value: ', z_stat)
print('T-value: ', p_value)

if p_value < alpha:
  print('Reject Null Hypothesis') # significance enough
else:
  print('Fail to Reject Null Hypothesis')