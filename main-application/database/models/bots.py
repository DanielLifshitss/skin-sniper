from sqlalchemy import Column, Integer, String, Boolean
from database import Base


class Bot(Base):
    __tablename__ = "bots"

    id = Column(Integer, primary_key=True, index=True)


class BotScan(Base):
    __tablename__ = "bot_scans"

    id = Column(Integer, primary_key=True, index=True)
    

class BotSell(Base):
    __tablename__ = "bot_sells"

    id = Column(Integer, primary_key=True, index=True)
    

class BotBuy(Base):
    __tablename__ = "bot_buys"

    id = Column(Integer, primary_key=True, index=True)
    

