import os
from tkinter import *
from tkinter import filedialog


class FileHandler:
    
    @staticmethod
    def read_file() -> str:
        root = Tk()
        try:
            name_of_file = filedialog.askopenfilename(filetypes=(("All files", "*.*"), ("All files", "*.*")))
            with open(name_of_file) as file:
                file_data = file.read()
                root.destroy()
                print("\nfile loaded...\n")
                return file_data
        except FileNotFoundError:
            root.destroy()
            print("Error, no file inserted")

    @staticmethod
    def choose_directory() -> str:
        root = Tk()
        try:
            dir_name = filedialog.askdirectory()
            root.destroy()
            return dir_name
        except FileNotFoundError:
            root.destroy()

    @staticmethod
    def write_file(directory_name: str, content: str, a_plant_class: str) -> None:
        root = Tk()
        file_name = a_plant_class.class_name
        try:
            with open(directory_name + "/{}.py".format(file_name), "w+") as f:
                f.write(content)
                f.close()
                root.destroy()

        except FileNotFoundError:
            root.destroy()
            print("Error, no file inserted")
