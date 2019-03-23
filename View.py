
class View:

    def print_menu(self) -> None:
        print ("\n"
               "Press 1 to load your text file\n"
               "Press 2 to write from plantuml text to python code\n"
               "Press 3 to run the command line interpreter\n"
               "Press 4 to write file to database\n"
               "Press 5 to print  class names from database to screen\n"
               "Press 6 to exit"
               "\n")

    def file_not_loaded_warning(self):
        print("Must load a file first")

    def file_empty_warning(self):
        print("File must be empty")

    def file_type_warning(self):
        print("File must be a .txt file type")

    # def file_not_PEP8_warning(self):
    #     print("File must be converted to PEP8 first")


