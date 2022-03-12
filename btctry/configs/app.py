from os import environ as env


class AppConfig:
    APP_NAME = env.get("APP_NAME", "btctry-deta")
    CURRENCY = env.get("CURRENCY", "TRY")
    URI = env.get("URI", "https://api.coindesk.com/v1/bpi/currentprice/{currency}.json").format(currency=CURRENCY)
