import pandas as pd
from pandas_profiling import ProfileReport

df = pd.read_csv('data/mma_mart.csv')
profiling = ProfileReport(df)
profiling.to_file(output_file='output.html')