from ..main import API_KEY, STEAM_USERNAME, STEAM_PASSWORD, PATH_TO_STEAMGUARD_FILE
import steammarket as sm
from steampy.client import SteamClient


def steam_client_session_decorator(api_key, username, password, steamguard_path):
    """
    A decorator to manage a synchronous SteamClient session.
    It handles login and automatic logout for the decorated function.
    """
    def wrapper(func):
        def wrapped_func(*args, **kwargs):
            with SteamClient(api_key) as client:
                client.login(username, password, steamguard_path)
                return func(client, *args, **kwargs)
        return wrapped_func
    return wrapper


class SteamClient:
    def __init__(self, item_name:str = None, currency:str = None, appid:int = None):
        self.item_name = item_name
        self.currency = currency
        self.appid = appid
        
    @steam_client_session_decorator(
        api_key=API_KEY,
        username=STEAM_USERNAME,
        password=STEAM_PASSWORD,
        steamguard_path=PATH_TO_STEAMGUARD_FILE
        )
    def get_item_via_steam_client_session(self, client) -> dict:
        try:
            data = client.get_item(item=self.item_name, appid=self.appid, currency=self.currency)
            if data.get("success"):
                    return {
                        "item_name": self.item_name,
                        "appid": self.appid,
                        "volume": data.get("volume"),
                        "lowest_price": data.get("lowest_price"),
                        "median_price": data.get("median_price"),
                    }
            return {"error": f"Could not get data for {self.item_name}"}
        except Exception as e:
            print(f"SteamMarket error for {self.item_name}: {e}")
            return {"error": str(e)}
    

    def get_csgo_item_data(self) -> dict:
        try:
            item_data = sm.get_csgo_item(item=self.item_name, currency=self.currency)
                    
            if item_data.get('success'):
            
                response = {
                    'item_name': self.item_name,
                    'item_volume': item_data.get('volume'),
                    'item_lowest_price': item_data.get('lowest_price'),
                    'item_medium_price':item_data.get('median_price')
                }
                
                return  response
            else:
                return {'error_message': f'Could not get data for {self.item_name}', 'item_name': self.item_name}
        
        except Exception as e:
            print(f"An error occurred while fetching data for {self.item_name}: {e}")
           
           