
class View:

    def print_menu(self) -> None:
        print ("\n"
               "------------------------------------------------------\n"
               "Press 1 to load your text file   \n"
               "------------------------------------------------------\n"
               "Press 2 to write from plantuml text to python code  \n"
               "------------------------------------------------------\n"
               "Press 3 to run the command line interpreter         \n"
               "------------------------------------------------------\n"
               "Press 4 to write file to database                   \n"
               "------------------------------------------------------\n"
               "Press 5 to print class names from database to screen\n"
               "------------------------------------------------------\n"
               "Press 6 to load text file, convert data to PEP8 python\n "
               "\t\tformat then convert file to pickle format in\n"
               "\t\tsame directory \n"
               "------------------------------------------------------\n"
               "Press 7 to load data from pickle file\n"
               "------------------------------------------------------\n"
               "Press 8 to exit  \n"
               "------------------------------------------------------\n"
               "\n")

    def file_not_loaded_warning(self):
        print("Must load a file first")

    def file_empty_warning(self):
        print("File must not be empty")

    def file_type_warning(self):
        print("File must be a .txt file type")

    def exit_file_directory(self):
        print("Exiting file directory dialogue...")
