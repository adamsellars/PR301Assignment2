
class View:

    def print_menu(self) -> None:
        print ("\n"
               "Press 1 to load your text file\n"
               "Press 2 to write from plantuml text to python code\n"
               "Press 3 to run the command line interpreter\n"
               "Press 5 to exit"
               "\n")

    def file_not_loaded_warning(self):
        print("Must load a file first")

    def file_empty_warning(self):
        print("File must be empty")

    def file_type_warning(self):
        print("File must be a .txt file type")


