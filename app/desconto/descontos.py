def calcular_desconto(valor, cliente_vip):
    if valor <= 0:
        return 0

    if cliente_vip:
        return valor * 0.20
    else:
        return valor * 0.10