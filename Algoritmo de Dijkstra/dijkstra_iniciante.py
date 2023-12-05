import math

grafo = {}
grafo["a"] = {}
grafo["a"]["b"] = 5
grafo["a"]["c"] = 2

grafo["c"] = {}
grafo["c"]["b"] = 8
grafo["c"]["e"] = 7

grafo["e"] = {}
grafo["e"]["f"] = 1

grafo["b"] = {}
grafo["b"]["d"] = 4
grafo["b"]["e"] = 2

grafo["d"] = {}
grafo["d"]["e"] = 6
grafo["d"]["f"] = 3

grafo["f"] = {}

infinito = float('inf')
custos = {}
custos["b"] = 5
custos["c"] = 2
custos["d"] = infinito
custos["e"] = infinito
custos["f"] = infinito

pais = {}
pais["b"] = "a"
pais["c"] = "a"
pais["d"] = None
pais["e"] = None
pais["f"] = None

def nodo_mais_baixo(custos):
    nodo_custo_mais_baixo = None
    custo_mais_baixo = float('inf')
    for nodo in custos:
        if custos[nodo] < custo_mais_baixo and nodo not in processados:
            custo_mais_baixo = custos[nodo]
            nodo_custo_mais_baixo = nodo
    return nodo_custo_mais_baixo


    return nodo

processados=[]
nodo = nodo_mais_baixo(custos)
while nodo is not None:
    custo = custos[nodo]
    vizinhos = grafo[nodo]
    for n in vizinhos.keys():
        novo_custo = custo + vizinhos[n]
        if novo_custo < custos[n]:
            custos[n] = novo_custo
            pais[n] = nodo
    processados.append(nodo)
    nodo = nodo_mais_baixo(custos)


print("Custos:", custos)
print("Pais:", pais)