from app.desconto.descontos import calcular_desconto


def test_valor_zero():
    assert calcular_desconto(0, True) == 0


def test_valor_negativo():
    assert calcular_desconto(-100, False) == 0


def test_cliente_vip():
    assert calcular_desconto(100, True) == 20


def test_cliente_nao_vip():
    assert calcular_desconto(100, False) == 10


def test_valor_pequeno_vip():
    resultado = calcular_desconto(0.01, True)
    assert round(resultado, 3) == 0.002


def test_valor_pequeno_nao_vip():
    resultado = calcular_desconto(0.01, False)
    assert round(resultado, 3) == 0.001


def test_valor_maior_vip():
    assert calcular_desconto(200, True) == 40


def test_valor_maior_nao_vip():
    assert calcular_desconto(200, False) == 20