import pickle

loaded_data = []

with open('frontpage.pkl', 'rb') as file:
    try:
        while True:
            data = pickle.load(file)
            loaded_data.append(data)
    except EOFError:
        pass


for item in loaded_data:
    print(item)
