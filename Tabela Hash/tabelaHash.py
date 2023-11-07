
def inserir(tabela_hash, chave, valor):
    indice = funcao_de_hash(chave)
    if tabela_hash[indice] is None:
        tabela_hash[indice] = [(chave, valor)]
    else:
        for i, (ch, val) in enumerate(tabela_hash[indice]):
            if ch == chave:
                tabela_hash[indice][i] = (chave, valor)
                break
        else:
            tabela_hash[indice].append((chave, valor))

def buscar(tabela_hash, chave):
    indice = funcao_de_hash(chave)
    if tabela_hash[indice] is not None:
        for k, v in tabela_hash[indice]:
            if k == chave:
                return v
    return None


def funcao_de_hash(chave):
    #  hash(chave) gera um valor hash único para objetos 
    return hash(chave) % tamanho_da_tabela

tamanho_da_tabela = 100
#inicializar a tabela hash como uma lista de tamanho fixo preenchida com None:
tabela_hash = [None] * tamanho_da_tabela

# Inserir elementos na tabela hash
inserir(tabela_hash, "chave1", "valor1")
inserir(tabela_hash, "chave2", "valor2")

# Buscar valores na tabela hash
resultado1 = buscar(tabela_hash, "chave1")
resultado2 = buscar(tabela_hash, "chave2")
resultado3 = buscar(tabela_hash, "chave3")

print(resultado1)  # Saída: "valor1"
print(resultado2)  # Saída: "valor2"
print(resultado3)  # Saída: None (chave3 não existe na tabela)
