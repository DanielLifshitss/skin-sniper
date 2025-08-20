from ..main import API_KEY, STEAM_USERNAME, STEAM_PASSWORD, PATH_TO_STEAMGUARD_FILE
from steam_connection import steam_client_session_decorator


@steam_client_session_decorator(api_key=API_KEY,username=STEAM_USERNAME,password=STEAM_PASSWORD, steamguard_path=PATH_TO_STEAMGUARD_FILE)
def test(client):
    client
    return "True"


