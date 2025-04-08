"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
Como eu mudo então? Cria outra váriavel
VsCode ajuda a gente, colocando '.' após a váriavel ele lista os métodos
Tipos embutidos: Padrões do Python / Built-in Types
"""
string = '1000'
# outra_variavel = f'{string[:3]}ABC{string[4:]}'
# print(string)
# print(outra_variavel)
print(string.zfill(10))