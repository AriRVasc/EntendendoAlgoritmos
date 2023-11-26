def algoritmo_de_euclides( dividendo, divisor):
    z = 1
    while(divisor):
        z = 0
        if (divisor == 0):
            return dividendo
        else:
            aux = dividendo % divisor
            dividendo = divisor 
            divisor = aux
            z = 1

print(algoritmo_de_euclides(120, 36))

def algoritmo_euclides(a, b):
    while b:
        a, b = b, a % b
    return a

num1 = 120
num2 = 36

mdc = algoritmo_euclides(num1, num2)

print(f"O MDC de {num1} e {num2} é {mdc}")
    