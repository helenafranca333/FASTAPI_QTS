import time
import pytest
from app.faturamento.cobranca import processar_cobranca


@pytest.mark.parametrize(
    "valor_base, plano, dias_atraso, resultado_esperado",
    [

        
        (0, "BRONZE", 0, -1.0),
        (-100, "BRONZE", 0, -1.0),
        (100, "BRONZE", -1, -1.0),

        
        (100, "", 0, -2.0),
        (100, "DIAMANTE", 0, -2.0),

        
        (100, "BRONZE", 0, 100.00),
        (100, "PRATA", 0, 85.00),
        (100, "OURO", 0, 75.00),

       
        (100, "BRONZE", 1, 108.40),
        (100, "PRATA", 10, 96.40),
        (100, "BRONZE", 20, 116.00),
        (100, "BRONZE", 21, 146.80),

    ],
)
def test_tabela_decisao(
    valor_base, plano, dias_atraso, resultado_esperado
):
    resultado = processar_cobranca(
        valor_base,
        plano,
        dias_atraso
    )
    assert resultado == resultado_esperado


def test_valor_minimo():
    resultado = processar_cobranca(
        0.01,
        "BRONZE",
        0
    )
    assert resultado == 0.01


@pytest.mark.parametrize(
    "plano, resultado_esperado",
    [

        ("bronze", 100.00),
        (" BRONZE ", 100.00),

    ],
)
def test_variacoes_do_plano(plano, resultado_esperado):
    resultado = processar_cobranca(
        100,
        plano,
        0
    )
    assert resultado == resultado_esperado


def test_arredondamento():
    resultado = processar_cobranca(
        123.45,
        "PRATA",
        7
    )
    assert resultado == 101.91


def test_tempo_de_execucao():
    inicio = time.perf_counter()

    processar_cobranca(
        100,
        "PRATA",
        10
    )

    fim = time.perf_counter()
    tempo = fim - inicio

    assert tempo < 0.08