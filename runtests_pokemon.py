import unittest
from requests import api

class TestPokeapi(unittest.TestCase):
    
    def test_01a_ok(self):
        verificar_online("pokeapi")
        self.assertEqual(nome_do_pokemon(1), "bulbasaur")
        self.assertEqual(nome_do_pokemon(55), "golduck")
        self.assertEqual(nome_do_pokemon(25), "pikachu")
        self.assertEqual(nome_do_pokemon(700), "sylveon")
        self.assertEqual(nome_do_pokemon(807), "zeraora")

    
    def test_02a_ok(self):
        self.assertEqual(numero_do_pokemon("marill"), 183)

    
    def test_02b_caps(self):
        self.assertEqual(numero_do_pokemon("EEVEE"), 133)
        self.assertEqual(numero_do_pokemon("Psyduck"), 54)
        self.assertEqual(numero_do_pokemon("SkiTtY"), 300)
        self.assertEqual(numero_do_pokemon("Zeraora"), 807)

    
    def test_02c_nao_existe(self):
        pokemon_nao_existe(lambda : numero_do_pokemon("DOBBY"), self)
        pokemon_nao_existe(lambda : numero_do_pokemon("Peppa-Pig"), self)
        pokemon_nao_existe(lambda : numero_do_pokemon("batman"), self)
        pokemon_nao_existe(lambda : numero_do_pokemon("SpiderMan"), self)

    
    def test_03a_ok(self):
        self.assertEqual(color_of_pokemon("marill"), "blue")
        self.assertEqual(color_of_pokemon("togekiss"), "white")
        self.assertEqual(color_of_pokemon("magneton"), "gray")

    
    def test_03b_caps(self):
        self.assertEqual(color_of_pokemon("EEVEE"), "brown")
        self.assertEqual(color_of_pokemon("Psyduck"), "yellow")
        self.assertEqual(color_of_pokemon("SkiTtY"), "pink")
        self.assertEqual(color_of_pokemon("GASTLY"), "purple")
        self.assertEqual(color_of_pokemon("LeDyBa"), "red")
        self.assertEqual(color_of_pokemon("Torterra"), "green")
        self.assertEqual(color_of_pokemon("xurkiTree"), "black")

    
    def test_03c_nao_existe(self):
        pokemon_nao_existe(lambda : color_of_pokemon("DOBBY"), self)
        pokemon_nao_existe(lambda : color_of_pokemon("Peppa-Pig"), self)
        pokemon_nao_existe(lambda : color_of_pokemon("batman"), self)
        pokemon_nao_existe(lambda : color_of_pokemon("SpiderMan"), self)

    
    def test_04a_ok(self):
        self.assertEqual(cor_do_pokemon("marill"), "azul")
        self.assertEqual(cor_do_pokemon("togekiss"), "branco")

    
    def test_04b_caps(self):
        self.assertEqual(cor_do_pokemon("EEVEE"), "marrom")
        self.assertEqual(cor_do_pokemon("Psyduck"), "amarelo")
        self.assertEqual(cor_do_pokemon("SkiTtY"), "rosa")
        self.assertEqual(cor_do_pokemon("magneton"), "cinza")
        self.assertEqual(cor_do_pokemon("GASTLY"), "roxo")
        self.assertEqual(cor_do_pokemon("LeDyBa"), "vermelho")
        self.assertEqual(cor_do_pokemon("Torterra"), "verde")
        self.assertEqual(cor_do_pokemon("xurkiTree"), "preto")

    
    def test_04c_nao_existe(self):
        pokemon_nao_existe(lambda : cor_do_pokemon("DOBBY"), self)
        pokemon_nao_existe(lambda : cor_do_pokemon("Peppa-Pig"), self)
        pokemon_nao_existe(lambda : cor_do_pokemon("batman"), self)
        pokemon_nao_existe(lambda : cor_do_pokemon("SpiderMan"), self)

    
    def test_05a_ok(self):
        self.assert_equals_unordered_list(["grama"], tipos_do_pokemon("chikorita"))
        self.assert_equals_unordered_list(["terra"], tipos_do_pokemon("hippowdon"))
        self.assert_equals_unordered_list(["normal", "fada"], tipos_do_pokemon("jigglypuff"))
        self.assert_equals_unordered_list(["fogo"], tipos_do_pokemon("darumaka"))
        self.assert_equals_unordered_list(["pedra", "voador"], tipos_do_pokemon("archeops"))

    
    def test_05b_caps(self):
        self.assert_equals_unordered_list(["voador", "noturno"], tipos_do_pokemon("murKrow"))
        self.assert_equals_unordered_list(["água", "elétrico"], tipos_do_pokemon("cHinChou"))
        self.assert_equals_unordered_list(["lutador", "fantasma"], tipos_do_pokemon("MARSHADOW"))
        self.assert_equals_unordered_list(["aço"], tipos_do_pokemon("KLINK"))
        self.assert_equals_unordered_list(["lutador", "inseto"], tipos_do_pokemon("Heracross"))
        self.assert_equals_unordered_list(["veneno", "noturno"], tipos_do_pokemon("DRAPION"))
        self.assert_equals_unordered_list(["psíquico", "gelo"], tipos_do_pokemon("JYNX"))
        self.assert_equals_unordered_list(["dragão"], tipos_do_pokemon("dRaTiNi"))

    
    def test_05c_nao_existe(self):
        pokemon_nao_existe(lambda : tipos_do_pokemon("DOBBY"), self)
        pokemon_nao_existe(lambda : tipos_do_pokemon("Peppa-Pig"), self)
        pokemon_nao_existe(lambda : tipos_do_pokemon("batman"), self)
        pokemon_nao_existe(lambda : tipos_do_pokemon("SpiderMan"), self)

    
    def test_06a_ok(self):
        self.assertEqual(evolucao_anterior("togetic"), "togepi")

    
    def test_06b_caps(self):
        self.assertEqual(evolucao_anterior("togeKiss"), "togetic")
        self.assertEqual(evolucao_anterior("EEleKtriK"), "tynamo")
        self.assertEqual(evolucao_anterior("EELEKTROSS"), "eelektrik")
        self.assertEqual(evolucao_anterior("Pikachu"), "pichu")
        self.assertEqual(evolucao_anterior("rAiChu"), "pikachu")

    
    def test_06c_nao_tem(self):
        self.assertIs(evolucao_anterior("togepi"), None)
        self.assertIs(evolucao_anterior("TYNAMO"), None)
        self.assertIs(evolucao_anterior("Pichu"), None)

    
    def test_06d_nao_existe(self):
        pokemon_nao_existe(lambda : evolucao_anterior("DOBBY"), self)
        pokemon_nao_existe(lambda : evolucao_anterior("Peppa-Pig"), self)
        pokemon_nao_existe(lambda : evolucao_anterior("batman"), self)
        pokemon_nao_existe(lambda : evolucao_anterior("SpiderMan"), self)

    def test_07_pulado(self):
        pass #depois te mostro esse exercicio, pode ir pro 8
      
    def test_08a_simples(self):
        self.assertEqual(nivel_do_pokemon("blastoise",   110000), 49) # 4
        self.assertEqual(nivel_do_pokemon("mewtwo",     1000000), 92) # 1
        self.assertEqual(nivel_do_pokemon("Magikarp",       900),  8) # 1
        self.assertEqual(nivel_do_pokemon("Magikarp",   1000000), 92) # 1
        self.assertEqual(nivel_do_pokemon("SLOWBRO",      65000), 40) # 2
        self.assertEqual(nivel_do_pokemon("OcTiLLeRy",   280000), 65) # 2
        self.assertEqual(nivel_do_pokemon("FRAXURE",     280000), 60) # 1
        self.assertEqual(nivel_do_pokemon("lunatone",     20000), 29) # 3
        self.assertEqual(nivel_do_pokemon("skitty",       50000), 39) # 3
        self.assertEqual(nivel_do_pokemon("torchic",      40000), 35) # 4
        self.assertEqual(nivel_do_pokemon("ODDISH",        5000), 19) # 4

    
    def test_08b_complexos(self):
        self.assertEqual(nivel_do_pokemon("zangoose",      9000), 17) # 5
        self.assertEqual(nivel_do_pokemon("milotic",      65000), 37) # 5
        self.assertEqual(nivel_do_pokemon("Lumineon",    160000), 55) # 5
        self.assertEqual(nivel_do_pokemon("NINJASK",     300000), 72) # 5
        self.assertEqual(nivel_do_pokemon("zangoose",    580000), 97) # 5
        self.assertEqual(nivel_do_pokemon("makuhita",       600), 10) # 6
        self.assertEqual(nivel_do_pokemon("gulpin",        7000), 21) # 6
        self.assertEqual(nivel_do_pokemon("seviper",     150000), 50) # 6
        self.assertEqual(nivel_do_pokemon("drifblim",   1000000), 87) # 6

    
    def test_08c_limites(self):
        self.assertEqual(nivel_do_pokemon("pinsir",           0),   1) # 1
        self.assertEqual(nivel_do_pokemon("bibarel",          0),   1) # 2
        self.assertEqual(nivel_do_pokemon("aipom",            0),   1) # 3
        self.assertEqual(nivel_do_pokemon("Makuhita",         0),   1) # 6
        self.assertEqual(nivel_do_pokemon("Magikarp",      1249),   9) # 1
        self.assertEqual(nivel_do_pokemon("MeTaPoD",        999),   9) # 2
        self.assertEqual(nivel_do_pokemon("Magikarp",      1250),  10) # 1
        self.assertEqual(nivel_do_pokemon("Butterfree",    1000),  10) # 2
        self.assertEqual(nivel_do_pokemon("charmeleon",   29948),  32) # 4
        self.assertEqual(nivel_do_pokemon("charmeleon",   29949),  33) # 4
        self.assertEqual(nivel_do_pokemon("hariyama",     71676),  40) # 6
        self.assertEqual(nivel_do_pokemon("hariyama",     71677),  41) # 6
        self.assertEqual(nivel_do_pokemon("togePI",      799999),  99) # 3
        self.assertEqual(nivel_do_pokemon("gengar",     1059859),  99) # 4
        self.assertEqual(nivel_do_pokemon("zangoose",    599999),  99) # 5
        self.assertEqual(nivel_do_pokemon("SWALot",     1639999),  99) # 6
        self.assertEqual(nivel_do_pokemon("sYLVEON",    1000000), 100) # 2
        self.assertEqual(nivel_do_pokemon("Jigglypuff", 1000000), 100) # 3
        self.assertEqual(nivel_do_pokemon("LEDIAN",      800000), 100) # 3
        self.assertEqual(nivel_do_pokemon("vaPorEON", 999999999), 100) # 2
        self.assertEqual(nivel_do_pokemon("VILEPLUME",  1059860), 100) # 4
        self.assertEqual(nivel_do_pokemon("zangoose",    600000), 100) # 5
        self.assertEqual(nivel_do_pokemon("SWALOT",     1640000), 100) # 6

    
    def test_08d_nao_existe(self):
        pokemon_nao_existe(lambda : nivel_do_pokemon("DOBBY", 1234), self)
        pokemon_nao_existe(lambda : nivel_do_pokemon("Peppa-Pig", 1234), self)
        pokemon_nao_existe(lambda : nivel_do_pokemon("batman", 1234), self)
        pokemon_nao_existe(lambda : nivel_do_pokemon("SpiderMan", 1234), self)

    def reset(self):
        resposta = requests.post(f"{site_treinador}/reset")
        self.assertEqual(resposta.status_code, 200)

    
    def test_09a_ok(self):
        verificar_online("pokeapi+treinador")
        self.reset()

        resposta = requests.get(f"{site_treinador}/treinador")
        self.assertEqual(resposta.json(), {})
        
        self.assertTrue(cadastrar_treinador("Ash Ketchum"))

        self.assertTrue(cadastrar_treinador("Misty"))

        resposta = requests.get(f"{site_treinador}/treinador")
        self.assertEqual(resposta.json(), {
            "Ash Ketchum": {"nome": "Ash Ketchum", "pokemons": {}},
            "Misty": {"nome": "Misty", "pokemons": {}}
        })

    
    def test_09b_limpeza(self):
        self.reset()
        self.assertTrue(cadastrar_treinador("Jessie"))
        self.assertTrue(cadastrar_treinador("James"))
        self.reset()
        resposta = requests.get(f"{site_treinador}/treinador")
        self.assertEqual(resposta.json(), {})

    
    def test_09c_repetido(self):
        self.reset()
        self.assertTrue(cadastrar_treinador("Jessie"))
        self.assertFalse(cadastrar_treinador("Jessie"))
        
        resposta = requests.get(f"{site_treinador}/treinador")
        self.assertEqual(resposta.json(), {
            "Jessie": {"nome": "Jessie", "pokemons": {}}
        })

        

    
    def test_10a_ok(self):
        self.reset()

        oldMaxDiff = self.maxDiff
        self.maxDiff = None
        
        self.assertTrue(cadastrar_treinador("Ash Ketchum"))
        cadastrar_pokemon("Ash Ketchum", "P", "Pikachu", 50000)
        self.assertTrue(cadastrar_treinador("Misty"))
        cadastrar_pokemon("Misty", "A", "STARYU", 10000)
        cadastrar_pokemon("Misty", "B", "sTaRyU", 12000)
        self.assertTrue(cadastrar_treinador("Brock"))
        cadastrar_pokemon("Brock", "O", "onix", 8000)
        cadastrar_pokemon("Brock", "G", "Geodude", 20000)
        self.assertTrue(cadastrar_treinador("James"))
        cadastrar_pokemon("James", "A", "KOFFING", 5000)
        cadastrar_pokemon("James", "B", "MeowTH", 20000)

        resposta = requests.get(f"{site_treinador}/treinador")
        self.assertEqual(resposta.json(), {
            "Ash Ketchum": {"nome": "Ash Ketchum", "pokemons": {"P": {"apelido": "P", "tipo": "pikachu", "experiencia": 50000}}},
            "Misty": {"nome": "Misty", "pokemons": {"A": {"apelido": "A", "tipo": "staryu", "experiencia": 10000}, "B": {"apelido": "B", "tipo": "staryu", "experiencia": 12000}}},
            "Brock": {"nome": "Brock", "pokemons": {"O": {"apelido": "O", "tipo": "onix", "experiencia": 8000}, "G": {"apelido": "G", "tipo": "geodude", "experiencia": 20000}}},
            "James": {
                "nome": "James",
                "pokemons": {
                    "A": {"apelido": "A", "tipo": "koffing", "experiencia": 5000},
                    "B": {"apelido": "B", "tipo": "meowth", "experiencia": 20000}
                }
            }
        })
        self.maxDiff = oldMaxDiff

    
    def test_10b_treinador_nao_existe(self):
        self.reset()
        treinador_nao_cadastrado(lambda : cadastrar_pokemon("Max", "D", "lapras", 40000), self)
        self.assertEqual(requests.get(f"{site_treinador}/treinador").json(), {})

    
    def test_10c_pokemon_nao_existe(self):
        self.reset()
        self.assertTrue(cadastrar_treinador("Iris"))
        pokemon_nao_existe(lambda : cadastrar_pokemon("Iris", "D", "homer", 40000), self)
        resposta = requests.get(f"{site_treinador}/treinador")
        self.assertEqual(resposta.json(), {
            "Iris": {"nome": "Iris", "pokemons": {}}
        })

    
    def test_10d_pokemon_ja_existe(self):
        self.reset()
        self.assertTrue(cadastrar_treinador("Misty"))
        cadastrar_pokemon("Misty", "estrela", "STARMIE", 40000)
        pokemon_ja_cadastrado(lambda : cadastrar_pokemon("Misty", "estrela", "staryu", 1000), self)

        resposta = requests.get(f"{site_treinador}/treinador")
        self.assertEqual(resposta.json(), {
            "Misty": {"nome": "Misty", "pokemons": {"estrela": {"apelido": "estrela", "tipo": "starmie", "experiencia": 40000}}}
        })

    
    def test_10e_treinador_errado(self):
        self.reset()
        self.assertTrue(cadastrar_treinador("Ash Ketchum"))
        treinador_nao_cadastrado(lambda : cadastrar_pokemon("Gary", "pi", "pikachu", 40000), self)
        resposta = requests.get(f"{site_treinador}/treinador")
        self.assertEqual(resposta.json(), {
            "Ash Ketchum": {"nome": "Ash Ketchum", "pokemons": {}}
        })
    
    
    def test_11f_treinador_repetido(self):
        self.reset()
        self.assertTrue(cadastrar_treinador("Jessie"))
        self.assertFalse(cadastrar_treinador("Jessie"))
        
        resposta = requests.get(f"{site_treinador}/treinador")
        self.assertEqual(resposta.json(), {
            "Jessie": {"nome": "Jessie", "pokemons": {}}
        })

        
        cadastrar_pokemon("Jessie", "A", "ARBOK", 20000)
        cadastrar_pokemon("Jessie", "B", "wobbuffet", 2000)
        cadastrar_pokemon("Jessie", "C", "Lickitung", 2500)
        self.assertFalse(cadastrar_treinador("Jessie"))

        resposta = requests.get(f"{site_treinador}/treinador")
        self.assertEqual(resposta.json(), {
            "Jessie": {
                "nome": "Jessie",
                "pokemons": {
                    "A": {"apelido": "A", "tipo": "arbok", "experiencia": 20000},
                    "B": {"apelido": "B", "tipo": "wobbuffet", "experiencia": 2000},
                    "C": {"apelido": "C", "tipo": "lickitung", "experiencia": 2500}
                }
            }
        })

    
    def test_11a_ok(self):
        self.reset()

        self.assertTrue(cadastrar_treinador("Ash Ketchum"))
        cadastrar_pokemon("Ash Ketchum", "P", "pikachu", 50000)
        ganhar_experiencia("Ash Ketchum", "P", 1500)

        self.assertTrue(cadastrar_treinador("James"))
        cadastrar_pokemon("James", "P", "WEEZING", 10000)
        cadastrar_pokemon("James", "Q", "VictREeBEL", 12000)
        ganhar_experiencia("James", "P", 2500)

        resposta = requests.get(f"{site_treinador}/treinador")
        self.assertEqual(resposta.json(), {
            "Ash Ketchum": {"nome": "Ash Ketchum", "pokemons": {"P": {"apelido": "P", "tipo": "pikachu", "experiencia": 51500}}},
            "James": {"nome": "James", "pokemons": {"P": {"apelido": "P", "tipo": "weezing", "experiencia": 12500}, "Q": {"apelido": "Q", "tipo": "victreebel", "experiencia": 12000}}}
        })

    
    def test_11b_treinador_nao_existe(self):
        self.reset()
        treinador_nao_cadastrado(lambda : ganhar_experiencia("Cilan", "bob-esponja", 10000), self)
        self.assertEqual(requests.get(f"{site_treinador}/treinador").json(), {})

    
    def test_11c_pokemon_nao_existe(self):
        self.reset()
        self.assertTrue(cadastrar_treinador("Bonnie"))
        pokemon_nao_cadastrado(lambda : ganhar_experiencia("Bonnie", "bob-esponja", 40000), self)

        resposta = requests.get(f"{site_treinador}/treinador")
        self.assertEqual(resposta.json(), {
            "Bonnie": {"nome": "Bonnie", "pokemons": {}}
        })

    
    def test_11d_treinador_errado(self):
        self.reset()
        self.assertTrue(cadastrar_treinador("Serena"))
        self.assertTrue(cadastrar_treinador("Dawn"))
        cadastrar_pokemon("Serena", "fen", "fennekin", 5000)
        pokemon_nao_cadastrado(lambda : ganhar_experiencia("Dawn", "fen", 100), self)

        resposta = requests.get(f"{site_treinador}/treinador")
        self.assertEqual(resposta.json(), {
            "Serena": {"nome": "Serena", "pokemons": {"fen": {"apelido": "fen", "tipo": "fennekin", "experiencia": 5000}}},
            "Dawn": {"nome": "Dawn", "pokemons": {}}
        })

    
    def test_12a_ok(self):
        self.reset()

        self.assertTrue(cadastrar_treinador("Ash Ketchum"))
        cadastrar_pokemon("Ash Ketchum", "P", "pikachu", 50000)

        self.assertTrue(cadastrar_treinador("James"))
        cadastrar_pokemon("James", "P", "WEEZING", 10000)
        cadastrar_pokemon("James", "Q", "Gloom", 12000)

        pikachu = localizar_pokemon("Ash Ketchum", "P")
        weezing = localizar_pokemon("James", "P")
        gloom = localizar_pokemon("James", "Q")

        self.assertIs(type(pikachu), Pokemon)
        self.assertEqual(pikachu.nome_treinador, "Ash Ketchum")
        self.assertEqual(pikachu.apelido, "P")
        self.assertEqual(pikachu.tipo, "pikachu")
        self.assertEqual(pikachu.experiencia, 50000)
        self.assertEqual(pikachu.nivel, 36)
        self.assertEqual(pikachu.cor, "amarelo")
        self.assertEqual(pikachu.evoluiu_de, "pichu")

        self.assertIs(type(weezing), Pokemon)
        self.assertEqual(weezing.nome_treinador, "James")
        self.assertEqual(weezing.apelido, "P")
        self.assertEqual(weezing.tipo, "weezing")
        self.assertEqual(weezing.experiencia, 10000)
        self.assertEqual(weezing.nivel, 21)
        self.assertEqual(weezing.cor, "roxo")
        self.assertEqual(weezing.evoluiu_de, "koffing")

        self.assertIs(type(gloom), Pokemon)
        self.assertEqual(gloom.nome_treinador, "James")
        self.assertEqual(gloom.apelido, "Q")
        self.assertEqual(gloom.tipo, "gloom")
        self.assertEqual(gloom.experiencia, 12000)
        self.assertEqual(gloom.nivel, 25)
        self.assertEqual(gloom.cor, "azul")
        self.assertEqual(gloom.evoluiu_de, "oddish")

    
    def test_12b_treinador_nao_existe(self):
        self.reset()
        treinador_nao_cadastrado(lambda : localizar_pokemon("Cilan", "bob-esponja"), self)
        self.assertEqual(requests.get(f"{site_treinador}/treinador").json(), {})

    
    def test_12c_pokemon_nao_existe(self):
        self.reset()
        self.assertTrue(cadastrar_treinador("Bonnie"))
        pokemon_nao_cadastrado(lambda : localizar_pokemon("Bonnie", "bob-esponja"), self)

        resposta = requests.get(f"{site_treinador}/treinador")
        self.assertEqual(resposta.json(), {
            "Bonnie": {"nome": "Bonnie", "pokemons": {}}
        })

    
    def test_12d_treinador_errado(self):
        self.reset()
        self.assertTrue(cadastrar_treinador("Serena"))
        self.assertTrue(cadastrar_treinador("Dawn"))
        cadastrar_pokemon("Serena", "fen", "fennekin", 5000)
        pokemon_nao_cadastrado(lambda : localizar_pokemon("Dawn", "fen"), self)

        resposta = requests.get(f"{site_treinador}/treinador")
        self.assertEqual(resposta.json(), {
            "Serena": {"nome": "Serena", "pokemons": {"fen": {"apelido": "fen", "tipo": "fennekin", "experiencia": 5000}}},
            "Dawn": {"nome": "Dawn", "pokemons": {}}
        })

    
    def test_13a_ok(self):
        self.reset()

        self.assertTrue(cadastrar_treinador("Ash Ketchum"))
        cadastrar_pokemon("Ash Ketchum", "P", "pikachu", 50000)

        self.assertTrue(cadastrar_treinador("James"))
        cadastrar_pokemon("James", "P", "WEEZING", 10000)
        cadastrar_pokemon("James", "Q", "WeepinBElL", 12000)

        ash = detalhar_treinador("Ash Ketchum")
        james = detalhar_treinador("James")

        self.assertEqual(ash, {"P": "pikachu"})
        self.assertEqual(james, {"P": "weezing", "Q": "weepinbell"})

    
    def test_13b_treinador_nao_existe(self):
        self.reset()
        treinador_nao_cadastrado(lambda : detalhar_treinador("Cilan"), self)
        self.assertEqual(requests.get(f"{site_treinador}/treinador").json(), {})

    
    def test_14a_ok(self):
        self.reset()

        self.assertTrue(cadastrar_treinador("Ash Ketchum"))
        cadastrar_pokemon("Ash Ketchum", "P", "pikachu", 50000)

        self.assertTrue(cadastrar_treinador("Prof. Carvalho"))

        self.assertTrue(cadastrar_treinador("James"))
        cadastrar_pokemon("James", "P", "WEEZING", 10000)
        cadastrar_pokemon("James", "Q", "WeepinBElL", 12000)

        excluir_treinador("Ash Ketchum")

        resposta1 = requests.get(f"{site_treinador}/treinador")
        self.assertEqual(resposta1.json(), {
            "James": {"nome": "James", "pokemons": {"P": {"apelido": "P", "tipo": "weezing", "experiencia": 10000}, "Q": {"apelido": "Q", "tipo": "weepinbell", "experiencia": 12000}}},
            "Prof. Carvalho": {"nome": "Prof. Carvalho", "pokemons": {}}
        })
        treinador_nao_cadastrado(lambda : detalhar_treinador("Ash Ketchum"), self)
        treinador_nao_cadastrado(lambda : localizar_pokemon("Ash Ketchum", "P"), self)

        excluir_treinador("James")

        resposta2 = requests.get(f"{site_treinador}/treinador")
        self.assertEqual(resposta2.json(), {
            "Prof. Carvalho": {"nome": "Prof. Carvalho", "pokemons": {}}
        })
        treinador_nao_cadastrado(lambda : detalhar_treinador("James"), self)
        treinador_nao_cadastrado(lambda : localizar_pokemon("James", "P"), self)
        treinador_nao_cadastrado(lambda : localizar_pokemon("James", "Q"), self)

        excluir_treinador("Prof. Carvalho")

        resposta3 = requests.get(f"{site_treinador}/treinador")
        self.assertEqual(resposta3.json(), {})
        treinador_nao_cadastrado(lambda : detalhar_treinador("Prof. Carvalho"), self)

    
    def test_14b_treinador_nao_existe(self):
        self.reset()

        treinador_nao_cadastrado(lambda : excluir_treinador("Kiawe"), self)
        self.assertEqual(requests.get(f"{site_treinador}/treinador").json(), {})

        self.assertTrue(cadastrar_treinador("Kiawe"))
        cadastrar_pokemon("Kiawe", "c", "charizard", 50000)
        treinador_nao_cadastrado(lambda : excluir_treinador("Lillie"), self)
        resposta = requests.get(f"{site_treinador}/treinador")
        self.assertEqual(resposta.json(), {
            "Kiawe": {"nome": "Kiawe", "pokemons": {"c": {"apelido": "c", "tipo": "charizard", "experiencia": 50000}}}
        })

        excluir_treinador("Kiawe")
        self.assertEqual(requests.get(f"{site_treinador}/treinador").json(), {})

    
    def test_15a_ok(self):
        self.reset()

        self.assertTrue(cadastrar_treinador("Ash Ketchum"))
        cadastrar_pokemon("Ash Ketchum", "P", "pikachu", 50000)

        self.assertTrue(cadastrar_treinador("Prof. Carvalho"))

        self.assertTrue(cadastrar_treinador("James"))
        cadastrar_pokemon("James", "P", "WEEZING", 10000)
        cadastrar_pokemon("James", "Q", "WeepinBElL", 12000)

        excluir_pokemon("Ash Ketchum", "P")

        resposta1 = requests.get(f"{site_treinador}/treinador")
        self.assertEqual(resposta1.json(), {
            "Ash Ketchum": {"nome": "Ash Ketchum", "pokemons": {}},
            "James": {"nome": "James", "pokemons": {"P": {"apelido": "P", "tipo": "weezing", "experiencia": 10000}, "Q": {"apelido": "Q", "tipo": "weepinbell", "experiencia": 12000}}},
            "Prof. Carvalho": {"nome": "Prof. Carvalho", "pokemons": {}}
        })
        pokemon_nao_cadastrado(lambda : localizar_pokemon("Ash Ketchum", "P"), self)
        localizar_pokemon("James", "P")
        localizar_pokemon("James", "Q")

        excluir_pokemon("James", "Q")

        resposta2 = requests.get(f"{site_treinador}/treinador")
        self.assertEqual(resposta2.json(), {
            "Ash Ketchum": {"nome": "Ash Ketchum", "pokemons": {}},
            "James": {"nome": "James", "pokemons": {"P": {"apelido": "P", "tipo": "weezing", "experiencia": 10000}}},
            "Prof. Carvalho": {"nome": "Prof. Carvalho", "pokemons": {}}
        })
        pokemon_nao_cadastrado(lambda : localizar_pokemon("Ash Ketchum", "P"), self)
        localizar_pokemon("James", "P")
        pokemon_nao_cadastrado(lambda : localizar_pokemon("James", "Q"), self)

        excluir_pokemon("James", "P")

        resposta3 = requests.get(f"{site_treinador}/treinador")
        self.assertEqual(resposta3.json(), {
            "Ash Ketchum": {"nome": "Ash Ketchum", "pokemons": {}},
            "James": {"nome": "James", "pokemons": {}},
            "Prof. Carvalho": {"nome": "Prof. Carvalho", "pokemons": {}}
        })
        pokemon_nao_cadastrado(lambda : localizar_pokemon("Ash Ketchum", "P"), self)
        pokemon_nao_cadastrado(lambda : localizar_pokemon("James", "P"), self)
        pokemon_nao_cadastrado(lambda : localizar_pokemon("James", "Q"), self)

    
    def test_15b_treinador_nao_existe(self):
        self.reset()

        self.assertTrue(cadastrar_treinador("Kiawe"))
        cadastrar_pokemon("Kiawe", "c", "charizard", 50000)
        treinador_nao_cadastrado(lambda : excluir_pokemon("Lillie", "c"), self)
        resposta = requests.get(f"{site_treinador}/treinador")
        self.assertEqual(resposta.json(), {
            "Kiawe": {"nome": "Kiawe", "pokemons": {"c": {"apelido": "c", "tipo": "charizard", "experiencia": 50000}}}
        })

        localizar_pokemon("Kiawe", "c")
        self.assertEqual(requests.get(f"{site_treinador}/treinador").json(), {
            "Kiawe": {"nome": "Kiawe", "pokemons": {"c": {"apelido": "c", "tipo": "charizard", "experiencia": 50000}}}
        })

    
    def test_15c_pokemon_nao_existe(self):
        self.reset()

        self.assertTrue(cadastrar_treinador("Kiawe"))
        cadastrar_pokemon("Kiawe", "c", "charizard", 50000)
        pokemon_nao_cadastrado(lambda : excluir_pokemon("Kiawe", "d"), self)
        resposta = requests.get(f"{site_treinador}/treinador")
        self.assertEqual(resposta.json(), {
            "Kiawe": {"nome": "Kiawe", "pokemons": {"c": {"apelido": "c", "tipo": "charizard", "experiencia": 50000}}}
        })

        localizar_pokemon("Kiawe", "c")
        self.assertEqual(requests.get(f"{site_treinador}/treinador").json(), {
            "Kiawe": {"nome": "Kiawe", "pokemons": {"c": {"apelido": "c", "tipo": "charizard", "experiencia": 50000}}}
        })

        excluir_pokemon("Kiawe", "c")
        self.assertEqual(requests.get(f"{site_treinador}/treinador").json(), {
            "Kiawe": {"nome": "Kiawe", "pokemons": {}}
        })

    def test_16a_ok_evolucoes_simples(self):
        self.assert_equals_unordered_list(["charmeleon"], evolucoes_proximas("charmander"))
        self.assert_equals_unordered_list(["combusken"], evolucoes_proximas("torchic"))
        self.assert_equals_unordered_list(["charizard"], evolucoes_proximas("ChArMeLeON"))

    
    def test_16b_ok_nao_tem_simples(self):
        self.assert_equals_unordered_list([], evolucoes_proximas("lugia"))
        self.assert_equals_unordered_list([], evolucoes_proximas("turtonator"))
        self.assert_equals_unordered_list([], evolucoes_proximas("CHARIZARD"))
        self.assert_equals_unordered_list([], evolucoes_proximas("gEnGar"))
        self.assert_equals_unordered_list([], evolucoes_proximas("ALAkazam"))

    
    def test_16c_ok_evolucoes_complexas(self):
        self.assert_equals_unordered_list(["ninjask", "shedinja"], evolucoes_proximas("nincada"))
        self.assert_equals_unordered_list(["vaporeon", "jolteon", "flareon", "espeon", "umbreon", "leafeon", "glaceon", "sylveon"], evolucoes_proximas("eevee"))
        self.assert_equals_unordered_list(["hitmonlee", "hitmonchan", "hitmontop"], evolucoes_proximas("tyrogue"))
        self.assert_equals_unordered_list(["poliwhirl"], evolucoes_proximas("Poliwag"))
        self.assert_equals_unordered_list(["gloom"], evolucoes_proximas("oDDiSH"))
        self.assert_equals_unordered_list(["poliwrath", "politoed"], evolucoes_proximas("PoliWHIRL"))
        self.assert_equals_unordered_list(["vileplume", "bellossom"], evolucoes_proximas("GLOOM"))

    
    def test_16d_ok_nao_tem_complexas(self):
        self.assert_equals_unordered_list([], evolucoes_proximas("espeon"))
        self.assert_equals_unordered_list([], evolucoes_proximas("Leafeon"))
        self.assert_equals_unordered_list([], evolucoes_proximas("POLITOED"))

    
    def test_16e_nao_existe(self):
        pokemon_nao_existe(lambda : evolucoes_proximas("DOBBY"), self)
        pokemon_nao_existe(lambda : evolucoes_proximas("Peppa-Pig"), self)
        pokemon_nao_existe(lambda : evolucoes_proximas("batman"), self)
        pokemon_nao_existe(lambda : evolucoes_proximas("SpiderMan"), self)


    
    def test_98a_limpeza(self):
        self.reset()
        self.assertTrue(cadastrar_treinador("Tracey"))
        cadastrar_pokemon("Tracey", "m", "MARILL", 40000)

        self.reset()
        treinador_nao_cadastrado(lambda : detalhar_treinador("Tracey"), self)
        treinador_nao_cadastrado(lambda : localizar_pokemon("Tracey", "m"), self)
        treinador_nao_cadastrado(lambda : ganhar_experiencia("Tracey", "m", 4000), self)
        treinador_nao_cadastrado(lambda : cadastrar_pokemon("Tracey", "t", "togepi", 500), self)
        treinador_nao_cadastrado(lambda : excluir_pokemon("Tracey", "t"), self)
        treinador_nao_cadastrado(lambda : excluir_treinador("Tracey"), self)

        resposta = requests.get(f"{site_treinador}/treinador")
        self.assertEqual(resposta.json(), {})

    def test_99a_print(self):
        sem_io.test_print(self)

    def test_99b_input(self):
        sem_io.test_input(self)



def runTests():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestPokeapi)
    unittest.TextTestRunner(verbosity = 2, failfast = True).run(suite)
    #unittest.TextTestRunner(verbosity = 0, failfast = False).run(suite)


from requests import api, exceptions
from pokemon import *

def verificar_online(desejado):

    def pokeapi_online():
        try:
            resposta1 = api.get(f"{site_pokeapi}/api/v2/")
            if resposta1.status_code == 200 and resposta1.json()['pokemon'] == f'{site_pokeapi}/api/v2/pokemon/':
                return "online"
            return "zumbi"
        except exceptions.ConnectionError as x:
            return "offline"
        except:
            return "zumbi"

    def treinador_online():
        try:
            resposta2 = api.get(f"{site_treinador}/hello")
            if resposta2.status_code == 200 and resposta2.text == 'Pikachu, eu escolho você!':
                return "online"
            return "zumbi"
        except exceptions.ConnectionError as x:
            return "offline"
        except:
            return "zumbi"

    #if site_treinador != "http://127.0.0.1:9000" or site_pokeapi != "http://127.0.0.1:8000": raise Exception("As URLs para as APIs estão incorretas.")
    y = pokeapi_online()
    z = treinador_online()

    if y in ("zumbi","offline"): raise Exception("Para poder rodar os testes, você precisa de acesso ao pokeapi. Verifique se você tem esse acesso.")
    if desejado == "pokeapi+treinador":
        if y == "zumbi" or z == "zumbi": raise Exception("Os servidores aparentemente não estão em funcionamento. Estes testes só devem ser executados com ambos os servidores on-line.")
        if y == "offline" and z == "offline": raise Exception("Os servidores estão off-line. Estes testes só devem ser executados com ambos os servidores on-line.")
        if y == "online" and z == "offline": raise Exception("O treinador está off-line. A partir do teste 09, ele precisa estar online")
        if y == "offline" and z == "online": raise Exception("O pokeapi está off-line. Estes testes só devem ser executados com ambos os servidores on-line.")
        assert y == "online" and z == "online"
    

def verificar_erro(interno, tipo_erro, tests = None):
    if tests is None:
        try:
            interno()
        except Exception as x:
            assert type(x) is tipo_erro, f"Esperava-se que um erro do tipo {tipo_erro.__name__}, mas obteve-se uma do tipo {x.__class__.__name__}."
        else:
            assert False, f"Esperava-se que um erro do tipo {tipo_erro.__name__} fosse produzido, mas não foi."
    else:
        try:
            interno()
        except Exception as x:
            tests.assertIs(type(x), tipo_erro, f"Esperava-se que um erro do tipo {tipo_erro.__name__}, mas obteve-se uma do tipo {x.__class__.__name__}.")
        else:
            tests.fail(f"Esperava-se que um erro do tipo {tipo_erro.__name__} fosse produzido, mas não foi.")

def pokemon_nao_existe(interno, tests = None):
    verificar_erro(interno, PokemonNaoExisteException, tests)

def pokemon_nao_cadastrado(interno, tests = None):
    verificar_erro(interno, PokemonNaoCadastradoException, tests)

def treinador_nao_cadastrado(interno, tests = None):
    verificar_erro(interno, TreinadorNaoCadastradoException, tests)

def pokemon_ja_cadastrado(interno, tests = None):
    verificar_erro(interno, PokemonJaCadastradoException, tests)

def valor_errado(interno, tests = None):
    verificar_erro(interno, ValueError, tests)

def assert_equals_unordered_list(esperada, obtida, tests = None):
    error_string = f"Esperava-se que o resultado fosse {esperada}, mas foi {obtida}."
    if tests is None:
        assert len(esperada) == len(obtida), error_string
        for item in esperada:
            assert item in obtida, error_string
    else:
        tests.assertEqual(len(esperada), len(obtida), error_string)
        for item in esperada:
            tests.assertIn(item, obtida, error_string)

def assert_equals_unordered_list_clear(self, esperada, obtida):
    assert_equals_unordered_list(esperada, obtida, self)

class NoStdIO:
    def __init__(self):
        import sys
        self.__oout = sys.stdout
        self.__oin = sys.stdin
        self.__usou_print = False
        self.__usou_input = False

    def __enter__(self):
        import sys
        self.__oout = sys.stdout
        self.__oin = sys.stdin
        sys.stdout = self
        sys.stdin = self

    def __exit__(self, a, b, c):
        import sys
        sys.stdout = self.__oout
        sys.stdin = self.__oin

    def write(self, str):
        self.__usou_print = True
        return self.__oout.write(str)

    def readline(self):
        self.__usou_input = True
        return self.__oin.readline()

    def flush(self):
        pass

    @property
    def usou_print(self):
        return self.__usou_print

    @property
    def usou_input(self):
        return self.__usou_input

    def __call__(self, delegate):
        from functools import wraps
        @wraps(delegate)
        def sem_input(*args, **kwargs):
            with self:
                return delegate(*args, **kwargs)
        return sem_input

    def test_print(self, tests = None):
        if tests is None:
            assert self.usou_print == False, "Você não deveria utilizar a função print neste exercício."
        else:
            tests.assertFalse(self.usou_print, "Você não deveria utilizar a função print neste exercício.")

    def test_input(self, tests = None):
        if tests is None:
            assert self.usou_input == False, "Você não deveria utilizar a função input neste exercício."
        else:
            tests.assertFalse(self.usou_input, "Você não deveria utilizar a função print neste exercício.")

sem_io = NoStdIO()
TestPokeapi.assert_equals_unordered_list = assert_equals_unordered_list_clear

# try:
#     import sys
#     sys.path.append("../")
#     from pokemon_gabarito import *
# except:
#     pass


if __name__ == '__main__':
    runTests()
