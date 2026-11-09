
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



# --------------------------------------------------
# 10) analisando a combinação dos recursos
# --------------------------------------------------

print("\n" + "=" * 50)
print("COMBINAÇÃO DOS RECURSOS")
print("=" * 50)

# contando as unidades que possuem os três recursos
todos = sum(
    linha["IN_BIBLIOTECA"] == "1"
    and linha["IN_LABORATORIO_CIENCIAS"] == "1"
    and linha["IN_INTERNET"] == "1"
    for linha in dados
)

# contando as unidades que não possuem nenhum dos três recursos
nenhum = sum(
    linha["IN_BIBLIOTECA"] == "0"
    and linha["IN_LABORATORIO_CIENCIAS"] == "0"
    and linha["IN_INTERNET"] == "0"
    for linha in dados
)

print("Unidades com os três recursos:", todos)
print("Unidades sem nenhum dos três recursos:", nenhum)



# --------------------------------------------------
# 11) contando a quantidade de recursos por unidade
# --------------------------------------------------

from collections import Counter

quantidade_recursos = Counter()

for linha in dados:
    total_recursos = sum(
        linha[variavel] == "1"
        for variavel in recursos
    )

    quantidade_recursos[total_recursos] += 1

print("\n" + "=" * 50)
print("QUANTIDADE DE RECURSOS POR UNIDADE")
print("=" * 50)

for quantidade in range(4):
    total = quantidade_recursos[quantidade]
    percentual = total / len(dados) * 100

    print(
        f"{quantidade} recurso(s): "
        f"{total} unidades ({percentual:.2f}%)"
    )



# --------------------------------------------------
# 12) identificando as combinações de infraestrutura
# --------------------------------------------------

combinacoes = Counter()

for linha in dados:
    presentes = tuple(
        descricao
        for variavel, descricao in recursos.items()
        if linha[variavel] == "1"
    )

    combinacoes[presentes] += 1

print("\n" + "=" * 50)
print("COMBINAÇÕES DE INFRAESTRUTURA")
print("=" * 50)

for combinacao, quantidade in combinacoes.most_common():
    nome = ", ".join(combinacao) if combinacao else "nenhum recurso"
    percentual = quantidade / len(dados) * 100

    print(f"{nome}: {quantidade} unidades ({percentual:.2f}%)")



# --------------------------------------------------
# 13) comparando biblioteca e biblioteca/sala de leitura
# --------------------------------------------------

print("\n" + "=" * 50)
print("BIBLIOTECA E SALA DE LEITURA")
print("=" * 50)

biblioteca = sum(
    linha["IN_BIBLIOTECA"] == "1"
    for linha in dados
)

biblioteca_sala = sum(
    linha["IN_BIBLIOTECA_SALA_LEITURA"] == "1"
    for linha in dados
)

sem_biblioteca_com_sala = sum(
    linha["IN_BIBLIOTECA"] == "0"
    and linha["IN_BIBLIOTECA_SALA_LEITURA"] == "1"
    for linha in dados
)

print("total de unidades:", len(dados))
print("unidades com biblioteca:", biblioteca)
print("unidades com biblioteca ou sala de leitura:", biblioteca_sala)
print(
    "unidades sem biblioteca, mas com indicador combinado positivo:",
    sem_biblioteca_com_sala
)

print("\nvalores do indicador combinado:")
print(
    dict(Counter(
        linha["IN_BIBLIOTECA_SALA_LEITURA"]
        for linha in dados
    ))
)



# --------------------------------------------------
# 14) conferindo a consistência dos indicadores de leitura
# --------------------------------------------------

inconsistencias = sum(
    linha["IN_BIBLIOTECA"] == "1"
    and linha["IN_BIBLIOTECA_SALA_LEITURA"] == "0"
    for linha in dados
)

print("\n" + "=" * 50)
print("CONSISTÊNCIA DOS INDICADORES DE LEITURA")
print("=" * 50)

print(
    "unidades com biblioteca, mas sem indicador combinado:",
    inconsistencias
)
