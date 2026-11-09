# Infraestrutura das Escolas Públicas

## Sobre o projeto

Este projeto tem como objetivo analisar a infraestrutura das escolas públicas do Distrito Federal, utilizando os microdados do Censo Escolar 2024, disponibilizados pelo Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP).

A análise busca identificar possíveis desigualdades na disponibilidade de recursos de infraestrutura, considerando a localização das unidades escolares e sua dependência administrativa.

## Objetivo

Investigar a disponibilidade de recursos de infraestrutura nas unidades públicas do Distrito Federal, com foco em:

- bibliotecas;
- laboratórios de ciências;
- acesso à internet.

Como análise complementar, também será considerada a disponibilidade de bibliotecas e/ou salas de leitura.

## Perguntas de análise

1. qual percentual das unidades públicas do Distrito Federal possui biblioteca, laboratório de ciências e acesso à internet?
2. como a disponibilidade desses recursos varia entre unidades urbanas e rurais?
3. quais diferenças de infraestrutura existem entre as unidades públicas das dependências federal e estadual no Distrito Federal?

## Ferramentas utilizadas

- **Python:** exploração, filtragem, tratamento e análise dos dados.
- **SQL:** consultas e análise dos dados.
- **Power BI:** construção de visualizações e dashboard.
- **Git e GitHub:** versionamento e documentação do projeto.

## Fonte dos dados

Os dados utilizados são os microdados do Censo Escolar 2024, disponibilizados pelo INEP.

[Portal de Microdados do Censo Escolar — INEP](https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/censo-escolar)

## Recorte da análise

- **abrangência:** Distrito Federal (DF).
- **público analisado:** unidades públicas das dependências federal e estadual em atividade.
- **período:** Censo Escolar 2024.
- **total de unidades analisadas:** 716.

O Distrito Federal não possui municípios nem rede municipal de ensino. Por isso, a análise considera as dependências administrativas federal e estadual, conforme a classificação utilizada nos microdados do INEP.

Foram identificadas 11 unidades federais e 705 estaduais em atividade.

O recorte também inclui unidades com funções educacionais específicas, não se limitando às escolas que oferecem ensino regular.

## Análise exploratória dos dados

A análise inicial foi realizada em Python, utilizando as bibliotecas `csv` e `collections`.

Foram selecionadas as unidades públicas do Distrito Federal em atividade, considerando três indicadores principais de infraestrutura: biblioteca, laboratório de ciências e internet.

### Disponibilidade dos recursos

| indicador | unidades | percentual |
|---|---:|---:|
| biblioteca | 199 | 27,79% |
| laboratório de ciências | 118 | 16,48% |
| acesso à internet | 711 | 99,30% |

Os resultados mostram que o acesso à internet está presente em quase todas as unidades analisadas. Por outro lado, bibliotecas e laboratórios de ciências apresentam uma disponibilidade menor, principalmente os laboratórios.

### Comparação entre unidades urbanas e rurais

Das 716 unidades analisadas, 633 estão localizadas em áreas urbanas e 83 em áreas rurais.

| indicador | urbanas | rurais |
|---|---:|---:|
| biblioteca | 28,28% | 24,10% |
| laboratório de ciências | 17,69% | 7,23% |
| acesso à internet | 99,37% | 98,80% |

A principal diferença aparece nos laboratórios de ciências, presentes em 17,69% das unidades urbanas e em apenas 7,23% das rurais.

A disponibilidade de bibliotecas também é menor nas unidades rurais, enquanto o acesso à internet apresenta percentuais semelhantes nos dois grupos.

### Comparação por dependência administrativa

| indicador | federal | estadual |
|---|---:|---:|
| biblioteca | 100% | 26,67% |
| laboratório de ciências | 100% | 15,18% |
| acesso à internet | 100% | 99,29% |

Todas as 11 unidades federais analisadas possuem os três recursos.

Entre as 705 unidades estaduais, a disponibilidade de bibliotecas e laboratórios de ciências é menor, enquanto o acesso à internet está presente em praticamente todas.

É importante considerar a diferença no tamanho dos grupos antes de interpretar esses resultados.

### Combinação dos recursos

Além da disponibilidade individual, foi analisada a presença simultânea dos três recursos em cada unidade.

| combinação | unidades | percentual |
|---|---:|---:|
| somente internet | 451 | 62,99% |
| biblioteca e internet | 143 | 19,97% |
| laboratório de ciências e internet | 63 | 8,80% |
| biblioteca, laboratório e internet | 54 | 7,54% |
| nenhum dos três recursos | 3 | 0,42% |
| somente biblioteca | 1 | 0,14% |
| biblioteca e laboratório | 1 | 0,14% |

A combinação mais frequente é a presença somente de internet, identificada em 451 unidades.

Apenas 54 unidades possuem os três recursos simultaneamente, representando 7,54% do total analisado.

Isso mostra que a alta disponibilidade de internet não significa que os demais recursos de infraestrutura estejam igualmente presentes.

### Biblioteca e sala de leitura

Durante a análise, foi identificada uma diferença entre duas variáveis presentes nos microdados:

- `IN_BIBLIOTECA`: identifica a presença de biblioteca.
- `IN_BIBLIOTECA_SALA_LEITURA`: identifica a presença de biblioteca e/ou sala de leitura.

De acordo com o dicionário de dados do INEP, as variáveis representam indicadores diferentes.

Considerando apenas bibliotecas, 199 unidades possuem o recurso, correspondendo a 27,79% do total.

Ao considerar bibliotecas e/ou salas de leitura, esse número aumenta para 632 unidades, representando 88,27%.

Também foram identificadas 433 unidades sem biblioteca, mas com resultado positivo no indicador combinado.

A conferência entre as variáveis não identificou inconsistências: todas as unidades com biblioteca também apresentaram resultado positivo no indicador combinado.

Por isso, os dois indicadores serão mantidos separadamente na análise, evitando interpretações incorretas.

## Observações metodológicas

- foram consideradas apenas unidades do Distrito Federal com situação de funcionamento em atividade;
- foram incluídas as dependências administrativas federal e estadual;
- os percentuais foram calculados considerando o total de unidades de cada grupo;
- os indicadores analisados possuem respostas binárias, sendo `0` para não e `1` para sim;
- a presença de internet não indica necessariamente a qualidade da conexão;
- a ausência dos três recursos selecionados não significa ausência de toda a infraestrutura escolar;
- os resultados descrevem o conjunto analisado e não devem ser generalizados para todas as escolas brasileiras.

## Estrutura do projeto

```text
infraestrutura-escolas-publicas/
│
├── data/                         # dados locais não versionados
│   └── .gitignore                # proteção dos microdados
│
├── sql/                          # consultas sql
│
├── dashboard/                    # arquivos do power bi
│
├── analise_infraestrutura.py     # análise exploratória em python
│
└── README.md                     # documentação do projeto
```

Os microdados originais não são enviados ao GitHub. Para reproduzir a análise, é necessário obter os arquivos no portal oficial do INEP.

## Status do projeto

**em desenvolvimento.**

Etapas concluídas:

- [x] configuração do repositório no GitHub;
- [x] organização da estrutura inicial;
- [x] obtenção e leitura dos microdados do Censo Escolar 2024;
- [x] definição do recorte geográfico e das unidades analisadas;
- [x] análise exploratória em Python;
- [x] comparação dos indicadores de infraestrutura;
- [x] análise das combinações de recursos;
- [x] validação dos indicadores de biblioteca e sala de leitura.

Próximas etapas:

- [ ] desenvolvimento das consultas SQL;
- [ ] preparação dos dados para visualização;
- [ ] construção do dashboard no Power BI;
- [ ] documentação dos resultados finais.

---

**fonte:** INEP — Microdados do Censo Escolar 2024.