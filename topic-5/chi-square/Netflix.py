import numpy as np
from scipy.stats import chi2_contingency

data = [[213, 202, 154, 73], [37, 48, 96, 177]]
chi, p, df, expected = chi2_contingency(data)

print('P value: ')
alpha = 0.05
if p < alpha:
  print('Reject Null Hypothesis')
else:
  print('Fail to Reject Null Hypothesis')