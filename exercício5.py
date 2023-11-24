# 5.1: Crie uma função que receba um número inteiro positivo N e retorne um array 0, 1, ..., N
def create_array(N):
    return np.arange(N+1)

# 5.2: Crie uma função que receba um array [0,1, .., N] e retorne o mesmo array, só que com os números em posições aleatórias
def shuffle_array(arr):
    np.random.shuffle(arr)
    return arr

# 5.3: Crie uma função que receba um número inteiro positivo N e retorne um array de tamanho N, cujos valores são números inteiros entre 0 e N-1 e pode haver repetição desses números
def random_array_with_repetition(N):
    return np.random.choice(N, N, replace=True)
