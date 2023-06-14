import plotly.graph_objs as go
import pandas as pd


class SymbolNotFoundException(Exception):
    pass

def draw_candlestick(symbol):
    df = pd.read_csv('static/candlestick_info.csv')
    df = df.loc[df['Symbol'] == symbol]
    if df.empty:
        raise SymbolNotFoundException
    candlestick_trace = go.Candlestick(
        x=df['Timestamp'],
        open=df['Open'],
        high=df['High'],
        low=df['Low'],
        close=df['Close']
    )
    candlestick_layout = go.Layout(
        title='Candlestick Chart',
        xaxis=dict(title='Date'),
        yaxis=dict(title='Price')
    )

    candlestick_fig = go.Figure(data=[candlestick_trace], layout=candlestick_layout)
    return candlestick_fig.to_dict()


def draw_pie_chart():
    df = pd.read_csv('static/market_cap_ten_symbols.csv')
    df["market_cap"] = df["Close Price"] * df["Circulating supply"]
    pie_chart = go.Figure(data=[go.Pie(labels=df['Symbol'], values=df['market_cap'])])
    return pie_chart.to_dict()

