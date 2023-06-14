import json

import plotly
from flask import Flask, render_template, jsonify, request

from utils import draw_candlestick, SymbolNotFoundException, draw_pie_chart

app = Flask(__name__)


# Route for displaying the candlestick data and pie chart
@app.route('/', methods=['GET', 'POST'])
def display_data():
    if request.method == 'POST':
        # Get the symbol from the form submission
        symbol = request.form.get('symbol')

        # Call the function to draw the candlestick figure based on the symbol
        try:
            candlestick_fig = draw_candlestick(symbol)
        except SymbolNotFoundException:
            error_message = f"Symbol '{symbol}' not found."
            return render_template('form.html', error_message=error_message)

        pie_chart = draw_pie_chart()
        # Convert the figure to JSON for rendering in the template
        graphJSONpie = json.dumps(pie_chart, cls=plotly.utils.PlotlyJSONEncoder)
        graphJSON = json.dumps(candlestick_fig, cls=plotly.utils.PlotlyJSONEncoder)
        return render_template('index.html',graphJSON=graphJSON, graphJSONpie=graphJSONpie, symbol=symbol)

    # Render the initial form
    return render_template('form.html')



if __name__ == '__main__':
    app.run(debug=True)
