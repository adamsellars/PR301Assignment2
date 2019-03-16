class PEP8Converter:

    def convert_class(plantClassName):
        className = plantClassName.capitalize()
        className = "class {}:\n".format(className)
        return className

    def convert_method(plantMethod):
        if ":" in plantMethod:
            methodAndType = plantMethod.split(":")
            returnType = methodAndType[1].strip()
            method = methodAndType[0][0].lower() + methodAndType[0][1:].rstrip()
            methodName = "\n    def {}:\n        return {}\n".format(method, returnType)
            return methodName
        else:
            plantMethod = plantMethod[0].lower() + plantMethod[1:]
            methodName = "\n    def {}:\n        return\n".format(plantMethod)
            return methodName

    def convert_attribute(plantAttribute):
        attributeAndType = plantAttribute.split(":")
        returnType = attributeAndType[1].strip()
        attribute = attributeAndType[0][0].lower() + attributeAndType[0][1:].strip()
        anAttribute = "    {} = {}\n".format(attribute, returnType)
        return anAttribute

    def create_class(plantClassName):
        print(plantClassName.method)
        methods = ""
        attributes = ""
        constructor = "\n    def __init__(self): \n        pass\n"
        className = PEP8Converter.convert_class(plantClassName.className)
        for aMethod in plantClassName.method:
            methods += PEP8Converter.convert_method(aMethod)
        for anAtrribute in plantClassName.attribute:
            attributes += PEP8Converter.convert_attribute(anAtrribute)
        return className + attributes + constructor + methods



