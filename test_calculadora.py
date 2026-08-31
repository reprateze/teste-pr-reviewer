def test_validar_numero_aceita_inteiro():
    from calculadora import validar_numero

    assert validar_numero(5) == True
