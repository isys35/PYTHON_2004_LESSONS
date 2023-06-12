class TypeAttr:
    CHECK_TYPES = [int, str]

    @staticmethod
    def check_equal_type(arg_1, arg_2, arg_type):
        return isinstance(arg_1, arg_type) and isinstance(arg_2, arg_type)

    def __init__(self, arg_1, arg_2):
        for arg_type in self.CHECK_TYPES:
            if self.check_equal_type(arg_1, arg_2, arg_type):
                self.__dict__["attr_" + arg_type.__name__] = arg_1 + arg_2


def main():
    type_attr = TypeAttr("string1", "string2")
    assert hasattr(type_attr, "attr_str")
    assert type_attr.attr_str == "string1string2"

    type_attr = TypeAttr(2, 5)
    assert hasattr(type_attr, "attr_int")
    assert type_attr.attr_int == 7


if __name__ == '__main__':
    main()
