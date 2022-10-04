import pandas as pd
import numpy as np
from scipy.stats import f_oneway
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.DataFrame({ 'score': [15, 12, 13, 14, 18,17, 17,15, 19, 25,
                              30, 32, 35, 33, 34, 30, 40, 28, 39, 35,
                              42, 44, 43, 39, 38, 45, 39, 47, 43, 35],
                    'group': np.repeat(['group1','group2','group3'], repeats=10)})

tukey = pairwise_tukeyhsd(endog = df['score'], groups = df['group'], alpha = 0.05)
print(tukey)
# sns.boxplot(tukey)
# plt.show()
