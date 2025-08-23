from ..bot import API_KEY, STEAM_USERNAME, STEAM_PASSWORD, PATH_TO_STEAMGUARD_FILE
import steammarket as sm
from steampy.client import SteamClient
from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any

#TODO: Need to fix and adjust the Exceptions in all the functions.

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
    def __init__(self, item_asset_id:int = None,item_name:str = None,currency:str = None,appid:int = None,item_buy_price:int = None,marketable:bool = None,item_sell_price:int = None):
        
        self.item_asset_id = item_asset_id
        self.item_name = item_name
        self.currency = currency
        self.appid = appid
        self.item_buy_price = item_buy_price
        self.marketable = marketable
        self.item_sell_price = item_sell_price


    """
    Function using steampy library:
    -------------------------------
    """
    @steam_client_session_decorator(api_key=API_KEY, username=STEAM_USERNAME, password=STEAM_PASSWORD, steamguard_path=PATH_TO_STEAMGUARD_FILE)
    def buy_skin_in_market(self, client) -> dict:
        """
        Places a buy order for a skin on the Steam Community Market at the lowest available price.

        Args:
            client (type(Object)): The authenticated SteamClient instance provided by the decorator.

        Returns:
            dict: A dictionary containing the buy order ID upon success.
            Example: {"response": {"item_name_bought": "Glock-18 | High Beam (Minimal Wear)","order_id": "1234567890"}}
        """
        try:
            buy_order_id = client.market.buy_item_with_lowest_price(self.item_name, self.item_buy_price)
            return {"response" : {"item_name_bought" : self.item_name, "order_id" : buy_order_id}}
        except Exception as e:
            print(f"SteamMarket error for {self.item_name}: {e}")
            return {"error": str(e)}
    
        
    @steam_client_session_decorator(api_key=API_KEY, username=STEAM_USERNAME, password=STEAM_PASSWORD, steamguard_path=PATH_TO_STEAMGUARD_FILE)
    def sell_skin_on_market(self, client) -> dict:
        """
        Sells an item\skin from bot inventory with the asset_id.

        Args:
            client (type(Object)): The authenticated SteamClient instance provided by the decorator.

        Returns:
            dict: A dictionary containing the sell order ID upon success.
            Example: {"response": {"item_name_sell": "Glock-18 | High Beam (Minimal Wear)","sell_orderid": "1234567890"}}
        """
        try:
            skin_to_sell = client.market.create_sell_order(self.item_asset_id, self.appid, self.item_sell_price)
            return  {"response" : {"item_name_sell" : self.item_name, "sell_orderid" : skin_to_sell['sell_orderid']}}
        except Exception as e:
            print(f"SteamMarket error for {self.item_name}: {e}")
            return {"error": str(e)}
    
    
    @steam_client_session_decorator(api_key=API_KEY, username=STEAM_USERNAME, password=STEAM_PASSWORD, steamguard_path=PATH_TO_STEAMGUARD_FILE)
    def get_bot_item_inventory(self, client) -> dict:
        """
        Retrieves all items from the bot's Steam inventory for a specified game.

        Args:
            client (type(Object)): The authenticated SteamClient instance provided by the decorator.

        Returns:
           dict: A dictionary containing a list of item details from the inventory.
            Example (Success): 
            {
                "response": [
                    {
                        "item_asset_id": "123456789012345678",
                        "market_hash_name": "AK-47 | Redline (Field-Tested)",
                        "tradable": true,
                        "marketable": true,
                        "classid": "...",
                        "instanceid": "..."
                    },
                    {
                        "item_asset_id": "987654321098765432",
                        "market_hash_name": "AWP | Asiimov (Battle-Scarred)",
                        "tradable": true,
                        "marketable": true,
                        "classid": "...",
                        "instanceid": "..."
                    }
                ]
            }
        """
        try:
            bot_inventory_data = client.get_my_inventory(self.appid)
            
            items_in_bot_inventory = [
                {
                    "item_asset_id":item_asset_id,
                    "market_hash_name":item_details['market_hash_name'],
                    "tradable": item_details['tradable'],
                    "marketable": item_details['marketable'],
                    "classid": item_details['classid'],
                    "instanceid": item_details['instanceid'],
                    
                    
                } for item_asset_id, item_details  in bot_inventory_data.items()
            ]
            
            return {'response' : items_in_bot_inventory}
        except Exception as e:
            print(f"SteamMarket error for {self.item_name}: {e}")
            return {"error": str(e)}


    @steam_client_session_decorator(api_key=API_KEY, username=STEAM_USERNAME, password=STEAM_PASSWORD, steamguard_path=PATH_TO_STEAMGUARD_FILE)
    def get_bot_listings_items_on_market(self, client) -> dict:
        """
        Retrieves the items that are listed by the bot on the steam market.

        Args:
            client (type(Object)): The authenticated SteamClient instance provided by the decorator.

        Returns:
            dict: A dictionary containing lists of sell listings items.
            Example: {
                "response": [
                    {
                        "item_listing_id": "123456789012345678",
                        "item_market_hash_name": "AK-47 | Redline (Field-Tested)",
                        "item_price": "2500"
                    },
                    {
                        "item_listing_id": "987654321098765432",
                        "item_market_hash_name": "AWP | Asiimov (Battle-Scarred)",
                        "item_price": "12500"
                    },
                    ... ]
                }
        """
        try:
            listings  = client.market.get_my_market_listings()
            
            sell_listings_data = [
                {
                    "item_listing_id": listing_id,
                    "item_market_hash_name": details['market_hash_name'],
                    "item_price": details['price']
                }
            for listing_id, details in listings['sell_listings'].items()
            ]
            
            return {"response" : sell_listings_data}
        except Exception as e:
            print(f"SteamMarket error for {self.item_name}: {e}")
            return {"error": str(e)}
    
    
    @steam_client_session_decorator(api_key=API_KEY, username=STEAM_USERNAME, password=STEAM_PASSWORD, steamguard_path=PATH_TO_STEAMGUARD_FILE)
    def get_bot_wallet_balance(self, client) -> dict:
        """    
        Retrieves the Steam wallet balance and any funds on hold for the authenticated account.

        Args:
            client (type(Object)): The authenticated SteamClient instance provided by the decorator.

        Returns:
            dict: A dictionary containing the wallet summary of the bot acount. 
            Example: {"response": {"wallet_balance" : 100, "on_hold_wallet_balance": 100}}
            The balance is in return from the function in Centes -> converting it to dollares and return it in response in dollars.
        """
        try:
            wallet_balance = client.get_wallet_balance()
            on_hold_wallet_balance = client.get_wallet_balance(on_hold = True)
            if wallet_balance or on_hold_wallet_balance:
                response = {"wallet_balance" : wallet_balance / 100.0, "on_hold_wallet_balance": on_hold_wallet_balance / 100.0}
                return {"response" : response}
        except Exception as e:
            print(f"SteamMarket error for {self.item_name}: {e}")
            return {"error": str(e)}


    @steam_client_session_decorator(api_key=API_KEY, username=STEAM_USERNAME, password=STEAM_PASSWORD, steamguard_path=PATH_TO_STEAMGUARD_FILE)
    def get_item_market_price_history(self, client) -> dict:
        """
        Retrieves the price history of item\skin. 

        Args:
            client (type(Object)): The authenticated SteamClient instance provided by the decorator.

        Returns:
            dict: A dictionary containing the item name\skin name and its prices history -> in List.
            Example: 
            {
                "response": {
                    "item_name" : "Glock-18 | High Beam (Minimal Wear)",
                    "item_prices_history": [
                            ["Jul 02 2014 01: +0", 417.777, "40"],
                            ["Jul 03 2014 01: +0", 415.555, "52"],
                            ["Jul 04 2014 01: +0", 412.345, "60"]
                        ]
                    }
            }
        """
        try:
            query_resp = client.market.fetch_price_history(self.item_name, game=self.appid)
            if query_resp.get("success"):
                response = {
                    "item_name": self.item_name,
                    "item_prices_history" : query_resp.get("prices")
                }
                return response
        except Exception as e:
            print(f"SteamMarket error for {self.item_name}: {e}")
            return {"error": str(e)}
    
    
    @steam_client_session_decorator(api_key=API_KEY, username=STEAM_USERNAME, password=STEAM_PASSWORD, steamguard_path=PATH_TO_STEAMGUARD_FILE)
    def get_item_market_information(self, client) -> dict:
        """
        Retrieves information about an item\skin. 

        Args:
            client (type(Object)): The authenticated SteamClient instance provided by the decorator.

        Returns:
            dict: A dictionary containing the item information: item name,vloume,lowest\median price and its appid -> what game the item\skin is assosiated.
            Example: 
            {
                "response": {
                    "item_name": "M4A1-S | Cyrex (Factory New)",
                    "appid": 730,
                    "volume": 208,
                    "lowest_price": "$11.30 USD",
                    "median_price": "$11.33 USD",
                }
            }
        """
        try:
            data = client.get_item(item=self.item_name, appid=self.appid, currency=self.currency)
            if data.get("success"):
                item_data =  {
                    "item_name": self.item_name,
                    "appid": self.appid,
                    "volume": data.get("volume"),
                    "lowest_price": data.get("lowest_price"),
                    "median_price": data.get("median_price"),
                }
                return {"response" : item_data}
            return {"error": f"Could not get data for {self.item_name}"}
        except Exception as e:
            print(f"SteamMarket error for {self.item_name}: {e}")
            return {"error": str(e)}
    
    
    """
    Function Using steammarket library:
    -----------------------------------
    """
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
           
           