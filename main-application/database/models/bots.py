from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Date
from sqlalchemy.dialects.postgresql import JSONB
from database import Base


class Bot(Base):
    
    __tablename__ = "bots"

    id = Column(Integer, primary_key=True, index=True)
    bot_inventory_items = Column(Integer, ForeignKey("inventory.id"), nullable=False)
    bot_inventory_value = Column(Integer, nullable=False)


class Invenotry(Base):
    __tablename__ = "invenotry"
    
    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer, ForeignKey('items.id'), nullable=False)
    tradeable = Column(Boolean, nullable=False)
    marketable = Column(Boolean, nullable=False)
    item_price = Column()
    item_bought_for = Column(Integer, ForeignKey("item_bought.id"))
    timestamp = Column(Date)


class InventoryHistory(Base):
    __tablename__ = "inventory_history"
    
    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer, ForeignKey('items.id'), nullable=False)
    item_price = Column()
    item_bought_for = Column(Integer, ForeignKey("item_bought.id"))
    item_sold_for = Column(Integer, ForeignKey("item_sold.id"))
    timestamp = Column(Date)
    
    
    
class BotScan(Base):
    __tablename__ = "bot_scans"

    id = Column(Integer, primary_key=True, index=True)
    
    

class BotSell(Base):
    __tablename__ = "bot_sells"

    id = Column(Integer, primary_key=True, index=True)
    
    

class BotBuy(Base):
    __tablename__ = "bot_buys"

    id = Column(Integer, primary_key=True, index=True)
    


