from core import web_scraper as wb
from core import market_client as mc
from core.market_client import steam_client_session_decorator
from steampy.client import SteamClient
from ..bot import API_KEY, STEAM_USERNAME, STEAM_PASSWORD, PATH_TO_STEAMGUARD_FILE




@steam_client_session_decorator(api_key=API_KEY, username=STEAM_USERNAME, password=STEAM_PASSWORD, steamguard_path=PATH_TO_STEAMGUARD_FILE)
def get_item_data(item_name, currency) -> dict:
    try:
        client = mc.SteamClient(client=client)
        return client.get_item_market_information(item_name=None, appid=None, currency=None)
    except Exception as e:
        print(f"SteamMarket error for : {e}")
        return {"error": str(e)}
    
@steam_client_session_decorator(api_key=API_KEY, username=STEAM_USERNAME, password=STEAM_PASSWORD, steamguard_path=PATH_TO_STEAMGUARD_FILE)
def get_item_data(item_name, currency) -> dict:
    try:
        client = mc.SteamClient(client=client)
        return client.get_item_market_information(item_name=None, appid=None, currency=None)
    except Exception as e:
        print(f"SteamMarket error for : {e}")
        return {"error": str(e)}