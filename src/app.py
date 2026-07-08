from __future__ import annotations

import streamlit as st

from analytics import (
    calcular_gastos_por_categoria,
    calcular_resumo_financeiro,
    formatar_moeda,
)
from data_loader import carregar_transacoes


st.set_page_config(
    page_title="FinanTec",
    page_icon="💰",
    layout="wide",
)


@st.cache_data
def carregar_dados():
    transacoes = carregar_transacoes()
    resumo = calcular_resumo_financeiro(transacoes)
    gastos_por_categoria = calcular_gastos_por_categoria(transacoes)

    return resumo, gastos_por_categoria


resumo, gastos_por_categoria = carregar_dados()


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
