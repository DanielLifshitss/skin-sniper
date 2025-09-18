from core import market_client as mc
from games import general as gen_scan_func
from database.crud import bot as botcrud
from database.crud import item as itemcrud
import logging

 
logger = logging.getLogger(__name__)


def scanner_bot_data() -> dict:
    itemcrud.get_item_form_db()
    
    
    
    
async def scanner_bot():
    
    _scanner_bot_data = scanner_bot_data()
    gen_scan_func.get_item_data(item_name=None)

    