tamanho_tabela = 100

def funcao_hash(chave):
    return hash(chave) % tamanho_tabela

def inserir_tabela(tabela_hash, chave, valor):
    #cria a função de espalhamento
    indice = funcao_hash(chave)
    if tabela_hash[indice] is None:
        tabela_hash[indice] = [(chave, valor)]
    else:
        #percorre todos as posições da lista no indice indicado
        for i, (ch, vl) in enumerate(tabela_hash[indice]):
            if ch == chave:
                #atualiza o novo valor para a chave encontrada
                tabela_hash[indice][i] = (chave, valor)
                break
            #adiciona o novo elemento ao final da lista encadeada:
            else: tabela_hash[indice].append(chave, valor)

def busca_tabela(tabela_hash, chave):
    indice = funcao_hash(chave)
    if tabela_hash[indice] is not None:
        for ch, vl in tabela_hash[indice]:
            if ch == chave:
                return vl
    return None


#inicializar a tabela hash como uma lista de tamanho fixo preenchida com None:
tabela_hash = [None] * tamanho_tabela

inserir_tabela(tabela_hash, "Valor1", 123)
inserir_tabela(tabela_hash, "Valor2", 456)

result1 = busca_tabela(tabela_hash,"Valor1")
result2 = busca_tabela(tabela_hash,"Valor2")
result3 = busca_tabela(tabela_hash,"Valor3")

print(result1)
print(result2)
print(result3)


