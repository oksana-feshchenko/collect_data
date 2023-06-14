import argparse
import csv
import os
from datetime import datetime, timedelta, timezone

from binance.client import Client

from engine import Symbol, Candle, session


FILE_PATH = "app/static/candlestick_info.csv"

def save_to_csv(data, symbol):
    write_header = not os.path.isfile(FILE_PATH)

    with open(FILE_PATH, 'a', newline='') as file:
        writer = csv.writer(file)
        if write_header:
            writer.writerow(['Timestamp', 'Symbol', 'Open', 'High', 'Low', 'Close', 'Volume'])
        rows_to_write = []
        for row in data:
            row.insert(1, symbol)
            rows_to_write.append(row[:7])
        print(rows_to_write)
        writer.writerows(rows_to_write)


#this function for saving data to db
def save_to_db(data, symbol):
    symbol = session.query(Symbol).filter_by(symbol_name=symbol).first()
    if not symbol:
        symbol = Symbol(symbol_name=symbol)
        session.add(symbol)
        session.commit()
    for candle_data in data:
        candle = Candle(symbol=symbol, timestamp=candle_data[0], open=float(candle_data[1]), high=float(candle_data[2]),
                        low=float(candle_data[3]), close=float(candle_data[4]), volume=float(candle_data[5]))
        session.add(candle)
    session.commit()



# we provide symbol, and interval for collecting data
def collect_data(symbol, interval):
    client = Client()
    info_interval = [char for char in interval]
    if info_interval[1] == "d":
        time_diff = timedelta(days=int(info_interval[0]))
    elif info_interval[1] == "h":
        time_diff = timedelta(hours=int(info_interval[0]))
    intervals = {"1d": Client.KLINE_INTERVAL_1DAY, "4h": Client.KLINE_INTERVAL_4HOUR, "1h": Client.KLINE_INTERVAL_1HOUR}
    interval = intervals[interval]
    now = datetime.now(timezone.utc)
    start = now - time_diff
    start = start.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3] + ' UTC'
    end = now.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3] + ' UTC'
    klines = client.get_historical_klines(symbol=symbol, interval=interval, start_str=start, end_str=end)
    save_to_db(klines, symbol)
    for candle in klines:
        candle[0] = datetime.utcfromtimestamp(candle[0] / 1000)
    save_to_csv(klines, symbol)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('symbol', type=str, help='The symbol you want to collect data for')
    parser.add_argument('interval', type=str, help='The interval of the data collection.Options: 1d, 4h, 1h')

    args = parser.parse_args()

    symbol = args.symbol
    interval = args.interval

    collect_data(symbol, interval)





