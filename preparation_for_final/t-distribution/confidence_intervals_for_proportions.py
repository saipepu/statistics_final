from statsmodels.stats.proportion import proportion_confint

#one population proportion
p = proportion_confint(778, 1497, method="normal")
print(p) #default 95% Wald CI