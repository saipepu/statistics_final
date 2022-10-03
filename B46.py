import numpy as np
from pymc3 import *
import pandas as pd
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE,SIG_DFL) 

Data = pd.read_csv('http://stat4ds.rwth-aachen.de/data/Anorexia.dat', sep='\s+')
diff = Data['after'] - Data['before']
Data['diff'] = diff
data = dict(y = Data.loc[Data['therapy'] == 'cb']['diff'])
B0 = 10**(-7)
with Model() as model:
  sigma = InverseGamma('sigma', B0, B0, testval=1.)
  intercept = Normal('Intercept', 0, sigma=1/B0)
  likelihood = Normal('y', mu=intercept, sigma = sigma, observed=Data.loc[Data['therapy'] == 'cb']['diff'])
  trace = sample(50000, cores = 2)

print(np.mean(trace['Intercept']))
