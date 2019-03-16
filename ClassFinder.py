from Classmaker import NewClass
import re


class ClassFinder:
    classList = []

    def find_class(file_data):
        listOfCapitalWords = []
        listOfWords = file_data.split()

        # Find total amount of words in the list
        totalWords = len(listOfWords)

        # for each word in the list
        for i in range(totalWords):

            # Check if the before word is class
            if listOfWords[i - 1] == "class":
                aNewClass = listOfWords[i]
                aNewClass = NewClass(aNewClass)
                ClassFinder.classList.append(aNewClass)

            # Add attributes
            elif ":" == listOfWords[i]:
                if (listOfWords[i - 1].isalpha()) and (listOfWords[i - 1][0].islower()) and (listOfWords[i + 1].isalpha):
                    attribute = listOfWords[i - 1] + " " + listOfWords[i] + " " + listOfWords[i + 1]
                    ClassFinder.classList[-1].add_attribute(attribute)
            # Add methods
            elif "(" in listOfWords[i]:
                partOfMethod = ""
                for j in range(i, totalWords):
                    if ")" in listOfWords[i]:
                        partOfMethod += listOfWords[i]
                        break
                    if ")" in listOfWords[j]:
                        partOfMethod += (" " + listOfWords[j])
                        if listOfWords[j + 1] == ":":
                            partOfMethod += listOfWords[j + 1] + " " + listOfWords[j + 2]

                        break
                    else:
                        partOfMethod += (listOfWords[j])

                if listOfWords[i + 1] == ":":
                    print("reach here: " + listOfWords[i])
                    method = partOfMethod + listOfWords[i + 1] + " " + listOfWords[i + 2]
                else:
                    method = partOfMethod
                ClassFinder.classList[-1].add_method(method)

    def display_my_classes():
        for aClass in ClassFinder.classList:
            print("{}".format(aClass))
            aClass.display_method()
            aClass.display_attribute()

    def get_all_my_class():
        return ClassFinder.classList
