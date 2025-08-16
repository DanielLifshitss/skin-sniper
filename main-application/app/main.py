from fastapi import FastAPI
from api.v1.routers import market_scanner_bot_api, data_service_api


app = FastAPI(title="Skin Sniper Application")
app.include_router(market_scanner_bot_api.router)
app.include_router(data_service_api.router)


@app.get('/')
def test_main_application_api():
    return {'response' : 'main application api success'}


