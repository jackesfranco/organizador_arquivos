# Pegando o diretório de onde está o arquivo e organizando, sem mover o arquivo exe de organizar junto

import os

diretorio_local = os.getcwd()
os.chdir(diretorio_local)

lista_arquivos = [arquivo.lower() for arquivo in os.listdir() if os.path.isfile(arquivo)]
lista_tipos = {tipo.split(".")[-1] for tipo in lista_arquivos}

for tipo in lista_tipos:
    if os.path.exists(tipo):
        pass
    else:
        os.mkdir(tipo)

for arquivo in lista_arquivos:
    pasta_destino = arquivo.split(".")[-1]
    de = os.path.join(os.getcwd(), arquivo)
    para = os.path.join(os.getcwd(), pasta_destino, arquivo)
    if os.path.exists(de):
        os.replace(de, para)
        arq = os.path.join(f"{diretorio_local}\\exe","organizador_local.exe")
    if os.path.exists(arq):
        os.replace(arq, de)