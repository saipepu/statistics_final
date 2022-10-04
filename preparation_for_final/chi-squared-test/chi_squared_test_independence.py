import numpy as np
import scipy.stats as stats
import pandas as pd

np.random.seed(10)
# sample data randomly at fixed probabilities
voter_race = np.random.choice(a=['asian', 'black', 'hispanic', 'other', 'white'],
                              p=[0.05,0.15,0.25,0.05,0.5], size=1000)

# sample data randomly at fixed probabilities
voter_party = np.random.choice(a=["democrat","independent","republican"],
                              p=[0.4,0.2,0.4], size=1000)

voters = pd.DataFrame({"race": voter_race,
                      "party": voter_party})

voter_tab = pd.crosstab(voters.race, voters.party, margins=True)

voter_tab.columns = ["democrat","independent","republican","row_totals"]
voter_tab.index = ['asian', 'black', 'hispanic', 'other', 'white',"col_totals"]

observed = voter_tab.iloc[0:5, 0:3]
print(voter_tab)


expected = np.outer(voter_tab["row_totals"][0:5],
                    voter_tab.loc["col_totals"][0:3]) / 1000

expected = pd.DataFrame(expected)

expected.columns = ["democrat","independent","republican"]
expected.index = ['asian', 'black', 'hispanic', 'other', 'white']
print(expected)
print(observed)

chi_squared_stat = (((observed-expected)**2)/expected).sum().sum()
print(chi_squared_stat)

crit = stats.chi2.ppf(q=0.95,df=8)
print('Critical value\n',crit)

p_value = 1 - stats.chi2.cdf(x=chi_squared_stat, df=8)
print("P value\n", p_value)