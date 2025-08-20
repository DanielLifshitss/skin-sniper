from sqlalchemy import Column, Integer, String, Boolean
from database import Base


class SystemLogger(Base):
    __tablename__ = "system_logger"

    id = Column(Integer, primary_key=True, index=True)

class ApplicationLogger(Base):
    __tablename__ = "application_logger"

    id = Column(Integer, primary_key=True, index=True)
    
class SteamLogger(Base):
    __tablename__ = "steam_logger"

    id = Column(Integer, primary_key=True, index=True)

class BotLogger(Base):
    __tablename__ = "bot_logger"

    id = Column(Integer, primary_key=True, index=True)

