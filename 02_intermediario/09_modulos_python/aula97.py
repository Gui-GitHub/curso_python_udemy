# Modularização - Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas
# abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ por
# padrão
# O python conhece todos os módulos e pacotes presentes
# nos caminhos de sys.path, irmãos

import aula97_m # Não vamos criar com nomes resrvados, como sys, os...
from aula97_m import soma, variavel_modulo

# print('Este módulo se chama', __name__)
print(aula97_m.variavel_modulo) # Caso eu importasse tudo
print(variavel_modulo) # Caso eu importo com o from coisas especificas
print(aula97_m.soma(2, 3)) # Caso eu importasse tudo
print(soma(2, 3)) # Caso eu importo com o from coisas especificas