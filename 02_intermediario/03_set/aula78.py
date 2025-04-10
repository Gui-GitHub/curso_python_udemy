# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3} Só temos o valor
s = set('Luiz') # não garante a ordem
print(s)
s1 = set()  # vazio
s1 = {'Luiz', 1, 2, 3}  # com dados, não garante a ordem
print(s1)

#######################################

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Seus valores serão sempre únicos;
# - Não aceitam valores mutáveis;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)
l1 = [1, 2, 3, 3, 3, 3, 3, 1]
s2 = set(l1) # Elimina as duplicadas
l2 = list(s2) # Posso converter de volta
print(s2)
print(l2)
s3 = {1, 2, 3}
print(3 not in s3)
for numero in s3: # Aqui eu busco meus dados no meu set
    print(numero)

############################################################

# Métodos úteis:
# add, update, clear, discard

s4 = set()
s4.add('Luiz')
s4.add(1)
s4.update(('Olá mundo', 1, 2, 3, 4))
# s4.clear()
s4.discard('Olá mundo')
s4.discard('Luiz')
print(s4)

#############################################################

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

s5 = {1, 2, 3}
s6 = {2, 3, 4}
s7 = s5 | s6
s7 = s5 & s6
s7 = s5 - s6 # Disponíveis apenas no da esquerda
s7 = s5 ^ s6
print(s7)