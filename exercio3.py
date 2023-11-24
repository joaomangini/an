# Criando o dicionário de mapeamento
mapping = {0: 'A', 1: 'B', 2: 'C'}

# Criando a coluna 'target_2' usando a função map
df['target_2'] = df['target'].map(mapping)
print(df)
