from src import Stock as stock
import os


def create_slope(points):
    slope = 0
    min_val = points[0][1]
    max_val = points[0][1]

    for i in range(len(points) - 1):
        slope = slope + (points[i][1] - points[i + 1][1])/(points[i][0] - points[i + 1][0])
        if points[i + 1][1] < min_val:
            min_val = points[i + 1][1]
        if points[i + 1][1] > max_val:
            max_val = points[i + 1][1]

    return [slope/(len(points) - 1), min_val, max_val]


# next weigh the importance of the different things that are
# checked for and make a final grade for each TDPair that is not just true or false
def compare_data_to_trends(trend, data):
    points = 0
    # check inital trend
    if (trend[1] and data[0][0] > 0) or (not trend[1] and data[0][0] < 0):
        points += 1

    mins = []
    maxs = []

    # check volatility over last 5 intervals
    for j in range(len(data)):
        mins.append([j, data[j][1]])
        maxs.append([j, data[j][2]])

    # check general shape of graph
    min_slope = create_slope(mins)
    max_slope = create_slope(maxs)
    if abs(max_slope[0] - trend[3]) < .1:
        points += 2
    if abs(min_slope[0] - trend[4]) < .1:
        points += 2

    # if the points of the trend is too low, set it to 0
    if points <= 2:
        return 0

    initial = not trend[1]
    for i in range(1, 6, 1):
        if data[i][0] > 0:
            current = True
        else:
            current = False

        if initial != current:
            None
        else:
            initial = not initial
            points += 1

    return points


class GradeStock:
    def __init__(self):
        self.ticker = ""
        self.object = None
        self.trends = []  # 0:name, 1:pre, 2:post, 3:max slope, 4:min slope
        self.read_trends()

    def grade_manager(self, ticker):  # 21 values, split by 0, 1, 2 ,3, 4, 5
        splits = [1, 2, 3, 4, 5]
        self.ticker = ticker
        self.object = stock.Stock(ticker)
        print(self.object.stock_data)
        stock_data = self.object.stock_data["Close"]
        final_results = [0, ticker]  # total score in 0; Trends with score >= 9 are noted (11 is max), along with their
        for trend in self.trends:
            for i in splits:
                index = len(stock_data) - 1
                mean = 0
                points = []
                slopes = []
                for j in range(18):
                    mean += stock_data.iloc[index]
                    points.append([index, stock_data.iloc[index]])
                    index = index - i

                    if (j + 1) % 3 == 0:
                        mean = 0
                        slopes.append(create_slope(points))
                        points = []
                result = compare_data_to_trends(trend, slopes)
                final_results[0] += result

                if result >= 8:
                    final_results.append([trend[0], i, result])
        return final_results

    def read_trends(self):
        # Get the absolute path of the current script
        script_dir = os.path.dirname(os.path.abspath(__file__))

        # Specify the relative path to your text file
        file_path = os.path.join(script_dir, 'patterns.txt')
        
        with open(file_path, 'r') as file:
            for line in file:
                split = line.rstrip().split(',')
                string_value = split[0]  # The first element as a string
                bool_value1 = split[1].lower() == 'true'  # Convert to boolean
                bool_value2 = split[2].lower() == 'true'  # Convert to boolean
                float_value1 = float(split[3])  # Convert to float
                float_value2 = float(split[4])  # Convert to float

                self.trends.append((string_value, bool_value1, bool_value2, float_value1, float_value2))
