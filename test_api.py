from api import obter_cotacao

def test_cotacao():
    valor = obter_cotacao("USD")
    assert valor is not None
    assert valor > 0
