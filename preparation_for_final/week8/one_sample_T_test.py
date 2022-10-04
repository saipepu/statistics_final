from scipy.stats import ttest_1samp

weather = [26.5, 28.1, 29.4, 30.5, 30.1, 29.4, 29, 28.8, 28.6, 28.3, 27.5, 26.1]
pop_mean = 30
alpha = 0.05
tscore, pvalue = ttest_1samp(weather, pop_mean)
print("T statistics: ", tscore)
print("P value: ", pvalue)
if (pvalue < tscore):
  print("Reject Null Hypothesis")
else:
  print('Fail to reject Null Hypothesis')
