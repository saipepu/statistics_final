import scipy.stats as stats
import pandas as pd
import numpy as np
from statsmodels.stats.multicomp import pairwise_tukeyhsd

FaceBook = [34, 24, 31, 29, 30, 28, 32, 26, 37, 36]
YouTube = [84, 91, 78, 79, 82, 88, 85, 81, 90, 85]
TikTok = [52, 54, 43, 49, 48, 55, 49, 57, 53, 55]

# a -> equality of variance at 5%
alpha = 0.05
levene, pvalue = stats.levene(FaceBook, YouTube, TikTok, center='median')
print('The levene value is: ', levene)
print('The p-value is ', pvalue)

if pvalue < alpha:
  print('HA - At least one population variance is difference')
else:
  print('H0 - All population variances are equal')

print()
# b -> difference of average spending times on each social network at 5%
alpha = 0.05
anova, pvalue = stats.f_oneway(FaceBook, YouTube, TikTok)
print('The ANOVA value is ', anova)
print('The p-value is ', pvalue)

if pvalue < alpha:
  print('HA - At least one population is difference')
else:
  print('H0 - There is no differences between the population')

print()
# Tukey HSD and draw box-plot 5% significance level

df = pd.DataFrame({
  'score': [34, 24, 31, 29, 30, 28, 32, 26, 37, 36,
            84, 91, 78, 79, 82, 88, 85, 81, 90, 85,
            52, 54, 43, 49, 48, 55, 49, 57, 53, 55],
  'group': np.repeat(['FaceBook', 'YouTube', 'TikTok'], repeats=10)
})

tukey = pairwise_tukeyhsd(endog = df['score'], groups = df['group'], alpha = 0.05)
print(tukey)