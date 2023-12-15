from src import GradeStock as sg
import pickle

webpage = ['https://finance.yahoo.com/chart/%5EDJI', 'https://finance.yahoo.com/chart/%5EGSPC', 'https://finance.yahoo.com/chart/%5EIXIC']
real_names = ['Dow Jones', 'S&P 500', 'Nasdaq']
symbols = ['^DJI', '^GSPC', '^IXIC']
grader = sg.GradeStock()
open('frontpage.pkl', 'wb').close()

for i in range(len(symbols)):
    grade = grader.grade_manager(symbols[i])
    grade[1] = real_names[i]
    grade[5] = webpage[i]
    with open('frontpage.pkl', 'ab') as file:
        pickle.dump(grade, file)
    print(grade)

