import pandas as pd
import statsmodels.api as sm
from scipy.stats import chi2_contingency
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame({
  'Gender': ['M', 'M','M', 'F', 'F'] * 10,
  'isSmoker': ['Smoker', 'Smoker', 'Non-smoker', 'Non-smoker', 'Smoker'] * 10
})

contigency = pd.crosstab(df['Gender'], df['isSmoker'])
print(type(contigency))
print(contigency)
# contigency = sm.stats.Table(contigency)
# print(type(contigency))
# print(contigency)
c, p, dof, expected = chi2_contingency(contigency) # cannot be normalized
print(p)

# plt.figure(figsize=(12, 8))
# sns.heatmap(contigency, annot=True, cmap='YlGnBu')
# plt.show()