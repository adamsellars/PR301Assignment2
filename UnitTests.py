import unittest
from FileHandler import FileHandler
from ClassFinder import ClassFinder

'''
class FileHandlerTests(unittest.TestCase):
    # FileHandler tests
    # read_file_from_path
    def setUp(self):
        # be executed before each test
        self.test = FileHandler()

    def tearDown(self):
        # be executed after each test case
        print('down')

    # test case 1 read_file_from_path returns a String from a valid file path
    def test_01(self):
        print(1)
        result = self.test.read_file_from_path("valid.txt")
        self.assertTrue(isinstance(result, str), "When given a valid file path a string should be returned")

    # test case 2 read_file_from_path exception handling prevents file not found error from invalid file path
    def test_02(self):
        print(2)
        try:
            self.test.read_file_from_path("doesnt_exist.txt")
        except FileNotFoundError:
            self.fail("Exception handling failed to handle file not found error")

    # test case 3 read_file_from_path prevents a permission exception from an file with no read permission
    def test_03(self):
        print(3)
        try:
            self.test.read_file_from_path("no_permission.txt")
        except PermissionError:
            self.fail("Exception handling failed to handle permission error")
'''
    #################################################################################################


class ClassFinderTests(unittest.TestCase):
    def setUp(self):
        # be executed before each test
        with open("test4.txt") as file:
            self.test_data = file.read()
            self.test = ClassFinder()

    # check that classes have been added
    def test_04(self):
        print("4")
        self.test.find_class(self.test_data)
        self.assertGreater(self.test.all_my_classes.__len__(), 0)
'''
    # check that the correct number of classes are added
    def test_05(self):
        print("5")
        self.test.find_class(self.test_data)
        self.assertEqual(self.test.all_my_classes.__len__(), 6)

    # check that the first added class has the correct class name
    def test_06(self):
        print(6)
        self.test.find_class(self.test_data)
        first_class = self.test.all_my_classes[0].class_name
        self.assertEqual(first_class, "Controller")

    # check that the last added class has the correct class name
    def test_07(self):
        print(6)
        self.test.find_class(self.test_data)
        last_class = self.test.all_my_classes[-1].class_name
        self.assertEqual(last_class, "FileHandler")

    # check that the first classes attributes are correctly added
    def test_08(self):
        print(7)
        self.test.find_class(self.test_data)
        first_class_attributes = self.test.all_my_classes[0].attribute
        self.assertEqual(first_class_attributes, ["myClassFinder : ClassFinder", "view : View"])

    # check that the last classes attributes are correctly added
    def test_09(self):
        print(7)
        self.test.find_class(self.test_data)
        last_class_attributes = self.test.all_my_classes[-1].attribute
        self.assertEqual(last_class_attributes, [])

    # check that the first classes methods are correctly added
    def test_10(self):
        print(7)
        self.test.find_class(self.test_data)
        first_class_methods = self.test.all_my_classes[0].method
        self.assertEqual(first_class_methods, ["__init__(self,model:Object,view: Object): None",
                                               "start_menu(): None"])

    # check that the last classes methods are correctly added
    def test_11(self):
        print(7)
        self.test.find_class(self.test_data)
        first_class_methods = self.test.all_my_classes[-1].method
        self.assertEqual(first_class_methods, ["read_file(): String", "write_file(): None"])
    # check that a classes relationship is correctly added
'''

if __name__ == '__main__':
    # unittest.main(verbosity=2)  # with more details
    unittest.main()
