O propósito: codificar um programa que acessa o site https://pokeapi.co/,
baixa os dados e responde perguntas sobre os pokemons.

Essa atividade é uma AC e, como tal, pode ser feita em grupos de até 6 pessoas.
Teremos tempo nessa aula e na aula que vem para realizar a atividade

# INSTALAÇÃO

Descompacte o pokemon.zip e abra a pasta no VSCode. No cmd do VScode rode 
python -m pip install -r requirements.txt --user 
(se for linux ou mac, substitua o python por python3)

## O que esse comando está fazendo??

Instalando todas as bibliotecas que estão listadas no arquivo requirements.txt
Se quiser abrir esse arquivo, pode ver as bibliotecas listadas (requests, flask e jsons)

## problemas?

Veja a lista de problemas na sessão Erros comuns, no fim desse arquivo

# PARTE 1 da AC

na pasta pokemon>atividade, codifique sua AC no arquivo pokemon.py
para testar, rode o arquivo runtests_pokemon.py

Se precisar de ajuda, o arquivo requests_exemplo.py poderá ser útil.

Você receberá um aviso quando chegar na parte 2

# PARTE 2 da AC

Só comece a parte 2 se já tiver passado todos os testes até o 8, inclusive o 8

A segunda parte do exercicio, após fazer o pokemon_pokeapi
envolve um segundo servidor, chamado treinador. Esse segundo servidor
vai rodar no seu computador.

1) Para rodar o treinador, abra um CMD, vá para a pasta pokemon>treinador (comando cd) e digite python treinador.py. Deixe esse cmd para o servidor, se precisar fazer algo no cmd, abra outro
Comandos do CMD: dir para listar o que tem na pasta, cd para mudar de pasta
2) codifique sua AC no arquivo pokemon.py
3) No final, nao deixe de verificar todos os testes



# Erros comuns

## ERROR: Could not open requirements file: [Errno 2] No such file or directory: 'requirements.txt'
O arquivo requirements.txt não está nessa pasta. Você tem que estar na pasta exata que tem o arquivo.

Para verificar o arquivos de uma pasta, digite, no terminal do VSCode `dir`. 
O requirements tem que estar nessa lista. Se não estiver:
1. abra a pasta correta com o VSCode
OU 
2. use `dir` para listar o conteudo da pasta e `cd nome_de_outra_pasta` para mudar de pasta
   (`cd ..` para ir uma pasta acima)

## O VScode está marcando um traço vermelho na linha “import requests” (primeira linha da atividade) dizendo que a biblioteca nao existe

Rode o comando de instalação (o do requirements.txt) e tenha certeza que não houve nenhum erro

## 'python' não é reconhecido  como um comando interno ou externo
Ele está reclamando que o comando python nao é um programa válido.

Desinstalar e reinstalar o python. Ao reinstalar, marcar a opção “adicionar o python no path” ou “adicionar o python nas variaveis de ambiente” isso faz com que os comandos “python” e “pip” passem a ser comandos válidos no cmd

Depois de deinstalar e reinstalar, feche o cmd e abra um novo, pra ele carregar os novos comandos

Se quiser mais detalhes, veja em https://sites.google.com/faculdadeimpacta.com.br/ads-dam-2022-1/unidade-01/parte-02, no final do "texto de apoio", onde ele ensina a fazer os comandos python e pip ficarem disponíveis no cmd

