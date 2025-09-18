from ..connection import session_to_database
from ..models.bots import Bot, Invenotry, BotScan, BotBuy, BotSell, InventoryHistory
import logging

logger = logging.getLogger(__name__)

@session_to_database
def get_bot_statistics(session) -> None:
    bot_status_req = session.query(Bot)
    
@session_to_database
def create_new_bot(session, bot: dict) -> None:
    pass

@session_to_database
def update_bot_statistics(session, bot_statistics:dict) -> None:
    pass


