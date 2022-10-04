from statsmodels.stats.proportion import proportion_confint
print(proportion_confint(814, 1142, method="jeffreys"))

import pymc3
from scipy.stats import beta
beta_dist = beta.rvs(size=5000000, a=814.5, b=328.5)
# print(pymc3.stats.hpd(beta_dist, alpha=0.05))

import numpy as np
print('[', np.quantile(beta_dist, 0.025), ',', np.quantile(beta_dist,0.975),']')

import arviz as az

print(az.hdi(beta_dist, alpha=0.05))