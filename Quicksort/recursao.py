def gerar_lista_recursiva(n):
    if n == 1:
        return [1]
    else:
        lista_anterior = gerar_lista_recursiva(n - 1)
        lista_anterior.append(n)
        return lista_anterior

lista = gerar_lista_recursiva(10)
print(lista)
