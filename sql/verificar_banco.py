
# 1) importar a biblioteca sqlite3
import sqlite3

# 2) conectar ao banco de dados
conexao = sqlite3.connect("data/infraestrutura_escolas.db")

# 3) criar um cursor
cursor = conexao.cursor()

# 4) consultar a estrutura da tabela escolas
cursor.execute("PRAGMA table_info(escolas)")

# 5) mostrar as colunas encontradas
colunas = cursor.fetchall()

for coluna in colunas:
    print(coluna[1], "-", coluna[2])

# 6) verificar quantos registros existem
cursor.execute("SELECT COUNT(*) FROM escolas")

total = cursor.fetchone()[0]

print("total de registros:", total)

# 7) fechar a conexão
conexao.close()
