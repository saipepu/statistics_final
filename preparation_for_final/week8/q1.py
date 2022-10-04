from scipy.stats import ttest_1samp

data = [55, 85, 90, 30, 45, 65, 25, 72, 103, 35]
value = 60
alpha = 0.05 # 5% significance level

tscore, pvalue = ttest_1samp(data, value)
print('T statistics: ', tscore)
print('P value: ', pvalue)
if pvalue < alpha:
  print('Reject Null Hypothesis')
else:
  print('Failed to Reject Null Hypothesis')
