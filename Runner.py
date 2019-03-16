from View import View
from FileHandler import FileHandler
from ClassFinder import ClassFinder
from PEP8Converter import PEP8Converter


class Controller:

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def start_menu(self):
        incorrectInput = True
        while (incorrectInput):
            View.print_menu()
            userInput = input("Please enter your input: ")

            # Press 1 to load your text file
            if (userInput == "1"):
                file_data = FileHandler.read_file()

            # Press 2 to write from plantuml text to python code
            elif (userInput == "2"):
                ClassFinder.find_class(file_data)
                allMyClasses = ClassFinder.get_all_my_class()
                for aPlantClass in allMyClasses:
                    content = PEP8Converter.create_class(aPlantClass)
                    FileHandler.write_file(content, aPlantClass)

            # Awaiting option
            elif (userInput == "3"):
                pass

            # Exit
            elif (userInput == "5"):
                incorrectInput = False
                print("\ngoodbye..\n")

            else:
                input("\nWrong option. Press enter to try again...")


if __name__ == "__main__":
    controller = Controller(ClassFinder, View)
    controller.start_menu()

