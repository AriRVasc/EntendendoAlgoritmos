#Backup do sistema de vendas

meses_sistema = ["jan2022", "fev2022", "mar2022", "abr2022", "mai2022", "jun2022", "jul2022", "ago2022", "set2022", "out2022", "nov2022", "dez2022"]
print(len(meses_sistema))

import os #percorrer pastas no computador

arquivos_extraidos = []
def pegar_arquivos_pasta(pasta):
    arquivo = os.listdir(pasta)
    print(arquivo)
    pass

pegar_arquivos_pasta("Arquivos")
