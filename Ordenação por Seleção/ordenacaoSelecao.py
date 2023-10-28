
def buscaMenor(arr):
    menor = arr[0]
    menor_indice = 0
    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor_indice = i
            menor = arr[i]
    return menor_indice

def ordenacaoPorSelecao(arr):
    novoArr = []
    for i in range(len(arr)):
        menor = buscaMenor(arr)
        novoArr.append(arr.pop(menor))
    return novoArr

print (ordenacaoPorSelecao([6, 9, 20, 1, 23, 18]))

#O Python já possui suas próprias funções para ordenar listas, são elas:
#sorted para criar nova lista ordenada:
lista = [1, 5, 6, 3, 49, 22, 4]
lista_ordenada = sorted(lista)
print (lista_ordenada)

#sort para alterar a lista já existente
lista2 = [1,9,11,333,4,55,14]
lista2.sort()
print(lista2)

