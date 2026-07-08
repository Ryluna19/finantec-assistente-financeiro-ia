from __future__ import annotations

import pandas as pd


def calcular_gastos_por_categoria(
    transacoes: pd.DataFrame,
    incluir_reserva: bool = False
) -> pd.Series:
    despesas = transacoes[transacoes["tipo"] == "despesa"].copy()

    if not incluir_reserva:
        despesas = despesas[despesas["categoria"] != "Reserva"]

    return (
        despesas.groupby("categoria")["valor"]
        .sum()
        .sort_values(ascending=False)
    )


def calcular_resumo_financeiro(transacoes: pd.DataFrame) -> dict:
    receitas = transacoes.loc[
        transacoes["tipo"] == "receita",
        "valor"
    ].sum()

    despesas_totais = transacoes.loc[
        transacoes["tipo"] == "despesa",
        "valor"
    ].sum()

    valor_reserva = transacoes.loc[
        (transacoes["tipo"] == "despesa")
        & (transacoes["categoria"] == "Reserva"),
        "valor"
    ].sum()

    despesas_do_mes = despesas_totais - valor_reserva
    saldo_disponivel = receitas - despesas_totais

    gastos_por_categoria = calcular_gastos_por_categoria(transacoes)

    maior_categoria = None
    maior_gasto = 0.0

    if not gastos_por_categoria.empty:
        maior_categoria = gastos_por_categoria.index[0]
        maior_gasto = float(gastos_por_categoria.iloc[0])

    return {
        "receitas_totais": float(receitas),
        "despesas_totais": float(despesas_totais),
        "despesas_do_mes": float(despesas_do_mes),
        "valor_guardado_reserva": float(valor_reserva),
        "saldo_disponivel": float(saldo_disponivel),
        "maior_categoria": maior_categoria,
        "maior_gasto": maior_gasto,
    }


def calcular_meta_mensal(
    valor_meta: float,
    prazo_meses: int,
    valor_ja_reservado: float
) -> dict:
    valor_restante = max(valor_meta - valor_ja_reservado, 0)

    if prazo_meses <= 0:
        return {
            "valor_restante": float(valor_restante),
            "valor_mensal_necessario": None,
        }

    valor_mensal_necessario = valor_restante / prazo_meses

    return {
        "valor_restante": float(valor_restante),
        "valor_mensal_necessario": float(valor_mensal_necessario),
    }


def formatar_moeda(valor: float) -> str:
    valor_formatado = f"{valor:,.2f}"

    return (
        "R$ "
        + valor_formatado.replace(",", "X")
        .replace(".", ",")
        .replace("X", ".")
    )
