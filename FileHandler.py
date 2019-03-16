from tkinter import *
from tkinter import filedialog
from PEP8Converter import PEP8Converter


class FileHandler:

    @staticmethod
    def readFile():
        root = Tk()
        nameOfFile = filedialog.askopenfilename(filetypes=(("All files", "*.*"), ("All files", "*.*")))
        if nameOfFile is None:
            return
        file = open(nameOfFile)
        file_data = file.read()
        file.close
        root.destroy()
        return file_data

    def writeFile(aPlantClass):
        fileName = aPlantClass.className
        f = open("{}.py".format(fileName), "w+")
        content = PEP8Converter.createClass(aPlantClass)
        f.write(content)
        f.close()
