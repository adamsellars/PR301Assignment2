import unittest
from FileHandler import FileHandler
from ClassFinder import ClassFinder
from ClassMaker import NewClass


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
        result = self.test.read_file_from_path("valid.txt")
        self.assertTrue(isinstance(result, str), "When given a valid file path a string should be returned")

    # test case 2 read_file_from_path exception handling prevents file not found error from invalid file path
    def test_02(self):
        try:
            self.test.read_file_from_path("doesnt_exist.txt")
        except FileNotFoundError:
            self.fail("Exception handling failed to handle file not found error")

    # test case 3 read_file_from_path prevents a permission exception from an file with no read permission
    def test_03(self):
        try:
            self.test.read_file_from_path("no_permission.txt")
        except PermissionError:
            self.fail("Exception handling failed to handle permission error")

class ClassMakerTests(unittest.TestCase):
    def setUp(self):
        # be executed before each test
        self.test = NewClass("test_class")

    # Test __str__ method
    def test_04(self):
        result = self.test.__str__()
        self.assertEqual(result, "test_class")

    # Test add_method
    def test_05(self):
        self.test.add_method("do_stuff()")
        method = self.test.method[-1]
        self.assertEqual(method, "do_stuff()")

    # Test that multiple methods can be added
    def test_06(self):
        count = 0
        while count <= 100:
            self.test.add_method("do_stuff_" + str(count) + "()")
            count += 1
        self.assertEqual(self.test.method[0], "do_stuff_0()")
        self.assertEqual(self.test.method[-1], "do_stuff_100()")

    # Test add_attribute
    def test_07(self):
        self.test.add_attribute("attribute1 : String")
        result = self.test.attribute[-1]
        self.assertEqual(result, "attribute1 : String")

    # Test that multiple methods can be added
    def test_08(self):
        count = 0
        while count <= 100:
            self.test.add_attribute("attribute" + str(count))
            count += 1
        self.assertEqual(self.test.attribute[0], "attribute0")
        self.assertEqual(self.test.attribute[-1], "attribute100")

    # Test add_relationship
    def test_09(self):
        self.test.add_relationship("class1 *-- class2")
        result = self.test.relationship[-1]
        self.assertEqual(result, "class1 *-- class2")

    # Test that multiple and different types of relationships can be added
    def test_10(self):
        self.test.add_relationship("class1 *-- class2")
        self.test.add_relationship("class1 o-- class3")
        self.test.add_relationship("class1 *-- class4")
        self.assertEqual(self.test.relationship[0], "class1 *-- class2")
        self.assertEqual(self.test.relationship[1], "class1 o-- class3")
        self.assertEqual(self.test.relationship[2], "class1 *-- class4")





class ClassFinderTests(unittest.TestCase):
    def setUp(self):
        # be executed before each test
        with open("test4(myowncode).txt") as file:
            self.test_data = file.read().split()
            # print(self.test_data)
            self.test = ClassFinder()

    # check that classes have been added
    def test_11(self):
        self.test.find_class(self.test_data)
        self.assertGreater(self.test.my_classes.__len__(), 0, "my_classes List should not be empty")

    # check that the correct number of classes are added
    def test_12(self):
        self.test.find_class(self.test_data)
        self.assertEqual(self.test.my_classes.__len__(), 6)

    # check that the first added class has the correct class name
    def test_13(self):
        self.test.find_class(self.test_data)
        first_class = self.test.my_classes[0].class_name
        self.assertEqual(first_class, "Controller")

    # check that the last added class has the correct class name
    def test_14(self):
        self.test.find_class(self.test_data)
        last_class = self.test.my_classes[-1].class_name
        self.assertEqual(last_class, "FileHandler")

    # check that the first classes attributes are correctly added
    def test_15(self):
        self.test.find_class(self.test_data)
        first_class_attributes = self.test.my_classes[0].attribute
        self.assertEqual(first_class_attributes, ["my_class_finder : ClassFinder", "my_view : View",
                                                  "all_my_classes : List"])

    # check that the last classes attributes are correctly added
    def test_16(self):
        self.test.find_class(self.test_data)
        last_class_attributes = self.test.my_classes[-1].attribute
        self.assertEqual(last_class_attributes, [])

    # check that the first classes methods are correctly added
    def test_17(self):
        self.test.find_class(self.test_data)
        first_class_methods = self.test.my_classes[0].method
        self.assertEqual(first_class_methods, [" __init__(self, class_finder: Object, view: Object): None",
                                               "start_menu(self): None"])

    # check that the last classes methods are correctly added
    def test_18(self):
        self.test.find_class(self.test_data)
        last_class_methods = self.test.my_classes[-1].method
        self.assertEqual(last_class_methods, ["read_file(): String", "write_file(): None"])

    # check that a classes relationship is correctly added
    def test_19(self):
        self.test.find_class(self.test_data)
        self.test.relationship_finder(self.test_data)
        class_relationship = self.test.my_classes[0].relationship
        self.assertEqual(class_relationship, ["o-- ClassFinder", "-- FileHandler", "-- PEP8Converter", "o-- View"])


if __name__ == '__main__':
    unittest.main(verbosity=2)  # with more details
    # unittest.main()