import numpy as np
from scipy.stats import chi2_contingency

data = [[213, 202, 154, 72], [37, 48, 96, 177]]
chi_stat, p, dof, expected = chi2_contingency(data)
alpha= 0.05
print('P value is ', p)
if (p<=alpha):
  print('Reject Null Hypothesis')
  print('No relationship between 2 categories')
else:
  print('Failed to Reject Nul Hypothesis')
  print('2 Categories can be related')