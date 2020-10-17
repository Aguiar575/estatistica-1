import numpy as np
import seaborn as sns

# base de dados:
iris = sns.load_dataset('iris')

# Selecionado um registro aleatório entre os valores de 0 a 10:
N = np.random.choice(10, 1)

print('Número aleatório escolhido: %s', N)

# Geramos um array que vai de 0 a 100 com espaço de tempo N:
array = np.arange(0,100,N)

#geramos a amostra com base nos valores do array
amostra = iris.loc[array,:]

amostra.info()




