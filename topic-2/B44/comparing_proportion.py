import numpy as np
from scipy.stats import norm

def prop2_confint(y1, n1, y2, n2, alpha = 0.05):
  # y1, y2 : number of successes in groups A and B
  # n1, n2 : sample sizes in groups A and B
  prop1 = y1/n1; prop2 = y2/n2
  var = prop1*(1 - prop1)/n1 + prop2*(1-prop2)/n2
  se = np.sqrt(var)
  qz = norm.ppf(1 - alpha/2)
  prop_diff = prop1 - prop2

  confint = prop_diff + np.array([-1, 1]) * qz * se
  conf = 1 - alpha # level
  return prop_diff, confint, conf

prop_diff, confint, conf = prop2_confint(315, 604, 304, 597)
print('prop1 - prop2 =', prop_diff)
print(conf, 'confidence interval: ', confint)