import sqlite3

from main import DB_FILE, TABLE_NAME

# Conexão com o banco de dados
connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# Selecionando todos os dados da tabela
cursor.execute(
    f'SELECT * FROM {TABLE_NAME}'
)

# Imprimindo os dados selecionados
for row in cursor.fetchall():
    _id, name, weight = row
    print(_id, name, weight)
print()

# Selecionando dados com filtro
cursor.execute(
    f'SELECT * FROM {TABLE_NAME} '
    'WHERE id = "3"'
)
row = cursor.fetchone()
_id, name, weight = row
print(_id, name, weight)

# Fechar conexões
cursor.close()
connection.close()