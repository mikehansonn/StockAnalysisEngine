from flask import Flask, render_template, jsonify, request
from src import AnalysisSystemController as asc, CompleteDataReader  # this works for the time being, dont have use for it yet

app = Flask(__name__)


# 0 : grade, 1 : symbol, 2 : close, 3 : day change, 4 : % change, 5 : time intervals
def get_data():
    return CompleteDataReader.read_data_file_into_list(
        r'C:\Individual_Projects\StockAnalysisProject\src\top_grades.pkl')


def double_data():
    return CompleteDataReader.read_data_file_into_list(
        r'C:\Individual_Projects\StockAnalysisProject\src\risk_grades.pkl')


def get_home_data():
    return [['Dow Jones', 36247.87, 0.36, 'https://finance.yahoo.com/chart/%5EDJI']
            , ['S&P 500', 4604.37, 0.41, 'https://finance.yahoo.com/chart/%5EGSPC']
            , ['Nasdaq', 14403.97, -0.45, 'https://finance.yahoo.com/chart/%5EIXIC']]


@app.route('/')
def index():
    return render_template('home.html', data=get_home_data())


@app.route('/top-picks')
def top_picks():
    # get the top 10 picks
    # along with a drop down of every stock with a 10 grade
    date = '12-08-2023'
    return render_template('top-picks.html', data=get_data(), date=date, risk=double_data())


@app.route('/search')
def search():
    # allow the user to search for specific stock to see my grade
    return render_template('search.html')


def read_tickers():
    symbols = []

    with open(r'C:\Individual_Projects\StockAnalysisProject\src\tickers.txt', 'r') as file:
        for line in file:
            symbols.append(line.rstrip())

    return symbols


@app.route('/autocomplete', methods=['GET'])
def autocomplete():
    symbols = read_tickers()
    term = request.args.get('term')
    results = [s for s in symbols if term.lower() in s.lower()]
    return jsonify(results)


if __name__ == '__main__':
    app.run(debug=True)
