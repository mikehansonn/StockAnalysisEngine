import pickle

data = {'key': 'value'}
data2 = [['KNYB', 92], ['BTRS', 58]]
data3 = [['AAPL', 31], ['GOOG', 12]]

# Overwrite and add data to file
with open('data.pkl', 'wb') as file:
    pickle.dump(data, file)

#append to file
with open('data.pkl', 'ab') as file:
    pickle.dump(data3, file)
    pickle.dump(data2, file)

loaded_data = []

# Read all data from the file
with open('data.pkl', 'rb') as file:
    try:
        while True:
            data = pickle.load(file)
            print(data)
            loaded_data.append(data)
    except EOFError:
        pass

print(loaded_data)
