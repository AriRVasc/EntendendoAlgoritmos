from collections import deque

grafo = {}
grafo["Ari"] = ["Maris", "Jessic", "Raul"]
grafo["Maris"] = ["Mara", "Leci"]
grafo["Jessic"] = ["Ana", "Rachel"]
grafo["Raul"] = ["Reginaldo"]

def pessoa_vendedora(pessoa):
    return pessoa[-1] == 'a'

def pesquisa(nome):
    fila_de_pesquisa = deque()
    fila_de_pesquisa += [nome]  # Adiciona o nome inicial à fila
    pessoas_verificadas = set()

    while fila_de_pesquisa:
        pessoa = fila_de_pesquisa.popleft()
        if pessoa not in pessoas_verificadas:
            if pessoa_vendedora(pessoa):
                print(pessoa + " vende mangas")
                return True
            else:
                fila_de_pesquisa.extend(grafo.get(pessoa, []))
                pessoas_verificadas.add(pessoa)

    return False

pesquisa("Ari")
