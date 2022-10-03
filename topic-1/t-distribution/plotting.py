import numpy as np
from scipy.stats import t, norm
import matplotlib.pyplot as plt

# 1 degree of freedom (df)
# 2 computation of quantiles & cumulative probability
# 3 plotting the t distribution

df = np.array([5, 50, 500, 5000])

confidence = 0.975
t_crit = t.ppf(confidence, df)
print(t_crit)

for i in range(len(df)):
  tcdf = t.cdf(t_crit[i], df)
  print(tcdf)

y = np.linspace(-4, 4, 100)
print(y)

def t_pdfs():
  fig, ax = plt.subplots(1, 1, figsize=(10, 7))
  for i in range(4):
    ax.plot(y, t.pdf(y, df[i]))

  ax.plot(y, norm.pdf(y), lw=2, linestyle='dashed')
  ax.legend(['df=5', 'df=50', 'df=500', 'df=5000', 'normal'], loc='upper right')

t_pdfs()
plt.xlabel('y')
plt.ylabel('Probability density function')
plt.show()