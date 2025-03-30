import pytest

from btctry.utils import get_btctry, prepare_for_put
from btctry.configs import AppConfig


# Mock data as in CoinGecko API format
MOCK_COINGECKO_DATA = {"bitcoin": {"try": 3163692}}


@pytest.fixture
def mock_coingecko_response(mocker):
    # Configure the mock to return a response with sample data
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = MOCK_COINGECKO_DATA

    # Mock the requests.get method
    mock_get = mocker.patch('btctry.utils.coingecko.requests.get', return_value=mock_response)
    return mock_get


def test_get_btctry_mocked(mock_coingecko_response):
    btc = get_btctry()
    assert btc is not None
    assert "bpi" in btc
    assert AppConfig.CURRENCY in btc["bpi"]

    # Verify the rate data
    currency_data = btc["bpi"][AppConfig.CURRENCY]
    assert currency_data["code"] == AppConfig.CURRENCY
    assert float(currency_data["rate"]) == float(MOCK_COINGECKO_DATA["bitcoin"][AppConfig.CURRENCY.lower()])
    assert currency_data["rate_float"] == MOCK_COINGECKO_DATA["bitcoin"][AppConfig.CURRENCY.lower()]

    # Verify request was made with the correct URL
    mock_coingecko_response.assert_called_once_with(AppConfig.URI)


def test_prepare_for_put(mock_coingecko_response):
    result = prepare_for_put()
    assert result is not None

    # Verify that specific fields are present
    assert AppConfig.CURRENCY in result

    # Check the values
    assert result[AppConfig.CURRENCY] == str(MOCK_COINGECKO_DATA["bitcoin"][AppConfig.CURRENCY.lower()])

    # Verify request count
    assert mock_coingecko_response.call_count == 1
