# (Parte1) try e except para tratar exceções

try: # Não podemos silenciar erros, devemos tratar cada um deles
    a = 18
    b = 0
    print('Linha 1'[1000])
    c = a / b
    print('Linha 2')
except ZeroDivisionError: # Usando somente um except, eu não sei o erro que acontece e não sei como trata-lo
    print('Dividiu por zero.')
except NameError:
    print('Nome b não está definido')
except (TypeError, IndexError): # Posso tratar 2 erros em uma única linha
    print('TypeError + IndexError')
except Exception:
    print('ERRO DESCONHECIDO.')

print('CONTINUAR')

# (Parte 2) try e except para tratar exceções

try:
    a = 18
    b = 0
    # print(b[0])
    # print('Linha 1'[1000])
    c = a / b
    print('Linha 2')
except ZeroDivisionError as e: # O as 'e' faz com que ele exiba a mensagem, criei uma variavel
    print(e.__class__.__name__)
    print(e) # Seria legal colocar algo como 'Mensagem de erro: e'
except NameError:
    print('Nome b não está definido')
except (TypeError, IndexError) as error:
    print('TypeError + IndexError')
    print('MSG:', error)
    print('Nome:', error.__class__.__name__) # Aqui trás essesatributos para pegar o nome da Classe
except Exception:
    print('ERRO DESCONHECIDO.')

print('CONTINUAR')