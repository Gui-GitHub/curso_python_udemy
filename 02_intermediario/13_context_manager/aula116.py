import os

# Leia também: https://www.otaviomiranda.com.br/2020/normalizacao-unicode-em-python/
# Criando arquivos com Python + Context Manager with
# with open (context manager) e métodos úteis do TextIOWrapper
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)

# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)

# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)

# Python tem dificuldade com \, então usamos \\ no Windows
# C:\\Users\\guilh\\OneDrive\\Documentos\\curso_python_udemy\\02_intermediario\\13_context_manager\\aula116.txt
caminho_arquivo = 'C:\\Users\\guilh\\OneDrive\\Documentos\\curso_python_udemy\\02_intermediario\\13_context_manager\\aula116.txt'

# arquivo = open(caminho_arquivo, 'w')
# arquivo.close()

with open(caminho_arquivo, 'w+') as arquivo: # Colocando + para que ele também consiga ler o arquivo!
    arquivo.write('Linha 1\n') # Escreve uma linha
    arquivo.write('Linha 2\n')
    arquivo.writelines( # Escreve multiplas linhas
        ('Linha 3\n', 'Linha 4\n')
    )
    arquivo.seek(0, 0) # Volta para o inicio do arquivo
    print(arquivo.read()) # Ler o arquivo
    print('Lendo')
    arquivo.seek(0, 0)
    print(arquivo.readline(), end='') # Como se fosse um next, le um por um
    print(arquivo.readline().strip()) # Remove espaços, no caso as quebras de linhas
    print(arquivo.readline().strip())

    print('READLINES')
    arquivo.seek(0, 0)
    for linha in arquivo.readlines(): # Le diversas linhas do arquivo
        print(linha.strip())

print('#' * 10)

with open(caminho_arquivo, 'r') as arquivo:
    print(arquivo.read())

# w Apaga o que estava no arquivo e executa o comando
# a Não apaga nada do arquiov, começa a executar no fim do arquivo (Ótimo para Logs)

with open(caminho_arquivo, 'w', encoding='utf8') as arquivo: # Importante usar encoding='utf8', para padronizar
     arquivo.write('Atenção\n')
     arquivo.write('Linha 1\n')
     arquivo.write('Linha 2\n')
     arquivo.writelines(
         ('Linha 3\n', 'Linha 4\n')
     )

# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.renameS - troca o nome ou move o arquivo

with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
    arquivo.write('Atenção\n')
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.writelines(
        ('Linha 3\n', 'Linha 4\n')
    )

os.remove(caminho_arquivo) # ou unlink
os.rename(caminho_arquivo, 'aula116-2.txt') # import os na primeira linha