from ..connection import session_to_database
from ..models.items import Item
import logging

logger = logging.getLogger(__name__)

@session_to_database
def get_all_items_form_database(session) -> list:
    try:
        items_query = session.query(Item).all()
        
        resp = [{
            "id": item.id,
            "appid": item.appid,
            "item_asset_id": item.item_asset_id,
            "item_market_hash_name": item.item_market_hash_name,
            "volume": item.volume,
            "item_lowest_price": item.item_lowest_price,
            "item_median_price": item.item_median_price
        } for item in items_query]
        
        logger.info("Database query - getting items succesfuly completed")
        return resp
    except Exception as e:
        logger.error("Could not get items from database")
        return {"error": str(e)} 

@session_to_database
def get_single_item_from_database(session, item_id:int) -> None:
    pass

@session_to_database
def add_new_item_to_database(session, item:dict) -> None:
    pass

@session_to_database
def delete_item_from_database(session, item_id:int) -> None:
    pass

