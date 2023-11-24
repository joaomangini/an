# Calculando a média da variável 'X2' para cada valor de 'target'
mean_X2_by_target = df.groupby('target')['X2'].mean()
print(mean_X2_by_target)
