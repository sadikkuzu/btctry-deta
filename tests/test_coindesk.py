from btctry.utils import get_btctry, prepare_for_put


def test_get_btctry():
    btc = get_btctry()
    assert btc is not None
    assert "bpi" in btc


def test_prepare_for_put():
    base = prepare_for_put()
    assert base is not None
    assert "timeutc" in base
