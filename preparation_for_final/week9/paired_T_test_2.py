from scipy.stats import ttest_rel

before = [67, 74, 58, 45, 78, 79, 61, 83, 70, 69]
after = [89, 75, 64, 71, 80, 82, 92, 81, 73, 75]
alpha = 0.1 # 10% significance test

t_value, p_value = ttest_rel(before, after)
print('T value: ', t_value)
print('P value: ', p_value)
if p_value < alpha:
  print('Reject Null Hypothesis') # significance enough
else:
  print('Failed to Reject Null Hypothesis')
