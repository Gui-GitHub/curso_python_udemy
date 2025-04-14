import copy
from dados import produtos

# copy, sorted, produtos.sort
# Exercícios

# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

novos_produtos = [
    {**p, 'preco': round(p['preco'] * 1.1, 2)}
    for p in 
    copy.deepcopy(produtos)
]

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

produtos_decrescente = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['nome'],
    reverse=True
)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

produtos_preco_crescente = sorted (
    copy.deepcopy(produtos),
    key=lambda p: p['preco']
)

print('NOVOS PRODUTOS:', *novos_produtos, sep='\n')
print('PRODUTOS DECRESCENTES:', *produtos_decrescente, sep='\n')
print('PRODUTOS PREÇOS CRESCENTES:', *produtos_preco_crescente, sep='\n')