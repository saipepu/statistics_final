# one way ANOVA example
import scipy.stats as stats

group1 = [15, 12, 13, 14, 18,17, 17,15, 19, 25]
group2 = [30, 32, 35, 33, 34, 30, 40, 28, 39, 35]
group3 = [42, 44, 43, 39, 38, 45, 39, 47, 43, 35]

# levene test ONE WAY
levene, pvalue = stats.levene(group1, group2, group3, center = 'median')

print('The levene value is: ', levene)
print('The p-value is ', pvalue)

# F test ONE WAY
anova, pvalue = stats.f_oneway(group1, group2, group3)

print('The ANOVA value is ', anova)
print('The p-value is ', pvalue)
