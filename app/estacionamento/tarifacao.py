
def calcular_valor_vaga(horas: int, perfil_usuario: str = "visitante") -> float:

    if horas <= 0:
        return 0.0

    elif horas <= 4:
        return horas * 4.00

    else:
        return (horas * 2.50) + 6.00
