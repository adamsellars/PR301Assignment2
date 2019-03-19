from Classmaker import NewClass


file = open("test4(myowncode).txt")
stuff = file.read()
filedata = stuff.split()
relationships = ["--", "o--"]
ClassFinder = NewClass("ClassFinder")
Controller = NewClass("Controller")
Poop = NewClass("Poop")
classlist = [ClassFinder, Controller, Poop]


def relationship_finder(classlist):
    listOfRelationships = []
    total_relationships = len(relationships)
    total_words = len(filedata)
    total_classes = len(classlist)
    my_relationship = ""
    for i in range(total_words):
        if filedata[i] in relationships:
            class_one, my_relationship, class_two = filedata[i - 1], filedata[i], filedata[i + 1]
            for j in range(total_classes):
                if classlist[j].className == class_one:
                    a_relationship = my_relationship + " " + class_two
                    classlist[j].relationship.append(a_relationship)


# def set_relationships(relationshiplist):
    #total_classes = len(classlist)
    #a_relationship = relationshiplist
    # for i in range(total_classes):
        # if classlist[i] in relationshiplist:



