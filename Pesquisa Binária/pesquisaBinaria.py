
def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1
    tentativas = 0
    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]
        tentativas += 1
        if chute == item:
            return meio, tentativas
        elif chute < item:
            baixo = meio + 1
        else: alto = meio - 1
    return None, tentativas

minha_lista = [ 1, 3, 4, 5, 6, 7, 8]
result, tentativas = pesquisa_binaria(minha_lista, 7)
print(f'O item esta na posição: {result}')
print(f'Foram necessárias {tentativas} tentativas')
a= 400
lista = [i + 1 for i in range(a)]
#print(lista)
result2, tentativas2 = pesquisa_binaria(lista, 100)
print(f'O item esta na posição:{result2}')
print(f'Foram necessárias {tentativas2} tentativas')





        

