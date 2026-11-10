
# 1) importar as bibliotecas
import csv
import sqlite3

# 2) definir o caminho dos arquivos
arquivo_csv = (
    r"data\microdados_censo_escolar_2024"
    r"\microdados_censo_escolar_2024_defeso"
    r"\dados\microdados_ed_basica_2024.csv"
)

arquivo_banco = "data/infraestrutura_escolas.db"

# 3) conectar ao banco de dados
conexao = sqlite3.connect(arquivo_banco)
cursor = conexao.cursor()

# 4) preparar o comando sql de inserção
comando_sql = """
INSERT OR REPLACE INTO escolas (
    id_escola,
    dependencia,
    localizacao,
    biblioteca,
    laboratorio_ciencias,
    internet,
    biblioteca_sala_leitura
)
VALUES (?, ?, ?, ?, ?, ?, ?)
"""

# 5) ler o csv e selecionar as unidades do df
registros = []

with open(arquivo_csv, encoding="latin1", newline="") as f:
    leitor = csv.DictReader(f, delimiter=";")

    for linha in leitor:
        if (
            linha["SG_UF"] == "DF"
            and linha["TP_DEPENDENCIA"] in ["1", "2"]
            and linha["TP_SITUACAO_FUNCIONAMENTO"] == "1"
        ):
            registros.append((
                int(linha["CO_ENTIDADE"]),
                linha["TP_DEPENDENCIA"],
                linha["TP_LOCALIZACAO"],
                int(linha["IN_BIBLIOTECA"]) if linha["IN_BIBLIOTECA"] in ["0", "1"] else None,
                int(linha["IN_LABORATORIO_CIENCIAS"]) if linha["IN_LABORATORIO_CIENCIAS"] in ["0", "1"] else None,
                int(linha["IN_INTERNET"]) if linha["IN_INTERNET"] in ["0", "1"] else None,
                int(linha["IN_BIBLIOTECA_SALA_LEITURA"]) if linha["IN_BIBLIOTECA_SALA_LEITURA"] in ["0", "1"] else None
            ))

# 6) inserir os registros no banco
cursor.executemany(comando_sql, registros)

# 7) salvar as alterações
conexao.commit()

# 8) conferir a quantidade de unidades importadas
cursor.execute("SELECT COUNT(*) FROM escolas")
total = cursor.fetchone()[0]

print("registros selecionados do csv:", len(registros))
print("total de unidades no banco:", total)

# 9) fechar a conexão
conexao.close()
