class PEP8Converter:

    @staticmethod
    def convert_class(plant_class_name: str) -> str:
        class_name = plant_class_name
        class_name = "class {}:\n".format(class_name)
        return class_name

    # for a relationship in a class, if relationship equal to composition, then format code to PEP8 else return nothing.
    @staticmethod
    def create_relationship(plant_relationship: str, counter: int) -> str:
        if "--" in plant_relationship:
            relationships = plant_relationship.split()
            relationship_content = "\nobject{} = {}()".format(counter, relationships[1])
            return relationship_content
        else:
            return ""

    @staticmethod
    def set_import(plant_relationship: str) -> str:
        if "--" in plant_relationship:
            relationships = plant_relationship.split()
            import_statement = 'from {} import {}\n'.format(relationships[1], relationships[1])
            return import_statement
        else:
            return ""

    @staticmethod
    def create_class(plant_class_name: str) -> str:
        methods = ""
        attributes = ""
        relationship = ""
        import_class = ""
        counter = 1
        class_name = PEP8Converter.convert_class(plant_class_name.class_name)
        for a_method in plant_class_name.method:
            if "init" in a_method:
                for an_attribute in plant_class_name.attribute:
                    # print("I am an attribute: ", an_attribute)
                    attributes += PEP8Converter.convert_attribute(an_attribute)
                    # print(attributes)
                methods += PEP8Converter.convert_constructor(a_method, attributes)
            else:
                methods += PEP8Converter.convert_method(a_method)
        if (len(plant_class_name.relationship)) > 0:
            for a_relationship in plant_class_name.relationship:
                relationship += PEP8Converter.create_relationship(a_relationship, counter)
                import_class += PEP8Converter.set_import(a_relationship)
                counter += 1
            return "from typing import TypeVar\n" + import_class + "\n" + "T = TypeVar('T')" + "\n\n\n" +\
                   class_name + methods + "\n" + relationship + "\n"
        else:
            return class_name + methods + relationship

    @staticmethod
    def convert_method(plant_method: str) -> str:
        print(plant_method)
        if "String" in plant_method:
            plant_method = plant_method.replace("String", "str")
        elif "Object" in plant_method:
            plant_method = plant_method.replace("Object", "T")
        total_words = len(plant_method)
        my_method = ""
        for i in range(total_words):
            if "(" in plant_method[i]:
                for j in range(i, total_words):
                    if ")" in plant_method[j]:
                        plant_method = list(plant_method)
                        plant_method[j+1] = " ->"
                        my_method = "".join(plant_method).lstrip()
        if "self" not in my_method:
            pep8_method = "\n    @staticmethod\n    def {}:\n        pass\n".format(my_method)
        else:
            pep8_method = "\n    def {}:\n        pass\n".format(my_method)
        return pep8_method

    @staticmethod
    def convert_constructor(plant_method: str, pep8_attributes: str) -> str:
        if "String" in plant_method:
            plant_method = plant_method.replace("String", "str")
        elif "Object" in plant_method:
            plant_method = plant_method.replace("Object", "T")
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
        if "String" in plant_attribute:
            plant_attribute = plant_attribute.replace("String", "str")
        attribute_and_type = plant_attribute.split(":")
        return_type = attribute_and_type[1].strip()
        attribute = attribute_and_type[0][0].lower() + attribute_and_type[0][1:].strip()
        an_attribute = "    self.{} = {}    \n    ".format(attribute, return_type)
        return an_attribute







