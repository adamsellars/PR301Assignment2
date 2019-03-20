from View import View
from FileHandler import FileHandler
from ClassFinder import ClassFinder
from PEP8Converter import PEP8Converter


class Controller:

    def __init__(self, class_finder: object, view: object) -> None:
        self.my_class_finder = class_finder
        self.my_view = view
        self.all_my_classes = []

    def start_menu(self) -> None:
        incorrect_input = True
        while incorrect_input:
            self.my_view.print_menu()
            user_input = input("Please enter your input: ")

            # Press 1 to load your text file
            if user_input == "1":
                data = FileHandler.read_file()
                file_data = data.split()

            # Press 2 to write from plantuml text to python code
            elif user_input == "2":
                file = open("test4(myowncode).txt")
                stuff = file.read()
                file_data = stuff.split()
                self.my_class_finder.find_class(file_data)
                self.my_class_finder.relationship_finder(file_data)
                self.all_my_classes = self.my_class_finder.get_all_my_classes()
                # directory_name = FileHandler.choose_directory()
                for a_plant_class in self.all_my_classes:
                    content = PEP8Converter.create_class(a_plant_class)
                    # print(a_plant_class, " - ", a_plant_class.relationship)
                    print(content)
                    # FileHandler.write_file(directory_name, content, a_plant_class)

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
    view = View()
    class_finder = ClassFinder()
    controller = Controller(class_finder, view)
    controller.start_menu()
