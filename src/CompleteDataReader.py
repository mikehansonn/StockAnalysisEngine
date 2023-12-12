import pickle


def read_data_file_into_list(filename):
    loaded_data = []

    with open(filename, 'rb') as file:
        try:
            while True:
                data = pickle.load(file)
                loaded_data.append(data)
        except EOFError:
            pass

    return loaded_data
