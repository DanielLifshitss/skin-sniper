from steampy.client import SteamClient
from dataclasses import dataclass, field
import logging

logger = logging.getLogger(__name__)

#TODO: Need to fix and adjust the Exceptions in all the functions.

def steam_client_session_decorator(api_key, username, password, steamguard_path):
    """
    A decorator to manage a synchronous SteamClient session.
    It handles login and automatic logout for the decorated function.
    """
    def wrapper(func):
        def wrapped_func(*args, **kwargs):
            try:
                with SteamClient(api_key) as client:
                    client.login(username, password, steamguard_path)
                    logger.info("Succesfully created session to Steam Client")
                    return func(client, *args, **kwargs)
            except Exception as e:
                logger.critical(f"An error occurred during a Steam Client session: {e}")
                raise
        return wrapped_func
    return wrapper

    
class SteamClient:
    def __init__(self, client):
        self.client = client
        
        
    """
    Function using steampy library:
    -------------------------------
    """
    def buy_skin_in_market(self, item_name: str, item_buy_price: int, currency:str ) -> dict:
        """
        Places a buy order for a skin on the Steam Community Market at the lowest available price.

        Args:
            client (type(Object)): The authenticated SteamClient instance provided by the decorator.

        Returns:
            dict: A dictionary containing the buy order ID upon success.
            Example: {"response": {"item_name_bought": "Glock-18 | High Beam (Minimal Wear)","order_id": "1234567890"}}
        """
        try:
            logging.info(f"Bot is about to buy the item: {item_name}, for {item_buy_price} {currency}")
            buy_order_id = self.client.market.buy_item_with_lowest_price(item_name, item_buy_price)
            logging.info(f"Bot successfuly bought the item: {item_name}, for {item_buy_price} {currency}")
            return {"response" : {"item_name_bought" : item_name, "order_id" : buy_order_id}}
        except Exception as e:
            logging.error(f"Bot could not buy item:{item_name}, system error: {str(e)}")
            return {"error": str(e)}
    
        
    def sell_skin_on_market(self, item_asset_id:int, appid:int, item_sell_price:int, item_name:str) -> dict:
        """
        Sells an item\skin from bot inventory with the asset_id.

        Args:
            client (type(Object)): The authenticated SteamClient instance provided by the decorator.

        Returns:
            dict: A dictionary containing the sell order ID upon success.
            Example: {"response": {"item_name_sell": "Glock-18 | High Beam (Minimal Wear)","sell_orderid": "1234567890"}}
        """
        try:
            logging.info(f"Bot is about to sell the item: {item_name}, for {item_sell_price}")
            skin_to_sell = self.client.market.create_sell_order(item_asset_id, appid, item_sell_price)
            logging.info(f"Bot successfuly sold the item: {item_name}, for {item_sell_price}")
            return  {"response" : {"item_name_sell" : item_name, "sell_orderid" : skin_to_sell['sell_orderid']}}
        except Exception as e:
            logging.error(f"Bot could not sell item:{item_name}, system error: {str(e)}")
            return {"error": str(e)}
    
    
    def get_bot_item_inventory(self, appid:int) -> dict:
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
            bot_inventory_data = self.client.get_my_inventory(appid)
            
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
            logging.info("Bot got the items informations from inventory successfuly")
            return {'response' : items_in_bot_inventory}
        except Exception as e:
            logging.error("Bot could get items information from inventory")
            return {"error": str(e)}


    def get_bot_listings_items_on_market(self) -> dict:
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
            listings  = self.client.market.get_my_market_listings()
            
            sell_listings_data = [
                {
                    "item_listing_id": listing_id,
                    "item_market_hash_name": details['market_hash_name'],
                    "item_price": details['price']
                }
            for listing_id, details in listings['sell_listings'].items()
            ]
            logging.info('Bot got items listed on the market')
            return {"response" : sell_listings_data}
        except Exception as e:
            logging.error('Bot could not get items listed on the market')
            return {"error": str(e)}
    
    
    def get_bot_wallet_balance(self) -> dict:
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
            wallet_balance = self.client.get_wallet_balance()
            on_hold_wallet_balance = self.client.get_wallet_balance(on_hold = True)
            if wallet_balance or on_hold_wallet_balance:
                response = {"wallet_balance" : wallet_balance / 100.0, "on_hold_wallet_balance": on_hold_wallet_balance / 100.0}
                logging.info("Bot got acount wallet\\on hold wallet balance")
                return {"response" : response}
        except Exception as e:
            logging.error("Bot could not get wallet\\on hold wallet balance")
            return {"error": str(e)}


    def get_item_market_price_history(self, item_name:str, appid:int) -> dict:
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
            query_resp = self.client.market.fetch_price_history(item_name, game=appid)
            if query_resp.get("success"):
                response = {
                    "item_name": item_name,
                    "item_prices_history" : query_resp.get("prices")
                }
                logging.info("Bot got single item market prices history")
                return response
        except Exception as e:
            logging.error("Bot could not get a single item market prices history")
            return {"error": str(e)}
    
    
    def get_item_market_information(self, item_name:str, appid:int, currency:str) -> dict:
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
            data = self.client.get_item(item=item_name, appid=appid, currency=currency)
            if data.get("success"):
                item_data =  {
                    "item_name": item_name,
                    "appid": appid,
                    "volume": data.get("volume"),
                    "lowest_price": data.get("lowest_price"),
                    "median_price": data.get("median_price"),
                }
                logging.info("Bot got single item market information")
                return {"response" : item_data}
        except Exception as e:
            logging.error("Bot could not get single item market information price")
            return {"error": str(e)}
    
    
           