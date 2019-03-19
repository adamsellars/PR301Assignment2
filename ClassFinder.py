from ClassMaker import NewClass
import re


class ClassFinder:

    def __init__(self) -> None:
        self.all_my_classes = []

    def find_class(self, file_data: str) -> None:
        list_of_letters = file_data
        print(list_of_letters)
        # Find total amount of words in the list
        total_letters = len(list_of_letters)

        # for each word in the list
        for i in range(total_letters):

            # Check if the before word is class
            if list_of_letters[i - 1] == "class":
                a_new_class = list_of_letters[i]
                a_new_class = NewClass(a_new_class)
                self.all_my_classes.append(a_new_class)
            # Add attributes
            elif ":" == list_of_letters[i]:
                if ("(" not in list_of_letters[i - 1]) and (list_of_letters[i - 1][0].islower())\
                        and list_of_letters[i + 1].isalpha():
                    attribute = list_of_letters[i - 1] + " " + list_of_letters[i] + " " + list_of_letters[i + 1]
                    print("I am attribute: ", attribute)
                    self.all_my_classes[-1].add_attribute(attribute)

            # Add methods
            elif "(" in list_of_letters[i]:
                part_of_method = ""
                for j in range(i, total_letters):
                    if ")" in list_of_letters[i]:
                        part_of_method += list_of_letters[i]
                        break
                    elif ")" in list_of_letters[j]:
                        part_of_method += (" " + list_of_letters[j])
                        if list_of_letters[j + 1] == ":":
                            part_of_method += list_of_letters[j + 1] + " " + list_of_letters[j + 2]
                            break
                    elif "}" in list_of_letters[j]:
                        break
                    else:
                        part_of_method += " " + (list_of_letters[j])

                if list_of_letters[i + 1] == ":":
                    method = part_of_method + list_of_letters[i + 1] + " " + list_of_letters[i + 2]
                else:
                    method = part_of_method
                self.all_my_classes[-1].add_method(method)

    def get_all_my_classes(self) -> list:
        return self.all_my_classes

    def relationship_finder(self, data):
        file_data = data
        list_of_relationships = ["--", "o--"]
        total_letters = len(file_data)
        total_classes = len(self.all_my_classes)
        for i in range(total_letters):
            if file_data[i] in list_of_relationships:
                class_one, my_relationship, class_two = file_data[i - 1], file_data[i], file_data[i + 1]
                for j in range(total_classes):
                    if self.all_my_classes[j].class_name == class_one:
                        a_relationship = my_relationship + " " + class_two
                        self.all_my_classes[j].add_relationship(a_relationship)
