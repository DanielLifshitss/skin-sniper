import steammarket as sm

class Scanning:
    def __init__(self, item_name, currency):
        self.item_name = item_name
        self.currency = currency
    
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
    
    