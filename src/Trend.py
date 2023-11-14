# hold all of the data for a trend

class Trend:
    def __init__(self, name, pre, post, max_slope, min_slope):
        self.name = name
        self.pre = pre
        self.post = post
        self.max_slope = max_slope
        self.min_slope = min_slope
