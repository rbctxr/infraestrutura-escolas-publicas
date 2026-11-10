
# 1) importar a biblioteca csv
import csv

# 2) informar o caminho dos microdados
arquivo = (
    r"data\microdados_censo_escolar_2024"
    r"\microdados_censo_escolar_2024_defeso"
    r"\dados\microdados_ed_basica_2024.csv"
)

# 3) abrir o arquivo csv
with open(arquivo, encoding="latin1", newline="") as f:
    leitor = csv.DictReader(f, delimiter=";")

    # 4) verificar se a coluna CO_ENTIDADE existe
    if "CO_ENTIDADE" in leitor.fieldnames:
        print("coluna CO_ENTIDADE encontrada!")
    else:
        print("coluna CO_ENTIDADE não encontrada.")
