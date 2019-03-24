import pickle
from tkinter import *
from tkinter import filedialog


class Pickler:

    @staticmethod
    def pickle_file(file_data):
        with open("data.pickle", "wb") as file:
            pickle.dump(file_data, file)

    @staticmethod
    def unpickle_file():
        root = Tk()
        name_of_file = filedialog.askopenfilename(filetypes=(("All files", "*.pickle*"), ("All files", "*.pickle*")))
        with open(name_of_file, "rb") as file:
            file_data = pickle.load(file)
        print(file_data)
        root.destroy()



