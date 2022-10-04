import numpy as np
from scipy.stats import t,norm
import matplotlib.pyplot as plt

# 1 degree of freedom (df)
# 2 computatiohn of quantiles & cumulative probability
# 3 plotting the t distribution

### degree of freedom ###
df = np.array([1, 10, 30, 100, 1000, 10000])

### quantiles ###
# significance level of 5% which is 9.75% confidence interval
t_crit = t.ppf(0.975, df) # 0.975 quantiles for specified df values
print(t_crit)

### cumulative probaility ### at specified t when df = 100000
tcdf = t.cdf(t_crit[len(t_crit)-2], 10000)
print(tcdf)

y = np.linspace(-4, 4, 100)
print(y)

def t_pdfs():
  fig, ax = plt.subplots(1, 1, figsize=(10, 7))
  for i in range(6):
    ax.plot(y, t.pdf(y, df[i]))
  ax.plot(y, norm.pdf(y), lw=2, linestyle='dashed')
  ax.legend(['df=1', 'df=10', 'df=30','df=100', 'df=1000', 'df=10000', 'normal'], loc='upper right')

t_pdfs()
plt.xlabel('y')
plt.ylabel('Probability density function')
plt.show()