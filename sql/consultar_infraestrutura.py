
# 1) importar a biblioteca sqlite3
import sqlite3

# 2) conectar ao banco de dados
conexao = sqlite3.connect("data/infraestrutura_escolas.db")
cursor = conexao.cursor()

# 3) consultar os indicadores de infraestrutura
consulta = """
SELECT
    COUNT(*) AS total_unidades,
    SUM(biblioteca) AS com_biblioteca,
    SUM(laboratorio_ciencias) AS com_laboratorio,
    SUM(internet) AS com_internet
FROM escolas;
"""

# 4) executar a consulta sql
cursor.execute(consulta)

# 5) recuperar o resultado
resultado = cursor.fetchone()

# 6) mostrar os resultados
print("total de unidades:", resultado[0])
print("unidades com biblioteca:", resultado[1])
print("unidades com laboratório:", resultado[2])
print("unidades com internet:", resultado[3])

# 7) fechar a conexão
conexao.close()
