import importlib
import aula98_m # Só pode existir uma instancia dele durante todo meu programa

print(aula98_m.variavel)

for i in range(10):
    importlib.reload(aula98_m) # Recarrego o módulo
    print(i)

print('Fim')