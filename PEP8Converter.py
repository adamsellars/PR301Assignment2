class PEP8Converter:

    @staticmethod
    def convert_class(plant_class_name: str) -> str:
        class_name = plant_class_name.capitalize()
        class_name = "class {}:\n".format(class_name)
        return class_name

    @staticmethod
    def create_class(plant_class_name: str) -> str:
        methods = ""
        attributes = ""
        class_name = PEP8Converter.convert_class(plant_class_name.class_name)
        for aMethod in plant_class_name.method:
            if "init" in aMethod:
                for an_attribute in plant_class_name.attribute:
                    print("I am attribute: ", an_attribute)
                    attributes += PEP8Converter.convert_attribute(an_attribute)
                methods += PEP8Converter.convert_constructor(aMethod, attributes)
            else:
                methods += PEP8Converter.convert_method(aMethod)

        return class_name + methods

    @staticmethod
    def convert_method(plant_method: str) -> str:
        print("My method: ", plant_method)
        if "init" in plant_method:
            print("I have a constructor")
        elif "String" in plant_method:
            plant_method = plant_method.replace("String", "str")

        total_words = len(plant_method)
        my_method = ""
        for i in range(total_words):
            if "(" in plant_method[i]:
                print("here1")
                for j in range(i, total_words):
                    if ")" in plant_method[j]:
                        plant_method = list(plant_method)
                        print("here3")
                        print("small stuff: ", plant_method[j+1])
                        plant_method[j+1] = " ->"
                        my_method = "".join(plant_method).lstrip()
        pep8_method = "\n    def {}:\n        pass\n".format(my_method)
        return pep8_method

    @staticmethod
    def convert_constructor(plant_method: str, pep8_attributes: str) -> str:
        if "String" in plant_method:
            plant_method = plant_method.replace("String", "str")
        total_words = len(plant_method)
        my_method = ""
        for i in range(total_words):
            if "(" in plant_method[i]:
                for j in range(i, total_words):
                    if ")" in plant_method[j]:
                        plant_method = list(plant_method)
                        plant_method[j + 1] = " ->"
                        my_method = "".join(plant_method).lstrip()
        pep8_method = "\n    def {}:\n    {}".format(my_method, pep8_attributes)
        return pep8_method

    @staticmethod
    def convert_attribute(plant_attribute: str) -> str:
        attribute_and_type = plant_attribute.split(":")
        return_type = attribute_and_type[1].strip()
        attribute = attribute_and_type[0][0].lower() + attribute_and_type[0][1:].strip()
        an_attribute = "    self.{} = {}    \n    ".format(attribute, return_type)
        return an_attribute



    # @staticmethod
    # def create_relationship():

