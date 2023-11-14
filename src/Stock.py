import yfinance as yf
from datetime import datetime, timedelta
# Holds one stock
# Hold the data for the stock over the last day


class Stock:
    def __init__(self, ticker):
        self.ticker = ticker
        self.grade = 0
        self.pattern_index = 0  # most likely pattern

        self.stock_data = None
        self.generate_stock_data()

    def set_grade(self, grade):
        self.grade = grade

    def set_pattern_index(self, index):
        self.pattern_index = index

    def generate_stock_data(self):
        end_date = datetime.now()- timedelta(days=7)
        start_date = end_date - timedelta(days=14)

        self.stock_data = yf.download(self.ticker, start=start_date, end=end_date, interval="15m")  # 130 current reads

    def compare_to(self, comp):
        if self.grade >= comp:
            return self
        else:
            return comp

    def to_string(self):
        string = self.ticker + "\n"
        string = string + "Grade: " + str(self.grade)
        # add most recent price, and maybe time?

        return string
