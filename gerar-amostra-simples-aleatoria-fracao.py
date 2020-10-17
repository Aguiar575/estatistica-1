import pandas as pd
import seaborn as sns

# base de dados:
iris = sns.load_dataset('iris')

# 10%:
df_sample = iris.sample(frac=0.10)

df_sample.info()