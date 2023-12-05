from src import LinkedList as ll
from src import GradeStock as sg
from src import FileReader as reader
import pickle
# https://twitter.com/chartmojo/status/1549750112628264965


class AnalysisSystemController:
    def __init__(self):
        self.list = ll.LinkedList()  # hold all the stocks
        self.grader = sg.GradeStock()
        self.initialize_stocks()

    def initialize_stocks(self):
        open('current_grades.pkl', 'wb').close()
        read = reader.FileReader('tickers.txt')
        tickers = read.read_file()

        for ticks in tickers:
            grade = self.grader.grade_manager(ticks)
            print(grade)
            with open('current_grades.pkl', 'ab') as file:
                pickle.dump(grade, file)
            pair = ll.Node(grade[0], grade)
            self.list.insert(pair)
        self.list.display()
        self.list.top_graded_patterns()


if __name__ == "__main__":
    controller = AnalysisSystemController()
