class SingletoneMeta(type):

    def __init__(cls, name, bases, namespase):
        super().__init__(name, bases, namespase)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class SingletoneBase(metaclass=SingletoneMeta):
    pass


class A(SingletoneBase):
    pass


class B(A):
    pass


if __name__ == '__main__':
    a = A()
    a_1 = A()
    a_2 = A()
    print(a, a_1, a_2)
    b = B()
    b_1 = B()
    b_2 = B()
    print(b, b_1, b_2)
