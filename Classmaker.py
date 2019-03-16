
class NewClass:

    def __init__(self, className):
        self.className = className
        self.attribute = []
        self.method = []
        self.relationship = None

    def __str__(self):
        return self.className

    # def __repr__(self):
        # return self.className

    def addMethod(self, methodName):
        self.method.append(methodName)

    def addAttribute(self, attribute):
        self.attribute.append(attribute)

    def displayMethod(self):
        methodCounter = 1
        for aMethod in self.method:
            print("Method {}: {}".format(methodCounter, aMethod))
            methodCounter += 1

    def displayAttribute(self):
        attributeCounter = 1
        for anAttribute in self.attribute:
            print("Attribute {}: {}".format(attributeCounter, anAttribute))
            attributeCounter += 1


