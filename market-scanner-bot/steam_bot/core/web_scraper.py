from bs4 import BeautifulSoup
import steammarket as sm
import requests
import time

class SteamWebScraper:
    BASE_URL = "https://steamcommunity.com/market/search/render/"
    
    @staticmethod
    def get_item_via_steam_url(item_type_name: str, appid: int) -> list:
        item_names = []
        start = 0
        while True:
            params = {
                'query': item_type_name,
                'appid': appid,
                'start': start,
                'count': 100
            }
            response = requests.get(SteamWebScraper.BASE_URL, params=params)
            data = response.json()
            
            if 'results_html' not in data or not data['results_html'].strip():
                break
            
            soup = BeautifulSoup(data['results_html'], 'html.parser')
            items = soup.find_all('span', class_='market_listing_item_name')
            
            if not items:
                break
            
            for item in items:
                item_names.append(item.text)
            
            start += 100
            time.sleep(1)
        return item_names