import numpy as np
import pandas as pd

df = pd.DataFrame({'week': np.repeat(['first', 'second', 'third'], 10),
                    'match': np.tile(np.repeat(['home', 'away'], 5), 3),
                    'score': [23, 24, 22, 28, 30, 14, 15, 18, 13, 20,
                              31, 33, 28, 30, 25, 21, 22, 25, 21, 19,
                              35, 34, 32, 30, 28, 26, 24, 21, 25, 20]})
print(df)
import statsmodels.api as sm
from statsmodels.formula.api import ols
model = ols('score ~ C(week) + C(match) + C(week):C(match)', data=df).fit()
print(sm.stats.anova_lm(model, type = 2 ))
