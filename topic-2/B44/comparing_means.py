#confidence interavls comparing means
import numpy as np
from scipy.stats import t
import pandas as pd

def t2ind_confint(y1, y2, equal_var = True, alpha = 0.05):
  n1 = len(y1); n2 = len(y2)
  v1 = np.var(y1)*n1/(n1-1); v2 = np.var(y2)*n2/(n2-1)
  if equal_var:
    df = n1 + n2 - 2
    vardiff = ((n1-1)*v1+(n2-1)*v2) / (n1+n2-2)**(1/n1 + 1/n2)
  else:
    df=(v1/n1+v2/n2)**2/(v1**2/(n1**2*(n1-1))+ v2**2/(n2**2*(n2-1)))
    vardiff = v1/n1 + v2/n2
  
  se = np.sqrt(vardiff)
  qt = t.ppf(1 - alpha/2, df) # t quantile for 100(1 - alpha)% CI
  mean_diff = np.mean(y1) - np.mean(y2)
  confint = mean_diff + np.array([-1, 1]) * qt * se
  conf = 1 - alpha
  return mean_diff, confint, conf, df

Data = pd.read_csv('http://stat4ds.rwth-aachen.de/data/Anorexia.dat', sep='\s+')
diff = Data['after'] - Data['before']
Data['diff'] = diff
cogbehav = Data.loc[Data['therapy'] == 'cb']['diff']
control = Data.loc[Data['therapy'] == 'c']['diff']
# print(cogbehav)
# print(control)

# equal variance
mean_diff, confint, conf, df = t2ind_confint(cogbehav, control)
print('mean1 - mean2', mean_diff)
print(conf, 'confidence interval: ', confint)
# print('df =', df)

# unequal variance
mean_diff, confint, conf, df = t2ind_confint(cogbehav, control, equal_var=False)
print('mean1 - mean2', mean_diff)
print(conf, 'confidence interval: ', confint)
# print('df = ', df)

import statsmodels.stats.api as sms
print(sms.DescrStatsW(diff).tconfint_mean())