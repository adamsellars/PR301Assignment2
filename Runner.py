from View import View
from FileHandler import FileHandler
from ClassFinder import ClassFinder
from PEP8Converter import PEP8Converter
from CommandLineInterpreter import CommandLineInterpreter
from sys import argv
from Database import SQL


class Controller:

    def __init__(self, class_finder: object, view: object) -> None:
        self.my_class_finder = class_finder
        self.my_view = view
        self.all_my_classes = []
        self.my_command_line_interpreter = CommandLineInterpreter(self)
        self.data = str
        self.pep8_content = str

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
                if self.data is not None:
                    self.find_all()
                    directory_name = FileHandler.choose_directory()
                    self.write_all(directory_name)
                else:
                    self.my_view.file_not_loaded_warning()

            # Press 3 to start command line interpreter
            elif user_input == "3":
                self.command_line_interpreter()

            # Press 4 to write file to data base
            elif user_input == "4":
                classes = []
                SQL.connect_to_db("assignment1")
                SQL.c.execute("""DROP TABLE class;""")
                SQL.create_class_table()
                if self.data is not None:
                    classes = self.get_class_names()
                    SQL.insert_data_into_table(classes)
                else:
                    self.my_view.file_not_loaded_warning()

            # Press 5 to print PEP8 class file to screen from database
            elif user_input == "5":
                if self.data is not None:
                    SQL.fetch_all_class_data()
                else:
                    self.my_view.file_not_loaded_warning()

            # Exit
            elif user_input == "6":
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
        pep8 = ""
        for a_plant_class in self.all_my_classes:
            pep8 += PEP8Converter.create_class(a_plant_class) + "\n"
        return pep8

    def prep_pep8(self):
        self.find_all()
        pep8 = ""
        for a_plant_class in self.all_my_classes:
            pep8 += PEP8Converter.create_class(a_plant_class) + "\n"
        self.pep8_content = pep8

    def get_class_names(self):

        class_list = []
        counter = 1
        total_classes = len(self.all_my_classes)
        for aClass in self.all_my_classes:
            database_format = []
            class_name = aClass.class_name
            database_format.append("{}".format(counter))
            database_format.append(class_name)
            counter += 1
            class_list.append(database_format)
        print(class_list)
        return class_list


Leroi wrote this
def start_cmd():
    if __name__ == "__main__":
        view = View()
        class_finder = ClassFinder()
        controller = Controller(class_finder, view)
        controller.command_line_interpreter()


Adam wrote this
def correct_num_of_arguments(num_of_args):
    if num_of_args == 2:
        return True
    else:
        return False


if __name__ == "__main__":
    len(argv)
    view = View()
    class_finder = ClassFinder()
    controller = Controller(class_finder, view)
    controller.start_menu()
