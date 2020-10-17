import pandas as pd
import seaborn as sns

# base de dados:
iris = sns.load_dataset('iris')

df_sample = iris.sample(n=10)

df_sample.info()
