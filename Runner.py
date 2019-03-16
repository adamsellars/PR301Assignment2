from View import View
from FileHandler import FileHandler
from ClassFinder import ClassFinder
from PEP8Converter import PEP8Converter


class Controller:

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def startMenu(self):
        incorrectInput = True
        while (incorrectInput):
            View.printMenu()
            userInput = input("Please enter your input: ")

            if (userInput == "1"):
                file_data = FileHandler.readFile()
                print("\n>\nFile Loaded\n>\n")

            elif (userInput == "2"):
                ClassFinder.findClass(file_data)
                ClassFinder.displayMyClasses()

            elif (userInput == "3"):
                allMyClasses = ClassFinder.getAllMyClass()
                for aPlantClass in allMyClasses:
                    FileHandler.writeFile(aPlantClass)

            elif (userInput == "4"):
                pass

            else:
                input("\nWrong option. Press enter to try again...")


if __name__ == "__main__":
    controller = Controller(ClassFinder, View)
    controller.startMenu()

