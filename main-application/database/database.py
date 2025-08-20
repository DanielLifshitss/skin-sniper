from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine


Base = declarative_base()

engine = create_engine("mysql+mysqlconnector://{connection-string-sensitive}",
                       pool_size=150, max_overflow=300)

Base.metadata.create_all(engine)