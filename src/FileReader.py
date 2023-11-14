# read file data, and return an array of tickers

class FileReader:
    def __init__(self, filename):
        self.filename = filename

    def read_file(self):
        tickers = []
        with open(self.filename, 'r') as file:
            for line in file:
                tickers.append(line.rstrip())

        return tickers
