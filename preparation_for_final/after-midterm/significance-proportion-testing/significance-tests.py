import numpy as np
from statsmodels.stats.proportion import proportions_ztest

stat, pval = proportions_ztest(524, 1008, 0.5) # hypo value -> 0.5
# print('{0:0.4f},'.format(stat),'{0:0.4f}'.format(pval))
print(round(stat, 4), round(pval, 4))

from statsmodels.stats.proportion import proportion_confint
print(proportion_confint(524, 1008, method='wilson'))

from statsmodels.stats.proportion import proportions_ztest
from scipy.stats import norm

count_success = ([315, 304])
sample = ([604, 597])
stat, pval = proportions_ztest(count_success, sample)
print(round(stat, 4), round(pval, 4))

# confidence = 0.95
# z_crit = np.abs(norm.ppf((1-confidence) / 2))
# print(z_crit)

print('stat= ', round(stat, 4), 'stat= ', round(pval, 4))