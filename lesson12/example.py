# Цепочка объектов

class Chain:

    def __init__(self, name, n=1, index=0):
        self.index = index
        self.name = name
        if n == 1:
            self.next = None
        else:
            self.next = self.__class__(name, n - 1, index + 1)

    def __repr__(self):
        return f"{self.__class__.__name__} {self.name} {self.index}"

    def __getitem__(self, item):
        if not self.index:
            raise IndexError


if __name__ == '__main__':
    chain = Chain("Item", 4)
    # chain[3]
    print()
