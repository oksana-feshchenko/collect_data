

Installation
1. Clone the repository:
```
git clone https://github.com/oksana-feshchenko/collect_data
```
2. Navigate to the project directory:

```
git clone https://github.com/oksana-feshchenko/collect_data
```

3. Create a virtual environment:

```
python -m venv venv
venv\Scripts\activate (on Windows)
source venv/bin/activate (on macOS)
pip install -r requirements.txt
```

4. Install the dependencies:

```
pip install -r requirements.txt
``` 

5. Collect data and write it to csv.file.

collect_candlesticks_data.py - script is designed to collect candlestick data from the Binance API and save it to a CSV file and a relational database.
It utilizes the Binance API client, and SQLAlchemy for database operations.

Provide symbol and interval for which you want to know latest info.Run the script by executing the following command:

```
python collect_candlesticks_data.py BTCUSDT 1d
```
collect_market_caps.py - script is for getting info about Market Capitalization.
Market Cap = Current Price x Circulating Supply.
Open the collect_market_caps.py file.The TEN_SYMBOLS list contains the symbols 
for which you want to retrieve market cap data. Modify this list according to your
requirements.

Run the script by executing the following command:

```
python collect_market_caps.py
```  


# Usage
1. Start the Flask development server:

```
flask run
```

2. Open your web browser and go to http://localhost:5000.

3. Enter the symbol.

4. Click the "Submit" button. The candlestick chart and pie chart will be displayed on the page.






