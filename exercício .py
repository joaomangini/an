import numpy as np
import pandas as pd

# Criando os arrays X e y
X = np.random.rand(100, 4)
y = np.random.randint(0, 3, 100)

# Concatenando os arrays
data = np.concatenate((X, y.reshape(-1, 1)), axis=1)

# Criando o dataframe df
df = pd.DataFrame(data, columns=['X1', 'X2', 'X3', 'X4', 'target'])

# Exibindo o dataframe
print(df)
