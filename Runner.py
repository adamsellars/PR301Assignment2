from View import View
from FileHandler import FileHandler
from ClassFinder import ClassFinder
from PEP8Converter import PEP8Converter


class Controller:

    def __init__(self, ClassFinder: object, view: object) -> None:
        self.myClassFinder = ClassFinder()
        self.view = view

    def start_menu(self) -> None:
        incorrect_input = True
        while incorrect_input:
            View.print_menu()
            user_input = input("Please enter your input: ")

            # Press 1 to load your text file
            if user_input == "1":
                file_data = FileHandler.read_file()

            # Press 2 to write from plantuml text to python code
            elif user_input == "2":
                self.myClassFinder.find_class(file_data)
                self.myClassFinder.relationship_finder(file_data)
                all_my_classes = self.myClassFinder.get_all_my_classes()
                directory_name = FileHandler.choose_directory()
                for aPlantClass in all_my_classes:
                    print(aPlantClass, " ", aPlantClass.relationship)
                    content = PEP8Converter.create_class(aPlantClass)
                    FileHandler.write_file(directory_name, content, aPlantClass)

            # Awaiting option
            elif user_input == "3":
                pass

            # Exit
            elif user_input == "5":
                incorrect_input = False
                print("\ngoodbye..\n")

            else:
                input("\nWrong option. Press enter to try again...")


if __name__ == "__main__":
    controller = Controller(ClassFinder, View)
    controller.start_menu()
