# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json 

CAMINHO = 'C:\\Users\\guilh\\OneDrive\\Documentos\\curso_python_udemy\\03_POO\\01_classes\\aula127.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa('João', 23)
p2 = Pessoa('Maria', 32)

bd = [vars(p1), vars(p2)]

def fazer_dump():
    with open(CAMINHO, 'w', encoding='utf8') as arquivo:
        json.dump(bd,arquivo, ensure_ascii=False, indent = 2)

if __name__ == 'main':
    print('ele é o Main')
    fazer_dump()