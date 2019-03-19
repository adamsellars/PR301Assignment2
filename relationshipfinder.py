from Classmaker import NewClass


file = open("test4(myowncode).txt")
stuff = file.read()
file_data = stuff.split()
relationships = ["--", "o--"]
ClassFinder = NewClass("ClassFinder")
Controller = NewClass("Controller")
Poop = NewClass("Poop")
my_class_list = [ClassFinder, Controller, Poop]


def relationship_finder(my_class_list):
    total_words = len(file_data)
    total_classes = len(my_class_list)
    for i in range(total_words):
        if file_data[i] in relationships:
            class_one, my_relationship, class_two = file_data[i - 1], file_data[i], file_data[i + 1]
            for j in range(total_classes):
                if my_class_list[j].className == class_one:
                    a_relationship = my_relationship + " " + class_two
                    my_class_list[j].add_relationship(a_relationship)
                print(my_class_list[j].relationship)

# def set_relationships(relationshiplist):
    #total_classes = len(my_class_list)
    #a_relationship = relationshiplist
    # for i in range(total_classes):
        # if my_class_list[i] in relationshiplist:



