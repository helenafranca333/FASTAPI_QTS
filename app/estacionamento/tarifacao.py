
HORAS_MAX_CURTAS = 4
TARIFA_HORA_CURTA = 4.00
TARIFA_HORA_LONGA = 2.50
TAXA_ADMINISTRATIVA = 6.00


def calcular_valor_vaga(horas: int, perfil_usuario: str = "visitante") -> float:

    if horas <= 0:
        valor = 0.0

    elif horas <= HORAS_MAX_CURTAS:
        valor = horas * TARIFA_HORA_CURTA

    else:
        valor = (horas * TARIFA_HORA_LONGA) + TAXA_ADMINISTRATIVA

    return round(valor, 2)
