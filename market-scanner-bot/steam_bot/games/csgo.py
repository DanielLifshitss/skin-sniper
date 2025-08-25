from core import web_scraper as wb
from core import market_client as mc
from core.market_client import steam_client_session_decorator
from steampy.client import SteamClient
from ..bot.bot import API_KEY, STEAM_USERNAME, STEAM_PASSWORD, PATH_TO_STEAMGUARD_FILE

APPID = 730
CURRENCY = "USD"


#TODO: Need to finish Exceptions and to add Logger Writer

"""
Steam Web Scapping Functions:
-----------------------------


Get Functions:
"""
#Global Skins Queries:
def get_all_knifes_data() -> dict:
    try:
        return wb.SteamWebScraper(item_name="knife", appid=APPID)
    except Exception as e:
        print(f"SteamMarket error for : {e}")
        return {"error": str(e)}

def get_all_gloves_data() -> dict:
    try:
        return wb.SteamWebScraper(item_name="glove", appid=APPID)
    except Exception as e:
        print(f"SteamMarket error for : {e}")
        return {"error": str(e)}


#Counter Terrorist Skins Queries:
def get_all_ak47_data() -> dict:
    try:
        return wb.SteamWebScraper(item_name="", appid=APPID)
    except Exception as e:
        print(f"SteamMarket error for : {e}")
        return {"error": str(e)}


#Terrorist Skins Queries:
def get_all_m4a4_data() -> dict:
    try:
        return wb.SteamWebScraper(item_name="", appid=APPID)
    except Exception as e:
        print(f"SteamMarket error for : {e}")
        return {"error": str(e)}


def get_all_m4a1s_data() -> dict:
    try:
        return wb.SteamWebScraper(item_name="", appid=APPID)
    except Exception as e:
        print(f"SteamMarket error for : {e}")
        return {"error": str(e)}



"""
    Steam Client Functions:
"""
@steam_client_session_decorator(api_key=API_KEY, username=STEAM_USERNAME, password=STEAM_PASSWORD, steamguard_path=PATH_TO_STEAMGUARD_FILE)
def get_item_data(item_name, currency) -> dict:
    try:
        client = mc.SteamClient(client=client)
        return client.get_csgo_item_data(item_name=item_name, currency=currency)
    except Exception as e:
        print(f"SteamMarket error for : {e}")
        return {"error": str(e)}
