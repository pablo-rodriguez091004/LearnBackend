from suma import suma

def test_suma_correcta():
    assert suma(2, 3) == 5

def test_suma_falla():
    assert suma(2, 3) == 5