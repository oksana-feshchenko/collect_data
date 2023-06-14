import csv

import requests

TEN_SYMBOLS = ["BTCUSDT", "ETHUSDT", "BNBUSDT", "SUIUSDT", "IDUSDT", "RDNTUSDT", "ADAUSDT", "SOLUSDT","DOTUSDT", "DAIUSDT"]

URL = 'https://www.binance.com/exchange-api/v2/public/asset-service/product/get-products'

FILE_PATH = "app/static/market_cap_ten_symbols.csv"

def save_to_csv(filtered_data):
    with open(FILE_PATH, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Symbol', 'Close Price', 'Circulating supply'])
        writer.writerows(filtered_data)


def get_market_cap_date():
    response = requests.get(URL)
    data = response.json()
    filtered_data = []
    for item in data['data']:
        if item['s'] in TEN_SYMBOLS:
            filtered_data.append([
                item['s'],
                item['c'],
                item['cs']
            ])

    save_to_csv(filtered_data)


if __name__ == '__main__':
    get_market_cap_date()





