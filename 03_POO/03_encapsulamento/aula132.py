# @property + @setter - getter e setter no modo Pythônico
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Atributos que começar com um ou dois underlines
# não devem ser usados fora da classe.
#  🐍🤓🤯🤯🤯🤯
class Caneta:
    def __init__(self, cor):
        # private protected
        self.cor = cor
        self._cor_tampa = None # Coloco um _ para dizer que não deve ser usado esse atributo

    @property
    def cor(self):
        print('ESTOU NO GETTER') # Pego um valor
        return self._cor

    @cor.setter # Utilizo nome_property.setter para configurar um novo valor
    def cor(self, valor):
        print('ESTOU NO SETTER') # Configuro um valor
        self._cor = valor

    @property
    def cor_tampa(self):
        return self._cor_tampa

    @cor_tampa.setter # Com o setter, eu não acesso o atributo diretamente no __init__
    def cor_tampa(self, valor):
        self._cor_tampa = valor


caneta = Caneta('Azul') # Aqui entrei direto no __init__
caneta.cor = 'Rosa'
caneta.cor_tampa = 'Azul'
print(caneta.cor)
print(caneta.cor_tampa)