from scipy.stats import ttest_rel

alpha = 0.05 # 5%  significance level
pre = [30, 31, 34, 40, 36, 35, 34, 30, 38, 39]
post = [30, 31, 32, 38, 32, 31, 32, 29, 28, 30]
# post = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

t_value, p_value = ttest_rel(pre, post)
print('T-value: ', t_value)
print('P-vaue: ', p_value)
if p_value < alpha:
  print('Reject Null Hypothesis')
  # it is significance that the alternative hypothesis is strong enough to reject the null
  # which means there is significant improvement after the new training
else:
  print('Failed to Reject Null Hypothesis')
