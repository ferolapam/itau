import pytest
from app.service.receivables import quote_receivable

def test_quote_valid():
    r = quote_receivable(10000, 0.03, 30, "DESCONTO")
    assert r["valor_liquido"] > 0
    assert "desagio" in r

def test_invalid_taxa():
    with pytest.raises(ValueError):
        quote_receivable(1000, 2.0, 10, "DESCONTO")

def test_invalid_tipo():
    with pytest.raises(ValueError):
        quote_receivable(1000, 0.02, 10, "XYZ")
