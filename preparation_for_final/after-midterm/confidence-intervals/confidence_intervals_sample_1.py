import numpy as np
from scipy.stats import t, norm

# sample 100 numbers extracted from a normal distribution
x = np.random.normal(size=100)

m = x.mean()
s = x.std()
dof = len(x) - 1
confidence = 0.95
t_crit = np.abs(norm.ppf((1 - confidence) / 2, dof))
print(t_crit)
confidenceInterval = (m-s*t_crit/np.sqrt(len(x)), m+s*t_crit/np.sqrt(len(x)))
print(confidenceInterval)