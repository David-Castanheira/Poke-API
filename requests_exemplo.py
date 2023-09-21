# esse arquivo explica a biblioteca requests, uma biblioteca para acessar paginas
# da internet através do python

import requests

#para instalar a biblioteca, rodar no cmd
#windows:   python -m pip install requests
#linux/mac: python3 -m pip install requests

# r = requests.get("https://viacep.com.br/ws/48400000/json/") #baixar a url
# #confira essa mesma URL no firefox, para ver o dicionário que estamos baixando

# print(r.status_code) #O pedido acima deve ter dado certo, então esse número deve ser 200
# # O viacep.com.br devolverá um número dizendo se tudo está ok, ou, se houve erro,
# # qual foi esse erro. Se acessarmos uma URL inválida, ele deve retornar 400 ou 404,
# # em vez de 200

# dici = r.json() #pega o arquivo baixado e transforma num dicionario de python 
# Transformar um arquivo em dados acessíveis pelo python é uma coisa
# que chamamos decodificar ou desserializar

# print(dici)
# print(dici['localidade']) #o dicionario que baixamos tem uma chave localidade
# print(dici['bairro'])

def cep_to_cidade(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    r = requests.get(url)
    dici = r.json()
    return dici['localidade']

print("48400000", cep_to_cidade("48400000"))
print("03675020", cep_to_cidade("03675020"))