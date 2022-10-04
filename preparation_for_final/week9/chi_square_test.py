import numpy as np
from scipy.stats import chi2_contingency

data = [[ 63, 37, 45], [26, 74, 55]]
chi_stat, p, dof, expected = chi2_contingency(data)
alpha = 0.05
print('P value is ', p)
if (p<=alpha):
  print('Reject Null Hypothesis')
  print('no relationship between 2 categories')
else:
  print('Fail to Reject Null Hypothesis')
  print('the 2 categories can be related')
