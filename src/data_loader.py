from __future__ import annotations

import json
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"


def carregar_json(nome_arquivo: str) -> dict:
    caminho = DATA_DIR / nome_arquivo

    with caminho.open("r", encoding="utf-8-sig") as arquivo:
        return json.load(arquivo)


def carregar_perfil_usuario() -> dict:
    return carregar_json("perfil_usuario.json")


def carregar_conceitos_financeiros() -> dict:
    return carregar_json("conceitos_financeiros.json")


def carregar_produtos_financeiros() -> dict:
    return carregar_json("produtos_financeiros.json")


def carregar_transacoes() -> pd.DataFrame:
    caminho = DATA_DIR / "transacoes.csv"

    transacoes = pd.read_csv(
        caminho,
        encoding="utf-8-sig",
        parse_dates=["data"]
    )

    transacoes["tipo"] = transacoes["tipo"].str.strip().str.lower()
    transacoes["categoria"] = transacoes["categoria"].str.strip()
    transacoes["valor"] = pd.to_numeric(transacoes["valor"], errors="coerce")

    return transacoes


def carregar_historico_atendimento() -> pd.DataFrame:
    caminho = DATA_DIR / "historico_atendimento.csv"

    return pd.read_csv(
        caminho,
        encoding="utf-8-sig",
        parse_dates=["data"]
    )
