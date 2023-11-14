import LinkedList as ll
import GradeStock as sg
import FileReader as reader
# https://twitter.com/chartmojo/status/1549750112628264965


class AnalysisSystemController:
    def __init__(self):
        self.list = ll.LinkedList()  # hold all the stocks
        self.grader = sg.GradeStock()
        self.initialize_stocks()

    def initialize_stocks(self):
        read = reader.FileReader("small_tickers.txt")
        tickers = read.read_file()

        for ticks in tickers:
            grade = self.grader.grade_manager(ticks)
            print(grade)
            pair = ll.Node(grade[0], grade)
            self.list.insert(pair)
        self.list.display()
        self.list.top_graded_patterns()


if __name__ == "__main__":
    controller = AnalysisSystemController()
