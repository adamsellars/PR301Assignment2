from tkinter import *
from tkinter import filedialog
from PEP8Converter import PEP8Converter


class FileHandler:

    def read_file():
        root = Tk()
        try:
            nameOfFile = filedialog.askopenfilename(filetypes=(("All files", "*.*"), ("All files", "*.*")))
            with open(nameOfFile) as file:
                file_data = file.read()
                root.destroy()
                print("\nfile loaded...\n")
                return file_data
        except FileNotFoundError:
            root.destroy()
            print("Error, no file inserted")

    def write_file(content, aPlantClass):
        fileName = aPlantClass.className
        with open("{}.py".format(fileName), "w+") as f:
            f.write(content)
            f.close()
