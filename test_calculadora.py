from calculadora import validar_numero


def test_validar_numero_aceita_inteiro():
    assert validar_numero(5) is True


def test_validar_numero_rejeita_string():
    assert validar_numero("abc") is False
