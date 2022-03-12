from deta import App, Deta
from fastapi import FastAPI

from btctry.configs import AppConfig, DetaConfig
from btctry.utils import get_btctry, save_btctry

app = App(
    FastAPI(
        title=AppConfig.APP_NAME,
    ),
)
deta = Deta()
db = deta.Base(DetaConfig.BASE_NAME)


@app.get("/", summary="Get BTC Exchange")
def get():
    exchange = get_btctry()
    return exchange


@app.get("/save", summary="Save BTC Exchange")
def save():
    saved = save_btctry(db)
    return saved


@app.lib.cron()
def cron_job(event):
    record = save_btctry(db)
    return record
