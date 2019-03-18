from View import View
from FileHandler import FileHandler
from ClassFinder import ClassFinder
from PEP8Converter import PEP8Converter


class Controller:

    def __init__(self, ClassFinder: object, view: object) -> None:
        self.myClassFinder = ClassFinder()
        self.view = view

    def start_menu(self) -> None:
        incorrectInput = True
        while (incorrectInput):
            View.print_menu()
            userInput = input("Please enter your input: ")

            # Press 1 to load your text file
            if (userInput == "1"):
                file_data = FileHandler.read_file()

            # Press 2 to write from plantuml text to python code
            elif (userInput == "2"):
                content = ""
                self.myClassFinder.find_class(file_data)
                allMyClasses = self.myClassFinder.get_all_my_classes()
                directoryName = FileHandler.choose_directory()
                print(directoryName)
                for aPlantClass in allMyClasses:
                    content += PEP8Converter.create_class(aPlantClass)
                    FileHandler.write_file(directoryName, content, aPlantClass)

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

