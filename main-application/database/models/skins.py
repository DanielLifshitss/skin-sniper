from sqlalchemy import Column, Integer, String, Boolean
from database import Base


class Skins(Base):
    __tablename__ = "skins"

    id = Column(Integer, primary_key=True, index=True)



