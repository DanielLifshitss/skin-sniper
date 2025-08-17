from steampy.client import SteamClient


#TODO: create steam connection wrapper
def steam_client_session_decoratir(func):
    def wrapper(*args, **kwargs):
        steam_session = ""
        return steam_session
    return wrapper