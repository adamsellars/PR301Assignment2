class NewClass:

    def __init__(self, className: str) -> None:
        self.className = className
        self.attribute = []
        self.method = []
        self.relationship = []

    def __str__(self) -> None:
        return self.className

    def add_method(self, methodName: str) -> None:
        self.method.append(methodName)

    def add_attribute(self, attribute: str) -> None:
        self.attribute.append(attribute)

    # def display_method(self) -> None:
        #methodCounter = 1
        # for aMethod in self.method:
            #print("Method {}: {}".format(methodCounter, aMethod))
            #methodCounter += 1

    # def display_attribute(self) -> None:
        #attributeCounter = 1
        # for anAttribute in self.attribute:
            #print("Attribute {}: {}".format(attributeCounter, anAttribute))
            #attributeCounter += 1


