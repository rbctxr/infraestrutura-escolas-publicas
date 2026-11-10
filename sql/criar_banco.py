
# 1) importar a biblioteca sqlite3
import sqlite3

# 2) definir o caminho do banco de dados
caminho_banco = "data/infraestrutura_escolas.db"

# 3) conectar ao banco de dados
conexao = sqlite3.connect(caminho_banco)

# 4) criar um cursor para executar comandos sql
cursor = conexao.cursor()

# 5) criar a tabela escolas
cursor.execute("""
CREATE TABLE IF NOT EXISTS escolas (
    id_escola INTEGER PRIMARY KEY,
    dependencia TEXT,
    localizacao TEXT,
    biblioteca INTEGER,
    laboratorio_ciencias INTEGER,
    internet INTEGER,
    biblioteca_sala_leitura INTEGER
)
""")

# 6) salvar as alterações no banco
conexao.commit()

# 7) fechar a conexão
conexao.close()

print("tabela escolas criada com sucesso!")
