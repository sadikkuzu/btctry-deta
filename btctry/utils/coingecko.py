import requests

from btctry.configs import AppConfig


def get_btctry() -> dict:
    response = requests.get(AppConfig.URI)
    result = response.json()
    formatted_result = {
        "bpi": {
            AppConfig.CURRENCY: {
                "code": AppConfig.CURRENCY,
                "rate": str(result["bitcoin"][AppConfig.CURRENCY.lower()]),
                "rate_float": float(result["bitcoin"][AppConfig.CURRENCY.lower()]),
            },
        },
    }
    return formatted_result


def prepare_for_put() -> dict:
    exchange = get_btctry()
    exchange[AppConfig.CURRENCY] = exchange["bpi"][AppConfig.CURRENCY]["rate"]
    return exchange


def save_btctry(db) -> dict:  # pragma: no cover
    data = prepare_for_put()
    record = db.put(data)
    return record
