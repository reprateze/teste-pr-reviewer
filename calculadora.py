def calcular_desconto(valor, percentual):
    if valor <= 0:
        raise ValueError("Valor inválido")

    if percentual < 0 or percentual > 100:
        raise ValueError("Percentual inválido")

    return valor - (valor * percentual / 100)
