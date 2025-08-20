from sqlalchemy import Column, Integer, String, Boolean
from database import Base


class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True, index=True)
    game_name = Column(String, index=True, unique=True)
    steam_appid = Column(Integer, unique=True, index=True)


