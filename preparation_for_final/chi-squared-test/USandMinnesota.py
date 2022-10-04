import numpy as np
import pandas as pd
import scipy.stats as stats


national = pd.DataFrame(["white"]*100000 + ["hispanic"]*60000 + ["black"]*50000 + ["asian"]*15000 + ["other"]*35000)
minnesota = pd.DataFrame(["white"]*600 + ["hispanic"]*300 + ["black"]*250 + ["asian"]*75 + ["other"]*150)

national_table = pd.crosstab(index=national[0],columns="count")
minnesota_table = pd.crosstab(index=minnesota[0],columns="count")

observed = minnesota_table

national_ratios = national_table/len(national) # get the ratios
expected = national_ratios * len(minnesota) # get expected counts

chi_squared_stat = (((observed-expected)**2)/expected).sum()

print(chi_squared_stat)

print('Critical value')
crit = stats.chi2.ppf(q=0.95  #find the critical value for 95% confidence*
                      , df=4) #df = number of variable categories - 1)
print(crit)

print('P value')
p_value = 1 - stats.chi2.cdf(x=chi_squared_stat, # find the p-value
                          df=4)
print(p_value)


chi_square_scipy = stats.chisquare(f_obs = observed,f_exp = expected)
print('scipy', chi_squared_stat)