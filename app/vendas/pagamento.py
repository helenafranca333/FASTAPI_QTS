import time
def processar_pagamento(valor:float)->bool:
    """simula o tempo de processamento de um gatway de pagamento"""
    if valor < 0:
        return False
    #simula latencia de rede ou comunicacao com api externa
    time.sleep(0.05)
    return True