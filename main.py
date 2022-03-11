from deta import App, Deta
from fastapi import FastAPI

from coindesk import BASE_NAME, get_btctry, prepare_for_put

app = App(FastAPI())
deta = Deta()
db = deta.Base(BASE_NAME)


@app.get("/")
def http():
    exchange = get_btctry()
    return exchange


@app.lib.cron()
def cron_job(event):
    data = prepare_for_put()
    record = db.put(data)
    return record
