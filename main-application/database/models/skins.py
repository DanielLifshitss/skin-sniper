from sqlalchemy import Column, Integer, String, Boolean,ForeignKey, Date
from database import Base
from sqlalchemy.dialects.postgresql import JSONB


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    appid = Column(Integer, ForeignKey("games.id"), nullable=False)
    item_asset_id = Column(Integer)
    item_market_hash_name = Column(String)
    volume = Column(Integer)
    item_lowest_price = Column(String)
    item_median_price = Column(String)


class ItemMarketPricesHistory(Base):
    __tablename__ = "item_market_prices_history"
    
    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer, ForeignKey("items.id"), nullable=False)
    item_price_history = Column(JSONB, nullable=False, default=[])
    bot_scanner_id = Column(Integer, ForeignKey("bot_scanner.id"), nullable=False)
    scan_timestamp = Column(Date)
    

class ItemBought(Base):
    __tablename__ = "item_bought"
    
    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer, ForeignKey("items.id"), nullable=False)
    item_price_bought = Column(Integer)
    bot_buyer_id = Column(Integer, ForeignKey("bot_buyer.id"), nullable=False)
    buy_date_timestamp = Column(Date)
    

class ItemSold(Base):
    __tablename__ = "item_sold"
    
    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer, ForeignKey("items.id"), nullable=False)
    item_price_sold = Column(Integer)
    bot_seller_id = Column(Integer, ForeignKey("bot_seller.id"), nullable=False)
    timestamp = Column(Date)
    




