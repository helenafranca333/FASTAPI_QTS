from app.classificacao.status import calcular_status_pedido

def test_retorna_invalido_valor_zero():
    assert calcular_status_pedido(0,True)=="invalido"
def test_retorna_invalido_valor_negativo():
    assert calcular_status_pedido(-10,False)=="invalido"
def test_retorna_pendente_nao_pago():
    assert calcular_status_pedido(120,False)=="pendente"
def test_retorna_confirmado_valor_valido():
    assert calcular_status_pedido(120,True)=="confirmado"