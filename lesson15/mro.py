class O:
    def method(self):
        print("O")


class A(O):

    def method(self):
        super().method()
        print("А")


class B(O):

    def method(self):
        super().method()
        print("B")


class C(A, B):
    def method(self):
        super().method()
        print("C")


if __name__ == '__main__':
    print(C.__mro__)
    C().method()