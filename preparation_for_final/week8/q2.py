from statsmodels.stats.proportion import proportions_ztest

count = 225
total = 400
value = 0.4 # 40% of customer procced
alpha = 0.01 #  1% significance level

zscore, pvalue = proportions_ztest(count, total, value)
print('Z statistics: ', zscore)
print('P value: ', pvalue)
if pvalue < alpha:
  print('Rejected Null Hypothesis')
else:
  print('Failed to Reject Null Hypothesis')