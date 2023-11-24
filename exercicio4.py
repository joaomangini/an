# 4.1: Filtre o dataframe df onde X1 é maior do que 6 ou target é diferente de 2
df1 = df[(df['X1'] > 6) | (df['target'] != 2)]

# 4.2: Filtre os primeiros 15 índices do dataframe df
df2 = df.head(15)

# 4.3: Transformando os dataframes df1 e df2 para arrays e multiplicando
array_df1 = df1.drop('target_2', axis=1).to_numpy()
array_df2 = df2.drop('target_2', axis=1).to_numpy()
result = np.dot(array_df1, array_df2.T)
print(result)
