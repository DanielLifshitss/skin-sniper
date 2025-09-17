from dotenv import load_dotenv
import os
import logging

#Loading Steam Cradentials:
load_dotenv()

API_KEY = os.getenv('API_KEY')
STEAM_USERNAME = os.getenv('STEAM_USERNAME')
STEAM_PASSWORD = os.getenv('STEAM_PASSWORD')
PATH_TO_STEAMGUARD_FILE = os.getenv('PATH_TO_STEAMGUARD_FILE')
DB_URL = os.getenv('DB_URL')

log_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'bot.log')

# Configure the root logger
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
)

# Get a logger for the main script
logger = logging.getLogger(__name__)