from ..main import API_KEY, STEAM_USERNAME, STEAM_PASSWORD, PATH_TO_STEAMGUARD_FILE
from steam_connection import steam_client_session_decorator
import steammarket as sm


class Scanning:
    def __init__(self, item_name, currency):
        self.item_name = item_name
        self.currency = currency
    
    @staticmethod
    @steam_client_session_decorator(
        api_key=API_KEY,
        username=STEAM_USERNAME,
        password=STEAM_PASSWORD,
        steamguard_path=PATH_TO_STEAMGUARD_FILE
        )
    def test(client) -> dict:
        balance = client.get_wallet_balance()
        response = {'bot balance' : f'{balance}' }
        return balance
    

    def get_csgo_item_data(self) -> dict:
        try:
            item_data = sm.get_csgo_item(item=self.item_name, currency='USD')
                    
            if item_data.get('success'):
            
                response = {
                    'item_name': self.item_name,
                    'item_volume': item_data.get('volume'),
                    'item_lowest_price': item_data.get('lowest_price'),
                    'item_medium_price':item_data.get('median_price')
                }
                
                return  response
            else:
                return {'error_message': f'Could not get data for {self.item_name}', 'item_name': self.item_name}
        
        except Exception as e:
            print(f"An error occurred while fetching data for {self.item_name}: {e}")
            return {'error_message': f'An exception occurred: {e}', 'item_name': self.item_name} 
