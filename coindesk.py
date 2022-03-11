from os import environ as env

import requests

CURRENCY = env.get("CURRENCY", "TRY")
URI = env.get("URI", "https://api.coindesk.com/v1/bpi/currentprice/{currency}.json").format(currency=CURRENCY)
BASE_NAME = env.get("BASE_NAME", "btctry")


def get_btctry() -> dict:
    response = requests.get(URI)
    result = response.json()
    return result


def prepare_for_put() -> dict:
    exchange = get_btctry()
    exchange[CURRENCY] = exchange["bpi"][CURRENCY]["rate"]
    exchange["datetime"] = exchange["time"]["updated"]
    exchange["timeutc"] = exchange["datetime"][-12:]
    return exchange
