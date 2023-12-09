from flask import Flask, render_template
from src import AnalysisSystemController as asc  # this works for the time being, dont have use for it yet

app = Flask(__name__)


def get_data():
    return [['AAPL', '95', '224.23', 1.41, [10, 0, 0, 0, 8]]
        , ['TSLA', '90', '113.65', -2.24, [0, 9, 0, 0, 9]]
        , ['S&P500', '85', '4435.41', 0.12, [10, 8, 0, 9, 0]]
        , ['CSCO', '80', '60.31', -1.22, [0, 0, 0, 0, 0]]
        , ['T', '76', '10.31', 0.00, [8, 10, 10, 9, 10]]
        , ['AAPL', '95', '224.23', 1.41, [10, 0, 0, 0, 8]]
        , ['TSLA', '90', '113.65', -2.24, [0, 9, 0, 0, 9]]
        , ['S&P500', '85', '4435.41', 0.12, [10, 8, 0, 9, 0]]
        , ['CSCO', '80', '60.31', -1.22, [0, 0, 0, 0, 0]]
        , ['T', '76', '10.31', 0.00, [8, 10, 10, 9, 10]]]


@app.route('/')
def index():
    getdata = get_data()
    return render_template('home.html', data=getdata)


@app.route('/top-picks')
def top_picks():
    # get the top 10 picks
    # along with a drop down of every stock with a 10 grade
    date = '12-08-2023'
    return render_template('top-picks.html', data=get_data(), date=date)


@app.route('/search')
def search():
    # allow the user to search for specific stock to see my grade
    return render_template('search.html')


if __name__ == '__main__':
    app.run(debug=True)
