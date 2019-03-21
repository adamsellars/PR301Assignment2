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

    # Created by Adam
    # Different way to read data from file requires user to enter complete file path
    @staticmethod
    def read_file_from_path(path) -> str:
        try:
            with open(path) as file:
                data = file.read()
                print("\nfile loaded...\n")
                return data
        except FileNotFoundError:
            print("Error, file does not exist!")
        except PermissionError:
            print("Error, you do not have permission to access this file!")

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

    @staticmethod
    def write_file_to_path(path: str, content: str) -> None:
        try:
            with open(path + ".py", "w+") as file:
                file.write(content)
        except FileNotFoundError:
            print("Error, no file inserted")
