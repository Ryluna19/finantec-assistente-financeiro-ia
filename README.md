# FinanTec

Assistente de organização financeira para estudantes e pessoas em início de carreira.

Projeto desenvolvido inicialmente para o Lab **Construa Seu Assistente Virtual com Inteligência Artificial**, da DIO, e evoluído posteriormente com uma camada simples de ETL para processamento de dados financeiros simulados.

## Sobre o Projeto

O FinanTec é um protótipo de assistente financeiro educativo que utiliza dados simulados para ajudar uma pessoa usuária a entender melhor receitas, gastos, saldo mensal e metas financeiras.

O projeto combina análise de dados com Python, uma interface em Streamlit e IA generativa para explicar os resultados de forma simples e contextualizada.

A proposta não é criar uma solução financeira completa, mas demonstrar como um assistente virtual pode usar uma base de conhecimento organizada, cálculos confiáveis e uma etapa de preparação de dados para responder perguntas com mais segurança.

## Objetivo

Ajudar estudantes, estagiários e pessoas em início de carreira a:

- visualizar receitas e gastos por período;
- identificar categorias de maior consumo;
- acompanhar metas financeiras;
- entender conceitos financeiros básicos;
- receber explicações simples com apoio de IA generativa;
- reconhecer quando não há dados suficientes para uma resposta segura.

## Funcionalidades

- Dashboard financeiro com resumo por período;
- cálculo de receitas, gasto de consumo, valor separado para reserva e saldo disponível;
- gráfico de gastos por categoria;
- identificação da maior categoria de consumo;
- filtro mensal no dashboard;
- simulador de metas financeiras;
- chat com IA generativa usando contexto dos dados simulados;
- histórico de conversa separado por período analisado;
- respostas com regras para evitar invenção de dados;
- pipeline simples de ETL para processar múltiplos arquivos CSV;
- documentação dos passos do desafio e da evolução do projeto.

## Tecnologias Utilizadas

- Python
- pandas
- Streamlit
- python-dotenv
- google-genai
- CSV
- JSON
- Gemini API
- ETL com Python

## Como o FinanTec Funciona

O fluxo principal do projeto é:

```text
Arquivos CSV/JSON
        ↓
Leitura com Python
        ↓
Tratamento e cálculos com pandas
        ↓
Dashboard em Streamlit
        ↓
Contexto estruturado para IA
        ↓
Resposta explicativa do FinanTec
```

Na evolução com ETL, o fluxo passa a ser:

```text
data/raw/
        ↓
Extração dos arquivos CSV
        ↓
Validação de colunas obrigatórias
        ↓
Tratamento e padronização com pandas
        ↓
data/processed/transacoes_processadas.csv
        ↓
Dashboard com filtro por período
        ↓
IA explicando os indicadores calculados
```

Os cálculos financeiros são feitos pela aplicação em Python. A IA generativa é usada para interpretar perguntas e explicar os resultados, não para inventar valores.

## Base de Conhecimento

A pasta `data/` contém dados simulados usados pelo projeto:

| Arquivo/Pasta | Finalidade |
|---|---|
| `perfil_usuario.json` | Perfil fictício da pessoa usuária, renda, situação atual e metas. |
| `transacoes.csv` | Arquivo original de transações usado na primeira versão do Lab. |
| `historico_atendimento.csv` | Dúvidas anteriores e respostas resumidas. |
| `conceitos_financeiros.json` | Conceitos básicos de organização financeira. |
| `produtos_financeiros.json` | Produtos financeiros descritos apenas para fins educativos. |
| `data/raw/` | Arquivos brutos de transações mensais. |
| `data/processed/` | Arquivo tratado gerado pelo pipeline ETL. |

A pessoa fictícia usada no projeto é Marina Costa, estudante universitária e estagiária.

## FinanTec 2 — Evolução com ETL

A versão 2 do projeto adiciona uma camada simples de ETL para aproximar o FinanTec de um fluxo mais realista de dados.

O objetivo dessa evolução é processar múltiplos arquivos de transações financeiras simuladas, validar sua estrutura, padronizar os dados e gerar uma base tratada para o dashboard e para o assistente com IA.

### O que foi adicionado

- Estrutura `data/raw/` para arquivos brutos;
- estrutura `data/processed/` para dados tratados;
- pasta `scripts/` para scripts de automação e ETL;
- pasta `logs/` para registros de execução;
- script `scripts/etl_transacoes.py`;
- leitura de múltiplos arquivos CSV mensais;
- validação de colunas obrigatórias;
- limpeza e padronização dos dados;
- criação da coluna `ano_mes`;
- geração do arquivo `transacoes_processadas.csv`;
- filtro mensal no dashboard;
- histórico de chat separado por período analisado.

### Etapas do ETL

| Etapa | Descrição |
|---|---|
| Extract | Leitura dos arquivos CSV em `data/raw/`. |
| Transform | Validação de colunas, conversão de datas, padronização de categorias, tipos e valores. |
| Load | Geração do arquivo tratado em `data/processed/transacoes_processadas.csv`. |

## Estrutura do Projeto

```text
finantec-assistente-financeiro-ia/
├── assets/
├── data/
│   ├── raw/
│   │   ├── transacoes_2026_06.csv
│   │   └── transacoes_2026_07.csv
│   ├── processed/
│   │   └── transacoes_processadas.csv
│   ├── conceitos_financeiros.json
│   ├── historico_atendimento.csv
│   ├── perfil_usuario.json
│   ├── produtos_financeiros.json
│   └── transacoes.csv
├── docs/
│   ├── 01-documentacao-agente.md
│   ├── 02-base-conhecimento.md
│   ├── 03-prompts.md
│   ├── 04-metricas.md
│   └── 05-pitch.md
├── logs/
├── scripts/
│   └── etl_transacoes.py
├── src/
│   ├── agent.py
│   ├── analytics.py
│   ├── app.py
│   ├── data_loader.py
│   ├── prompts.py
│   ├── teste_contexto.py
│   ├── teste_dados.py
│   ├── teste_ia.py
│   ├── teste_metas.py
│   └── teste_periodos.py
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt
```

## Como Executar o Projeto

### 1. Clone o repositório

```bash
git clone https://github.com/Ryluna19/finantec-assistente-financeiro-ia.git
cd finantec-assistente-financeiro-ia
```

### 2. Crie e ative o ambiente virtual

No Windows:

```bash
py -m venv .venv
.venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure a chave da IA

Crie um arquivo `.env` na raiz do projeto e adicione sua chave da Gemini API:

```env
GEMINI_API_KEY=SUA_CHAVE_AQUI
```

O arquivo `.env` não deve ser enviado para o GitHub.

### 5. Execute o ETL

Antes de abrir o dashboard, rode o pipeline de transações:

```bash
python scripts/etl_transacoes.py
```

Esse comando lê os arquivos em `data/raw/`, processa os dados e gera o arquivo tratado em:

```text
data/processed/transacoes_processadas.csv
```

Caso o arquivo processado não exista, a aplicação ainda consegue usar o arquivo original `data/transacoes.csv` como fallback.

### 6. Execute o Streamlit

```bash
streamlit run src/app.py
```

## Exemplos de Perguntas

O chat pode responder perguntas como:

```text
Em qual categoria eu mais gastei neste período?
```

```text
Qual é meu saldo neste período?
```

```text
Quanto preciso guardar por mês para comprar o notebook?
```

```text
Quanto preciso guardar por mês para montar a reserva?
```

```text
Qual banco oferece o melhor CDB hoje?
```

Para perguntas que dependem de dados externos ou informações em tempo real, o FinanTec deve informar que não possui dados suficientes.

## Avaliação

Foram realizados testes manuais para validar se o agente:

- usa corretamente os dados simulados;
- responde com base nos cálculos feitos em Python;
- evita inventar taxas, bancos ou rankings;
- reconhece limitações da base de conhecimento;
- mantém respostas claras e educativas.

Os testes estão documentados em:

```text
docs/04-metricas.md
```

Também foram criados scripts simples de teste para validar partes do projeto:

| Arquivo | Finalidade |
|---|---|
| `src/teste_dados.py` | Testa leitura de transações e cálculos financeiros. |
| `src/teste_metas.py` | Testa cálculo das metas financeiras. |
| `src/teste_contexto.py` | Exibe o contexto enviado para a IA. |
| `src/teste_ia.py` | Testa uma chamada simples ao assistente com IA. |
| `src/teste_periodos.py` | Testa a listagem e o resumo por período após o ETL. |

## Limitações

O FinanTec não:

- acessa contas bancárias reais;
- utiliza dados financeiros reais de usuários;
- substitui orientação profissional;
- recomenda investimentos personalizados;
- garante rentabilidade ou resultados financeiros;
- consulta taxas ou produtos em tempo real;
- executa operações financeiras.

## Possíveis Evoluções Futuras

Após a entrega inicial e a evolução com ETL, o projeto ainda pode ser expandido com melhorias como:

- salvar dados tratados em SQLite ou PostgreSQL;
- criar uma tabela de categorias padronizadas;
- gerar relatórios financeiros simples em Excel ou PDF;
- permitir upload de uma planilha-modelo pelo usuário;
- criar uma planilha padrão para preenchimento de receitas e despesas;
- validar automaticamente arquivos enviados pelo usuário;
- adicionar filtros por categoria;
- registrar logs mais detalhados do pipeline;
- criar uma automação para mover arquivos processados;
- evoluir para um fluxo simples de RPA;
- usar a IA apenas para explicar indicadores calculados pelo Python.

Essas evoluções não fazem parte da primeira versão do Lab, mas foram consideradas para manter o projeto aberto a melhorias futuras.

## Status

Primeira versão funcional concluída para entrega do Lab.

Versão 2 em evolução com pipeline simples de ETL, múltiplos arquivos mensais e filtro por período no dashboard.