import pickle
from tkinter import *
from tkinter import filedialog


class Pickler:

    # Leroi wrote this
    @staticmethod
    def pickle_file(file_data):
        root = Tk()
        try:
            with open("data.pickle", "wb") as file:
                pickle.dump(file_data, file)
                root.destroy()
        except FileNotFoundError:
            root.destroy()
            print("Must load a file first")

    # Adam wrote this
    @staticmethod
    def unpickle_file():
        root = Tk()
        try:
            name_of_file = filedialog.askopenfilename(filetypes=(("All files", "*.pickle*"), ("All files", "*.pickle*")))
            with open(name_of_file, "rb") as file:
                file_data = pickle.load(file)
                print(file_data)
                root.destroy()
        except FileNotFoundError:
            root.destroy()
            print("Must load a file first")



