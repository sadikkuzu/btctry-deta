import requests

from btctry.configs import AppConfig


def get_btctry() -> dict:
    response = requests.get(AppConfig.URI)
    result = response.json()
    return result


def prepare_for_put() -> dict:
    exchange = get_btctry()
    exchange[AppConfig.CURRENCY] = exchange["bpi"][AppConfig.CURRENCY]["rate"]
    exchange["datetime"] = exchange["time"]["updated"]
    exchange["timeutc"] = exchange["datetime"][-12:]
    return exchange


def save_btctry(db) -> dict:  # pragma: no cover
    data = prepare_for_put()
    record = db.put(data)
    return record
