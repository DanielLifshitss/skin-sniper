from sqlalchemy import Column, Integer, String, Boolean,ForeignKey
from database import Base
from sqlalchemy.dialects.postgresql import JSONB


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    appid = Column(Integer, ForeignKey(), nullable=True)
    item_asset_id = Column(Integer)
    item_market_hash_name = Column(String)
    volume = Column(Integer)
    item_lowest_price = Column(String)
    item_median_price = Column(String)


class ItemHistory(Base):
    __tablename__ = "item_history"
    
    id = Column(Integer, primary_key=True, index=True)
    item_price_history = Column(JSONB, nullable=False, default=[])
    bot_scanner_id = Column(Integer, ForeignKey("bot_scanner.id"), nullable=False)
    
    




