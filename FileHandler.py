import os
from tkinter import *
from tkinter import filedialog


class FileHandler:

    def read_file() -> str:
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

    def choose_directory() -> str:
        root = Tk()
        try:
            dir_name = filedialog.askdirectory()
            root.destroy()
            return dir_name
        except FileNotFoundError:
            root.destroy()

    def write_file(directoryName: str, content: str, aPlantClass: str) -> None:
        root = Tk()
        fileName = aPlantClass.className
        try:
            with open(directoryName + "/{}.py".format(fileName), "w+") as f:
                f.write(content)
                f.close()
                root.destroy()

        except FileNotFoundError:
            root.destroy()
            print("Error, no file inserted")
