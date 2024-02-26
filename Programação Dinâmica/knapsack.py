def knapsack(capacidade, pesos, valores, n):
    # Inicializando a matriz para guardar os subproblemas
    dp = [[0 for _ in range(capacidade + 1)] for _ in range(n + 1)]

    # Preenchendo a matriz dp de maneira iterativa
    for i in range(n + 1):
        for w in range(capacidade + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif pesos[i - 1] <= w:
                dp[i][w] = max(valores[i - 1] + dp[i - 1][w - pesos[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacidade]

# Exemplo de utilização
pesos = [2, 3, 4, 5]
valores = [3, 4, 5, 6]
capacidade = 5
n = len(valores)
print("A quantidade máxima de valor na mochila é:", knapsack(capacidade, pesos, valores, n))
