grafo = {}
grafo['inicio'] = {}
grafo['inicio']['a'] = 6
grafo['inicio']['b'] = 2

grafo['a'] = {}
grafo['a']['fim'] = 1

grafo['b'] = {}
grafo['b']['a'] = 3
grafo['b']['fim'] = 5

infinito = float("inf")
custos = {}
custos['a'] = 6
custos['b'] = 2
custos['fim'] = infinito

pais = {}
pais['a'] = 'inicio'
pais['b'] = 'inicio'
pais['fim'] = None

processados = []


def busca_nodo_baixo(custos):
    nodo_mais_baixo = None
    valor_mais_baixo = infinito
    for nodo in custos:
        if custos[nodo] < valor_mais_baixo and nodo not in processados:
            valor_mais_baixo = custos[nodo]
            nodo_mais_baixo = nodo
    return nodo_mais_baixo

nodo = busca_nodo_baixo(custos)

while nodo is not None:
    custo = custos[nodo]
    if nodo in grafo:  # Verifica se o nó tem vizinhos antes de acessá-los
        vizinhos = grafo[nodo]
        for n in vizinhos.keys():
            novo_custo = custo + vizinhos[n]
            if novo_custo < custos[n]:
                custos[n] = novo_custo
                pais[n] = nodo
    processados.append(nodo)
    nodo = busca_nodo_baixo(custos)

print('custos:', custos)
print('pais:', pais)


print('custos:', custos)
print('pais:', pais)
