from statsmodels.stats.proportion import proportions_ztest
import numpy as np

alpha = 0.02
success_a, size_a = (560, 1000)
success_b, size_b = (486, 1000)

success = np.array([success_a, success_b])
size = np.array([size_a, size_b])
zscore, pvalue = proportions_ztest(success, size, alternative='two-sided')

print('Zscore: ', zscore)
print('P value: ', pvalue)

if pvalue < alpha:
  print('Reject Null Hypothesis')
else:
  print('Fail to Reject Null Hypothesis')
  