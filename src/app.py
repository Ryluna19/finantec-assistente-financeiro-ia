from __future__ import annotations

import streamlit as st

from agent import gerar_resposta_finantec
from analytics import (
    calcular_gastos_por_categoria,
    calcular_meta_mensal,
    calcular_resumo_financeiro,
    calcular_simulacoes_de_metas,
    formatar_moeda,
)
from data_loader import (
    carregar_conceitos_financeiros,
    carregar_historico_atendimento,
    carregar_perfil_usuario,
    carregar_produtos_financeiros,
    carregar_transacoes,
)
from prompts import montar_contexto


st.set_page_config(
    page_title="FinanTec",
    page_icon="💰",
    layout="wide",
)


@st.cache_data
def carregar_dados():
    perfil_usuario = carregar_perfil_usuario()
    transacoes = carregar_transacoes()
    historico_atendimento = carregar_historico_atendimento()
    conceitos_financeiros = carregar_conceitos_financeiros()
    produtos_financeiros = carregar_produtos_financeiros()

    resumo = calcular_resumo_financeiro(transacoes)
    gastos_por_categoria = calcular_gastos_por_categoria(transacoes)
    simulacoes_metas = calcular_simulacoes_de_metas(perfil_usuario)
 
    contexto = montar_contexto(
        perfil_usuario=perfil_usuario,
        resumo_financeiro=resumo,
        gastos_por_categoria=gastos_por_categoria,
        simulacoes_metas=simulacoes_metas,
        historico_atendimento=historico_atendimento,
        conceitos_financeiros=conceitos_financeiros,
        produtos_financeiros=produtos_financeiros,
    )

    return perfil_usuario, resumo, gastos_por_categoria, contexto


perfil_usuario, resumo, gastos_por_categoria, contexto = carregar_dados()


if "mensagens" not in st.session_state:
    st.session_state.mensagens = [
        {
            "role": "assistant",
            "content": (
                "Olá! Sou o FinanTec. Posso ajudar você a entender seus "
                "gastos, metas e conceitos financeiros básicos."
            ),
        }
    ]


st.title("💰 FinanTec")
st.caption(
    "Assistente de organização financeira para estudantes e pessoas em início de carreira."
)

st.warning(
    "Projeto educativo com dados simulados. O FinanTec não oferece recomendação "
    "personalizada de investimento."
)


st.subheader("Resumo financeiro do mês")

coluna_receita, coluna_consumo, coluna_reserva, coluna_saldo = st.columns(4)

coluna_receita.metric(
    "Receitas",
    formatar_moeda(resumo["receitas_totais"]),
)

coluna_consumo.metric(
    "Gasto de consumo no mês",
    formatar_moeda(resumo["despesas_do_mes"]),
)

coluna_reserva.metric(
    "Valor separado para reserva",
    formatar_moeda(resumo["valor_guardado_reserva"]),
)

coluna_saldo.metric(
    "Saldo disponível",
    formatar_moeda(resumo["saldo_disponivel"]),
)


st.subheader("Gastos de consumo por categoria")

gastos_tabela = gastos_por_categoria.rename("Valor").reset_index()
gastos_tabela.columns = ["Categoria", "Valor"]

st.bar_chart(
    gastos_tabela,
    x="Categoria",
    y="Valor",
)

if resumo["maior_categoria"]:
    st.info(
        f"A maior categoria de consumo foi **{resumo['maior_categoria']}**, "
        f"com {formatar_moeda(resumo['maior_gasto'])}."
    )


st.divider()

st.subheader("Simulador de metas financeiras")

st.write(
    "Escolha uma meta cadastrada no perfil da Marina para estimar quanto ainda "
    "precisa ser guardado por mês."
)

metas = perfil_usuario["objetivos_financeiros"]
nomes_metas = [meta["nome"] for meta in metas]

nome_meta_escolhida = st.selectbox(
    "Meta",
    nomes_metas,
)

meta_escolhida = next(
    meta
    for meta in metas
    if meta["nome"] == nome_meta_escolhida
)

valor_meta = float(meta_escolhida["valor_meta"])
valor_atual = float(meta_escolhida["valor_atual"])
prazo_meses = int(meta_escolhida["prazo_meses"])

simulacao = calcular_meta_mensal(
    valor_meta=valor_meta,
    prazo_meses=prazo_meses,
    valor_ja_reservado=valor_atual,
)

coluna_meta, coluna_atual, coluna_restante, coluna_mensal = st.columns(4)

coluna_meta.metric(
    "Valor da meta",
    formatar_moeda(valor_meta),
)

coluna_atual.metric(
    "Valor atual",
    formatar_moeda(valor_atual),
)

coluna_restante.metric(
    "Falta guardar",
    formatar_moeda(simulacao["valor_restante"]),
)

coluna_mensal.metric(
    "Necessário por mês",
    formatar_moeda(simulacao["valor_mensal_necessario"]),
)

if simulacao["valor_mensal_necessario"] > resumo["saldo_disponivel"]:
    st.error(
        "Para essa meta, o valor mensal necessário é maior que o saldo disponível "
        "do mês. Pode ser necessário aumentar o prazo, reduzir gastos ou buscar "
        "renda extra."
    )
else:
    st.success(
        "Considerando apenas essa meta, o valor mensal necessário cabe no saldo "
        "disponível deste mês."
    )

st.caption(
    "Observação: a análise considera uma meta por vez. Se Marina tentar cumprir "
    "várias metas ao mesmo tempo, será necessário somar os valores mensais."
)


st.divider()

st.subheader("Converse com o FinanTec")

st.caption(
    "Teste perguntas como: “Em qual categoria eu mais gastei?”, "
    "“Qual é meu saldo mensal?”, “Quanto preciso guardar para o notebook?” "
    "ou “Qual banco oferece o melhor CDB hoje?”"
)

for mensagem in st.session_state.mensagens:
    with st.chat_message(mensagem["role"]):
        st.markdown(mensagem["content"])

pergunta_usuario = st.chat_input("Digite sua pergunta sobre organização financeira")

if pergunta_usuario:
    st.session_state.mensagens.append(
        {
            "role": "user",
            "content": pergunta_usuario,
        }
    )

    with st.chat_message("user"):
        st.markdown(pergunta_usuario)

    with st.chat_message("assistant"):
        with st.spinner("Analisando os dados disponíveis..."):
            try:
                resposta = gerar_resposta_finantec(
                    pergunta_usuario=pergunta_usuario,
                    contexto=contexto,
                )
                st.markdown(resposta)

            except RuntimeError as erro:
                resposta = str(erro)
                st.error(resposta)

    st.session_state.mensagens.append(
        {
            "role": "assistant",
            "content": resposta,
        }
    )
