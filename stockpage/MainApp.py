from flask import Flask, render_template
from src import AnalysisSystemController as asc # this works for the time being, dont have use for it yet

app = Flask(__name__)

def get_data():
    return [['AAPL', '95', '224.23', '+1.41']
            , ['TSLA', '90', '113.65', '+2.24']
            , ['S&P500', '85', '4435.41','-0.12']
            , ['CSCO', '80', '60.31', '+1.22']
            , ['T', '76', '10.31', '-1.25']]

@app.route('/')
def index():
    getdata = get_data()
    return render_template('home.html', data=getdata)

if __name__ == '__main__':
    app.run(debug=True)
