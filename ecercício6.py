def divide_dados(X, p):
    # Calculando o tamanho de X1 com base no percentual p
    size_X1 = int(p * X.shape[0])

    # Embaralhando as linhas de X
    np.random.shuffle(X)

    # Dividindo X em X1 e X2
    X1 = X[:size_X1, :]
    X2 = X[size_X1:, :]

    return X1, X2
