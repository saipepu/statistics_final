import scipy.stats as stats
import pandas as pd
import numpy as np
from statsmodels.stats.multicomp import pairwise_tukeyhsd

Facebook = [34, 24, 31, 29, 30, 28, 32, 26, 37, 36]
Youtube = [84, 91, 78, 79, 82, 88, 85, 81, 90, 85]
Tiktok = [52, 54, 43, 49, 48, 55, 49, 57, 53, 55]

levene, pvalue = stats.levene(Facebook, Youtube, Tiktok, center="median")

print('Levene: ', levene)
print('P value: ', pvalue)

# a
alpha = 0.05 # equality of variance
if pvalue < alpha:
  print('Reject Null Hypothesis')
else:
  print('Fail to Reject Null Hypothesis')

anova, pvalue = stats.f_oneway(Facebook, Youtube, Tiktok)

print('ANOVA: ', anova)
print('P value: ', pvalue)

# b
alpha = 0.05 #  difference of mean (average)
if pvalue < alpha:
  print('Reject Null Hypothesis')
else:
  print('Fail to Reject Null Hypothesis')

# c
score = Facebook + Youtube + Tiktok
df = pd.DataFrame({
  'score': score,
  'groups': np.repeat(['Facebook', 'Youtube', 'Tiktok'], repeats=10)
})

tukey = pairwise_tukeyhsd(endog = df['score'], groups = df['groups'], alpha = 0.05)
print(tukey)

import matplotlib.pyplot as plt
data = [Facebook, Youtube, Tiktok]
fig = plt.figure(figsize=(10, 7))

# Creating axes instance
ax = fig.add_axes([0, 0, 1, 1])

# Creating plot
bp = ax.boxplot(data)

plt.show()