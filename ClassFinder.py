from Classmaker import NewClass
import re


class ClassFinder:

    def __init__(self) -> None:
        self.all_my_classes = []

    def find_class(self, file_data: str) -> None:
        list_of_words = file_data.split()

        # Find total amount of words in the list
        total_words = len(list_of_words)

        # for each word in the list
        for i in range(total_words):

            # Check if the before word is class
            if list_of_words[i - 1] == "class":
                a_new_class = list_of_words[i]
                a_new_class = NewClass(a_new_class)
                self.all_my_classes.append(a_new_class)

            # Add relationships

            # Add attributes
            elif ":" == list_of_words[i]:
                if (list_of_words[i - 1].isalpha()) and (list_of_words[i - 1][0].islower())\
                        and list_of_words[i + 1].isalpha():
                    attribute = list_of_words[i - 1] + " " + list_of_words[i] + " " + list_of_words[i + 1]
                    self.all_my_classes[-1].add_attribute(attribute)

            # Add methods
            elif "(" in list_of_words[i]:
                part_of_method = ""
                for j in range(i, total_words):
                    if ")" in list_of_words[i]:
                        part_of_method += list_of_words[i]
                        break
                    elif ")" in list_of_words[j]:
                        part_of_method += (" " + list_of_words[j])
                        if list_of_words[j + 1] == ":":
                            part_of_method += list_of_words[j + 1] + " " + list_of_words[j + 2]
                            break
                    elif "}" in list_of_words[j]:
                        break
                    else:
                        part_of_method += (list_of_words[j])

                if list_of_words[i + 1] == ":":
                    method = part_of_method + list_of_words[i + 1] + " " + list_of_words[i + 2]
                else:
                    method = part_of_method
                self.all_my_classes[-1].add_method(method)

    # def display_my_classes():
        # for aClass in self.all_my_classes:
            # aClass.display_method()
            # aClass.display_attribute()

    def get_all_my_classes(self) -> list:
        print("reach Here")
        return self.all_my_classes

    def relationship_finder(self, file_data):
        print("here")
        list_of_relationships = ["--", "o--"]
        total_relationships = len(list_of_relationships)
        total_words = len(file_data)
        total_classes = len(self.all_my_classes)
        my_relationship = ""
        for i in range(total_words):
            print(type(file_data[i]))
            print(file_data[i])
            if file_data[i] in list_of_relationships:
                print("here1")
                class_one, my_relationship, class_two = file_data[i - 1], file_data[i], file_data[i + 1]
                for j in range(total_classes):
                    print("here2")
                    if self.all_my_classes[j].className == class_one:
                        a_relationship = my_relationship + " " + class_two
                        self.all_my_classes[j].add_relationship(a_relationship)
