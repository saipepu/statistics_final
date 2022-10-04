import numpy as np
from statsmodels.stats.proportion import proportions_ztest

# null hypothesis is two proportions are the same
alpha = 0.1 # 10% significance level
success_a , size_a = (795, 1000)
success_b, size_b = (175, 500)
success = np.array([success_a, success_b])
size = np.array([size_a, size_b])

z_stat, p_value = proportions_ztest(success, size, alternative="two-sided")
print('Z value: ', z_stat)
print('P value: ', p_value)
if p_value < alpha:
  print('Reject Null Hypothesis')
  # there is strong evidence against the null hypothesis,
else:
  print('Fail to Reject Null Hypothesis')