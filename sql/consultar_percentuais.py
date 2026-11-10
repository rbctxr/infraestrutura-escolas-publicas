
# 1) importar a biblioteca sqlite3
import sqlite3

# 2) conectar ao banco de dados
conexao = sqlite3.connect("data/infraestrutura_escolas.db")
cursor = conexao.cursor()

# 3) calcular os percentuais de infraestrutura por localização
consulta = """
SELECT
    CASE
        WHEN localizacao = '1' THEN 'urbana'
        WHEN localizacao = '2' THEN 'rural'
        ELSE 'não informada'
    END AS tipo_localizacao,

    COUNT(*) AS total_unidades,

    ROUND(100.0 * SUM(biblioteca) / COUNT(*), 2)
        AS percentual_biblioteca,

    ROUND(100.0 * SUM(laboratorio_ciencias) / COUNT(*), 2)
        AS percentual_laboratorio,

    ROUND(100.0 * SUM(internet) / COUNT(*), 2)
        AS percentual_internet

FROM escolas
GROUP BY localizacao
ORDER BY localizacao;
"""

# 4) executar a consulta
cursor.execute(consulta)

# 5) recuperar os resultados
resultados = cursor.fetchall()

# 6) mostrar os percentuais
for linha in resultados:
    print("\nlocalização:", linha[0])
    print("total de unidades:", linha[1])
    print("biblioteca:", linha[2], "%")
    print("laboratório de ciências:", linha[3], "%")
    print("internet:", linha[4], "%")

# 7) fechar a conexão
conexao.close()
