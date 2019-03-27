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
        except PermissionError:
            return PermissionError
        except FileNotFoundError:
            print("Must load a file first")
            return FileNotFoundError
        except Exception as e:
            print(e)
        finally:
            root.destroy()

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
        except PermissionError:
            return PermissionError
        except FileNotFoundError:
            print("Must load a file first")
            return FileNotFoundError
        except Exception as e:
            print(e)
        finally:
            root.destroy()


