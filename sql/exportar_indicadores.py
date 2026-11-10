
# 1) importar as bibliotecas
import csv
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
    END AS localizacao,
    COUNT(*) AS total_unidades,
    SUM(biblioteca) AS biblioteca,
    SUM(laboratorio_ciencias) AS laboratorio_ciencias,
    SUM(internet) AS internet
FROM escolas
GROUP BY localizacao
ORDER BY localizacao;
"""

# 4) executar a consulta
cursor.execute(consulta)
resultados = cursor.fetchall()

# 5) definir o caminho do arquivo de saída
arquivo_saida = "data/indicadores_localizacao.csv"

# 6) exportar os resultados para csv
with open(arquivo_saida, "w", newline="", encoding="utf-8-sig") as f:
    escritor = csv.writer(f, delimiter=";")

    escritor.writerow([
        "localizacao",
        "total_unidades",
        "biblioteca",
        "laboratorio_ciencias",
        "internet"
    ])

    escritor.writerows(resultados)

# 7) fechar a conexão
conexao.close()

print("arquivo exportado com sucesso!")
print("local:", arquivo_saida)
print("total de grupos:", len(resultados))
