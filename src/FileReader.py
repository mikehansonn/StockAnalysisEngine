import os
# read file data, and return an array of tickers

class FileReader:
    def __init__(self, filename):
        self.filename = filename

    def read_file(self):
        tickers = []
        # Get the absolute path of the current script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        # Specify the relative path to your text file
        file_path = os.path.join(script_dir, self.filename)
        with open(file_path, 'r') as file:
            for line in file:
                tickers.append(line.rstrip())

        return tickers
