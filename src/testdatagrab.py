import pickle

loaded_data = []

with open('current_grades.pkl', 'rb') as file:
    try:
        while True:
            data = pickle.load(file)
            print(data)
            loaded_data.append(data)
    except EOFError:
        pass

print(loaded_data)
