
def fibonacci(target, memo = {}):
    if target in memo:
        return memo[target]
    if target <= 1:  # Condição corrigida para retornar 0 ou 1 para os primeiros números de Fibonacci
        return target
    memo[target] = fibonacci(target-1, memo) + fibonacci(target-2, memo)
    return memo[target]

print(fibonacci(13))
