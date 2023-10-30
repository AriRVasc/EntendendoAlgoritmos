#Backup do sistema de vendas
meses_sistema = ["jan2023", "fev2023", "mar2023", "abr2023", "mai2022", "jun2022", "jul2022", "dez2022"]
print(len(meses_sistema))

import os #percorrer pastas no computador

lista_pastas = []

def pegar_arquivos_pasta(pasta):
    arquivos = os.listdir(pasta)
    for arquivo in arquivos:
        if "txt" in arquivo and "Vendas" in arquivo:
            nome_mes = arquivo.split()[-1].replace(".txt", "")
            lista_pastas.append(nome_mes)
        elif "txt" not in arquivo:
            pegar_arquivos_pasta(f'{pasta}/{arquivo}')

pegar_arquivos_pasta("Arquivos")
print(lista_pastas)

for mes in meses_sistema:
    if mes not in lista_pastas:
        print(mes)