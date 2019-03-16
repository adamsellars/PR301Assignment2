
class View:
    @staticmethod
    def printMenu():
        print ("\n"
               "Press 1 to load your text file\n"
               "Press 2 to generate python class\n"
               "Press 3 to write from text to python code\n"
               "Press 4 to generate python attribute\n"
               "Press 5 to exit"
               "\n")

    def printFileData(data):
        print(data)

    def printClassData(classes):
        classCounter = 1
        for aClass in classes:
            print("Class {}: ".format(classCounter) + aClass)
            classCounter += 1

    def printMethodData(methods):
        methodCounter = 1
        for aMethod in methods:
            print("\nMethod {}: ".format(methodCounter) + aMethod)
            methodCounter += 1

    def printAttributeData(attributes):
        attributeCounter = 1
        for attribute in attributes:
            print("\nAttribute {}: ".format(attributeCounter) + attribute)
            attributeCounter += 1

