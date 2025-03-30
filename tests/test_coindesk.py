import time

from btctry.utils import get_btctry, prepare_for_put

SLEEP_TIME = 16  # seconds
# This is to avoid hitting the API rate limit
# and to ensure that the tests do not fail due to rate limiting.
# The API rate limit is 4 requests per min.


def test_get_btctry():
    time.sleep(SLEEP_TIME)
    btc = get_btctry()
    assert btc is not None
    assert "bpi" in btc


def test_prepare_for_put():
    time.sleep(SLEEP_TIME)
    base = prepare_for_put()
    assert base is not None
    assert "TRY" in base
