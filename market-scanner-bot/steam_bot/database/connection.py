from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Session
from database import engine

def session_to_database(func):
    """
    Decorator which opens database session if its not already provided, passes it to the database function, and closes
    it after the function is finished.
    :param func:
    :return session:
    """

    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, Session):
                return func(*args, **kwargs)

        session = create_session()
        result = func(session, *args, **kwargs)
        close_session(session)
        return result

    return wrapper


def create_session():
    """
    Creates session with the global engine, and returns it.
    """

    return Session(engine)


def close_session(session):
    """
    Closes the provided session.
    :param session:
    """

    session.close()