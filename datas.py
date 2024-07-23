import datetime
import pickle

def load_data(file_name):
    try:
        with open(file_name, 'rb') as file:
            return pickle.load(file)
    except (EOFError, FileNotFoundError):
        return []
    

def save_data(file_name, data):
    with open(file_name, 'wb') as file:
        pickle.dump(data, file)