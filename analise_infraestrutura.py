
import csv
from collections import Counter, defaultdict

# --------------------------------------------------
# 1) localizando os arquivos
# --------------------------------------------------

arquivo = (
    r"data\microdados_censo_escolar_2024"
    r"\microdados_censo_escolar_2024_defeso"
    r"\dados\microdados_ed_basica_2024.csv"
)

# --------------------------------------------------
# 2) lendo os microdados
# --------------------------------------------------

with open(arquivo, encoding="latin1", newline="") as f:
    leitor = csv.DictReader(f, delimiter=";")

    # a ideia é selecionar apenas unidades do DF,
    # federais ou estaduais e em atividade.
    dados = [
        linha for linha in leitor
        if linha["SG_UF"] == "DF"
        and linha["TP_DEPENDENCIA"] in ["1", "2"]
        and linha["TP_SITUACAO_FUNCIONAMENTO"] == "1"
    ]

# --------------------------------------------------
# 3) definindo os recursos a serem analisados
# --------------------------------------------------

recursos = {
    "IN_BIBLIOTECA": "Biblioteca",
    "IN_LABORATORIO_CIENCIAS": "Laboratório de ciências",
    "IN_INTERNET": "Internet"
}

# --------------------------------------------------
# 4. função de calculo dos indicadores
# --------------------------------------------------

def analisar_grupo(nome, grupo):
    total = len(grupo)

    print(f"\n{nome}")
    print(f"Total de unidades: {total}")

    for variavel, descricao in recursos.items():
        quantidade = sum(
            linha[variavel] == "1" for linha in grupo
        )

        percentual = (
            quantidade / total * 100 if total else 0
        )

        ausentes = sum(
            linha[variavel] not in ["0", "1"]
            for linha in grupo
        )

        print(
            f"{descricao}: "
            f"{quantidade} unidades "
            f"({percentual:.2f}%)"
        )

        if ausentes:
            print(f"  Registros sem informação válida: {ausentes}")

# --------------------------------------------------
# 5) analise geral
# --------------------------------------------------

print("=" * 50)
print("ANÁLISE GERAL - DISTRITO FEDERAL")
print("=" * 50)

analisar_grupo("Todas as unidades públicas em atividade", dados)

# --------------------------------------------------
# 6) analise por localização
# --------------------------------------------------

por_localizacao = defaultdict(list)

for linha in dados:
    por_localizacao[linha["TP_LOCALIZACAO"]].append(linha)

print("\n" + "=" * 50)
print("ANÁLISE POR LOCALIZAÇÃO")
print("=" * 50)

analisar_grupo("Unidades urbanas", por_localizacao["1"])
analisar_grupo("Unidades rurais", por_localizacao["2"])

# --------------------------------------------------
# 7) analise por dependencia administrativa
# --------------------------------------------------

por_dependencia = defaultdict(list)

for linha in dados:
    por_dependencia[linha["TP_DEPENDENCIA"]].append(linha)

print("\n" + "=" * 50)
print("ANÁLISE POR DEPENDÊNCIA ADMINISTRATIVA")
print("=" * 50)

analisar_grupo("Unidades federais", por_dependencia["1"])
analisar_grupo("Unidades estaduais", por_dependencia["2"])

# --------------------------------------------------
# 8) conferindo a localização
# --------------------------------------------------

print("\n" + "=" * 50)
print("CONFERÊNCIA DA LOCALIZAÇÃO")
print("=" * 50)

localizacoes = Counter(
    linha["TP_LOCALIZACAO"] for linha in dados
)

print("Urbanas:", localizacoes["1"])
print("Rurais:", localizacoes["2"])
print("Sem localização informada:", localizacoes[""])

# --------------------------------------------------
# 9) conferindo a dependencia
# --------------------------------------------------

print("\n" + "=" * 50)
print("CONFERÊNCIA DA DEPENDÊNCIA")
print("=" * 50)

dependencias = Counter(
    linha["TP_DEPENDENCIA"] for linha in dados
)

print("Federais:", dependencias["1"])
print("Estaduais:", dependencias["2"])
print("Total:", len(dados))

print("\nAnálise concluída!")
