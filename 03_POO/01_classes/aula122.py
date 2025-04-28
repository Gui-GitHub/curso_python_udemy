# Entendendo self em classes Python
# Classe - Molde (geralmente sem dados)
# Instância da class (objeto) - Tem os dados
# Uma classe pode gerar várias instâncias.
# Na classe o self é a própria instância.

class Carro:
    def __init__(self, nome): #self é uma convenção mas poderia usar qualquer nome em primeiro
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando...')


fusca = Carro('Fusca')
fusca.acelerar()
Carro.acelerar(fusca) # Aqui eu preciso passar o argumento, dizer quem é o self, pois ele é o molde
# print(fusca.nome)

celta = Carro(nome='Celta')
celta.acelerar()
Carro.acelerar(celta)
# print(celta.nome)