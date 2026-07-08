# FinanTec

Assistente de organização financeira para estudantes e pessoas em início de carreira.

Projeto desenvolvido para o Lab **Construa Seu Assistente Virtual com Inteligência Artificial**, da DIO.

## Sobre o Projeto

O FinanTec é um protótipo de assistente financeiro educativo que utiliza dados simulados para ajudar uma pessoa usuária a entender melhor receitas, gastos, saldo mensal e metas financeiras.

O projeto combina análise de dados com Python, uma interface em Streamlit e IA generativa para explicar os resultados de forma simples e contextualizada.

A proposta não é criar uma solução financeira completa, mas demonstrar como um assistente virtual pode usar uma base de conhecimento organizada para responder perguntas com mais segurança.

## Objetivo

Ajudar estudantes, estagiários e pessoas em início de carreira a:

- visualizar receitas e gastos do mês;
- identificar categorias de maior consumo;
- acompanhar metas financeiras;
- entender conceitos financeiros básicos;
- receber explicações simples com apoio de IA generativa;
- reconhecer quando não há dados suficientes para uma resposta segura.

## Funcionalidades

- Dashboard financeiro com resumo mensal;
- cálculo de receitas, gasto de consumo no mês, reserva e saldo disponível;
- gráfico de gastos por categoria;
- identificação da maior categoria de consumo;
- simulador de metas financeiras;
- chat com IA generativa usando contexto dos dados simulados;
- respostas com regras para evitar invenção de dados;
- documentação dos passos do desafio.

## Tecnologias Utilizadas

- Python
- pandas
- Streamlit
- python-dotenv
- google-genai
- CSV
- JSON
- Gemini API

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

Os cálculos financeiros são feitos pela aplicação em Python. A IA generativa é usada para interpretar perguntas e explicar os resultados, não para inventar valores.

## Base de Conhecimento

A pasta `data/` contém dados simulados usados pelo projeto:

| Arquivo | Finalidade |
|---|---|
| `perfil_usuario.json` | Perfil fictício da pessoa usuária, renda, situação atual e metas. |
| `transacoes.csv` | Receitas e despesas simuladas de um mês. |
| `historico_atendimento.csv` | Dúvidas anteriores e respostas resumidas. |
| `conceitos_financeiros.json` | Conceitos básicos de organização financeira. |
| `produtos_financeiros.json` | Produtos financeiros descritos apenas para fins educativos. |

A pessoa fictícia usada no projeto é Marina Costa, estudante universitária e estagiária.

## Estrutura do Projeto

```text
finantec-assistente-financeiro-ia/
├── assets/
├── data/
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
├── src/
│   ├── agent.py
│   ├── analytics.py
│   ├── app.py
│   ├── data_loader.py
│   ├── prompts.py
│   ├── teste_contexto.py
│   ├── teste_dados.py
│   ├── teste_ia.py
│   └── teste_metas.py
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

### 5. Execute o Streamlit

```bash
streamlit run src/app.py
```

## Exemplos de Perguntas

O chat pode responder perguntas como:

```text
Em qual categoria eu mais gastei este mês?
```

```text
Qual é meu saldo mensal?
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

Após a entrega inicial do Lab, o projeto pode ser evoluído para um estudo mais completo de dados e automação, sem precisar refazer sua estrutura principal.

Algumas possibilidades:

- organizar os dados em etapas de `raw` e `processed`;
- criar um pipeline simples de ETL com Python;
- validar dados antes da análise;
- salvar dados tratados em SQLite ou PostgreSQL;
- registrar logs de processamento;
- criar novos meses de transações simuladas;
- adicionar filtros por período e categoria;
- gerar relatórios financeiros simples;
- usar a IA apenas para explicar indicadores calculados pelo Python.

Essas evoluções não fazem parte da primeira versão do Lab, mas foram consideradas para manter o projeto aberto a melhorias futuras.

## Status

Primeira versão funcional concluída para entrega do Lab.