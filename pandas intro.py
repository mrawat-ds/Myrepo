import numpy as np 
import pandas as pd 
df = pd.read_csv('/Users/manojrawat/downloads/data/survey_results_public.csv')
print(df.shape)
print(df.info)
df.iloc[0]
df.iloc[[0,3]]

df.iloc[[0,3],2]
df.loc[0]
df.loc[[0,1],'Respondent']
