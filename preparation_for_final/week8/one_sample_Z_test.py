from statsmodels.stats.weightstats import ztest

data = [23, 26, 32, 33, 21, 29, 28, 36, 34, 41, 21, 30, 39, 37, 16, 25, 24, 23, 38, 19]
alpha = 0.05
zscore, pvalue = ztest(data, value = 30)
print("Z statistics: ", zscore)
print("P value: ", pvalue)
if(pvalue < alpha):
  print("Reject Null Hypothesis")
else:
  print("Fail to reject Null Hypothesis")