from cmd import Cmd


class CommandLineInterpreter(Cmd):
    # Created by Adam
    def __init__(self, controller):
        Cmd.__init__(self)
        self.prompt = ">>> "
        self.my_controller = controller
        self.banner = "=====" * 10

    # Created by Adam
    def do_load_file(self, path):
        self.my_controller.read_file_from_path(path)

    # Created by Adam
    def do_write_file(self, path):
        self.my_controller.write_file_to_path(path)

    # Created by Adam
    def help_load_file(self):
        print(
            self.banner +
            "\nload_file command help\n" +
            self.banner +
            "\nDescription: Load a .txt file into the program\n"
            "Syntax: load_file [path]\n"
            "Parameter: [path] = full path name of the file starting from the root directory of this program\n"
            "Example: load_file test4(myowncode).txt\n"
        )

    # Created by Adam
    def help_quit(self):
        print(
            self.banner +
            "\nquit command help\n" +
            self.banner +
            "\nDescription: terminate the command line interpreter\n"
            "Syntax: quit\n"
            "Parameter: none\n"
            "Example: quit\n"
        )

    # Created by Adam
    def help_greet(self):
        print(
            self.banner +
            "\ngreet command help\n" +
            self.banner +
            "\nDescription: A Greeting message\n"
            "Syntax: greet\n"
            "Parameter: none\n"
            "Example: greet\n"
        )

    # Created by Adam
    def do_greet(self, line):
        print(self.banner + "\nWelcome to the command line interpreter."
                            "\nType help to view available commands\n" + self.banner + "\n")

    # print file to the command line interpreter?
    # not sure if you want to do this or just write files
    def do_print_file(self):
        self.my_controller.print_file_to_interpreter()



    #
    def help_print_file(self):
        pass

    #
    def help_write_file(self):
        pass

    # Created by Adam
    def do_quit(self, line):
        print("Goodbye thank you for using the command line interpreter")
        return True
