
# 1) importar a biblioteca sqlite3
import sqlite3

# 2) conectar ao banco de dados
conexao = sqlite3.connect("data/infraestrutura_escolas.db")
cursor = conexao.cursor()

# 3) consultar os indicadores por localização
consulta = """
SELECT
    CASE
        WHEN localizacao = '1' THEN 'urbana'
        WHEN localizacao = '2' THEN 'rural'
        ELSE 'não informada'
    END AS tipo_localizacao,
    COUNT(*) AS total_unidades,
    SUM(biblioteca) AS com_biblioteca,
    SUM(laboratorio_ciencias) AS com_laboratorio,
    SUM(internet) AS com_internet
FROM escolas
GROUP BY localizacao
ORDER BY localizacao;
"""

# 4) executar a consulta sql
cursor.execute(consulta)

# 5) recuperar todos os resultados
resultados = cursor.fetchall()

# 6) mostrar os resultados por localização
for linha in resultados:
    print("\nlocalização:", linha[0])
    print("total de unidades:", linha[1])
    print("unidades com biblioteca:", linha[2])
    print("unidades com laboratório:", linha[3])
    print("unidades com internet:", linha[4])

# 7) fechar a conexão
conexao.close()
