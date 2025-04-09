"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
"""

x = 1

def escopo():
    global x # Como eu defini o x dentro do def, eu preciso declarar ele como global, senão a gente não consegue manipular ele
    x = 10 # Esse x não é o x acima, é uma nova variavel (Isso vale se não existir o global, como existe, ele altera o valor da x fora)

    def outra_funcao():
        global x
        x = 11
        y = 2
        print(x, y)

    outra_funcao() # Tenho que chamar ela dentro do escopo em que ela é declarada
    print(x)

print(x)
escopo()
print(x) # Esse x que ele está chamando é o x da def, após a modificação da variavel, isso por que eu chamei a def escopo()