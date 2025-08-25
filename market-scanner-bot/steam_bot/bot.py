from dotenv import load_dotenv
import os
from ..core import market_client as ms

#Loading Steam Cradentials:
load_dotenv()

API_KEY = os.getenv('API_KEY')
STEAM_USERNAME = os.getenv('STEAM_USERNAME')
STEAM_PASSWORD = os.getenv('STEAM_PASSWORD')
PATH_TO_STEAMGUARD_FILE = os.getenv('PATH_TO_STEAMGUARD_FILE')




