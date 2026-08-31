def calcular_porcentagem(valor, percentual):
    if not validar_numero(valor) or not validar_numero(percentual):
        raise TypeError("Valores devem ser numericos")
    return (valor * percentual) / 100


def validar_numero(valor):
    return isinstance(valor, (int, float))
