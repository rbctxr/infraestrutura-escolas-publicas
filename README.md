# Infraestrutura das Escolas Públicas

## Sobre o projeto

Este projeto tem como objetivo analisar a infraestrutura das escolas públicas brasileiras utilizando os microdados do Censo Escolar, disponibilizados pelo Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP).

A análise busca identificar possíveis desigualdades na oferta de recursos essenciais para o ambiente escolar, considerando características como localização e dependência administrativa.

## Objetivo

Investigar a disponibilidade de recursos de infraestrutura nas escolas públicas, com foco em:

- Bibliotecas;
- Laboratórios de ciências;
- Acesso à internet.

## Perguntas de análise

1. Qual percentual das escolas públicas possui biblioteca, laboratório de ciências e acesso à internet?
2. Como a disponibilidade desses recursos varia entre escolas urbanas e rurais?
3. Quais municípios ou redes de ensino (municipal e estadual) apresentam maior carência de infraestrutura?

## Ferramentas utilizadas

- **Python:** exploração, tratamento e preparação dos dados.
- **SQL:** consultas e análise dos dados.
- **Power BI:** construção de visualizações e dashboard.
- **Git e GitHub:** versionamento e documentação do projeto.

## Fonte dos dados

Os dados serão obtidos nos microdados do Censo Escolar, disponibilizados pelo INEP.

[Portal de Microdados do Censo Escolar — INEP](https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/censo-escolar)

## Recorte da análise

- **Abrangência:** um estado brasileiro (a definir).
- **Público analisado:** escolas públicas.
- **Período:** ano do Censo Escolar a definir conforme disponibilidade e estrutura dos dados.

## Estrutura do projeto

```text
infraestrutura-escolas-publicas/
│
├── data/       # Dados brutos e tratados (não versionados)
├── sql/        # Consultas SQL
├── dashboard/  # Arquivos do Power BI
└── README.md   # Documentação do projeto
```

## Status do projeto

Em desenvolvimento. A etapa inicial de configuração do repositório e organização da estrutura foi concluída.