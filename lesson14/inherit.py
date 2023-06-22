class Table:
    def __init__(self, length: float, weight: float, height: float):
        self.length = length
        self.weight = weight
        self.height = height


class DeskTable(Table):

    def square(self) -> float:
        return self.weight * self.length


class ComputerTable(DeskTable):

    def square(self, monitor: float = 0.0) -> float:
        return self.weight * self.length - monitor


class KitchenTable(Table):

    def __init__(self, length: float, weight: float, height: float, places: int):
        # Table.__init__(self, length, weight, height)
        super().__init__(length, weight, height)
        self.places = places


if __name__ == '__main__':
    table1 = Table(10, 20, 2)
    table2 = DeskTable(2, 3, 4)
    table3 = ComputerTable(0.8, 2, 3)
    table4 = KitchenTable(2, 3, 4, 5)
    print(table4.__dict__)
    # print(table3.square(monitor=1))
    # print(table2.square())
