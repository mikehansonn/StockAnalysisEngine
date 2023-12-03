import unittest
from src import GradeStock as Grade


class MyTestCase(unittest.TestCase):
    def test_something(self):
        grader = Grade.GradeStock()
        # grader.grade_manager("AAPL")
        # grader.grade_manager("AMZN")
        # grader.grade_manager("TSLA")
        # grader.grade_manager("AMD")
        # grader.grade_manager("NVDA")
        grader.grade_manager("SNAP")
        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
