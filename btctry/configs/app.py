from os import environ as env


class AppConfig:
    APP_NAME = env.get("APP_NAME", "btctry-deta")
    CURRENCY = env.get("CURRENCY", "TRY")
    URI = env.get("URI", "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies={currency}").format(
        currency=CURRENCY.lower(),
    )
