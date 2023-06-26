class A:
    ...


# print(type(A))


NewClass = type('NewClass', (object,), {"attribute": 0})


def my_class_init(self, attr):
    self.attr = attr


MyClass = type('MyClass', (object,), {"__init__": my_class_init})


# print(MyClass(12))

def show_me(self):
    print("Me ", self.__class__)


def my_metaclass(name, parents, attributes):
    attributes["show_me"] = show_me
    return type(name, parents, attributes)


class MetaClass(type):

    def __call__(self, name, parents, attributes):
        return type(name, parents, attributes)


class C(metaclass=MetaClass):
    pass



C().show_me()
