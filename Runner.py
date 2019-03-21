from View import View
from FileHandler import FileHandler
from ClassFinder import ClassFinder
from PEP8Converter import PEP8Converter
from CommandLineInterpreter import CommandLineInterpreter


class Controller:

    def __init__(self, class_finder: object, view: object) -> None:
        self.my_class_finder = class_finder
        self.my_view = view
        self.all_my_classes = []
        self.my_command_line_interpreter = CommandLineInterpreter(self)
        self.data = ""
        self.pep8_content = ""

    def start_menu(self) -> None:
        incorrect_input = True
        while incorrect_input:
            self.my_view.print_menu()
            user_input = input("Please enter your input: ")

            # Press 1 to load your text file
            if user_input == "1":
                self.data = FileHandler.read_file()

            # Press 2 to write from plantuml text to python code
            elif user_input == "2":
                self.find_all()
                directory_name = FileHandler.choose_directory()
                self.write_all(directory_name)

            # Press 3 to start command line interpreter
            elif user_input == "3":
                self.command_line_interpreter()

            # Exit
            elif user_input == "5":
                incorrect_input = False
                print("\ngoodbye..\n")

            else:
                input("\nWrong option. Press enter to try again...")

    def find_all(self):
        self.data = self.data.split()
        self.my_class_finder.find_class(self.data)
        self.my_class_finder.relationship_finder(self.data)
        self.all_my_classes = self.my_class_finder.get_all_my_classes()

    def write_all(self, directory_name):
        for a_plant_class in self.all_my_classes:
            content = PEP8Converter.create_class(a_plant_class)
            FileHandler.write_file(directory_name, content, a_plant_class)

    def command_line_interpreter(self):
        self.my_command_line_interpreter.do_greet("user")
        self.my_command_line_interpreter.cmdloop()

    def read_file_from_path(self, path):
        self.data = FileHandler.read_file_from_path(path)

    def write_file_to_path(self, path):
        self.find_all()
        for a_plant_class in self.all_my_classes:
            self.pep8_content = PEP8Converter.create_class(a_plant_class)
            FileHandler.write_file_to_path(path, self.pep8_content, a_plant_class)

    def print_file_to_interpreter(self):
        self.find_all()
        self.pep8_content = PEP8Converter.create_class(a_plant_class)
        print(self.pep8_content)

if __name__ == "__main__":
    view = View()
    class_finder = ClassFinder()
    controller = Controller(class_finder, view)
    controller.start_menu()
