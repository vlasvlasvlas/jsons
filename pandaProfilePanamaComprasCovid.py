import numpy as np
import pandas as pd
from pandas_profiling import ProfileReport
import json

filein = '99.csv'
pathout = '99.html'

df = pd.read_csv(filein,sep=",") 
df.index += 1 
print(df)

profile = ProfileReport(df, title="panamacompras covid19 Profiling Report", minimal=True)
profile.to_file(pathout)
