#voce nao precisa fazer nada nesse arquivo
# codifique sua AC no arquivo pokemon.py, e teste com runtests_pokemon.py

import jsons

def to_dict(obj):
    return jsons.dump(obj, strip_privates = True)

def to_dict_list(lista):
    resultado = []
    for item in lista:
        resultado.append(to_dict(item))
    return resultado