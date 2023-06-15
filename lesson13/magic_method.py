class Car:

    def __new__(cls, *args, **kwargs):
        print("Настоящий конструктор класса")
        return super().__new__(cls)

    # def __init_subclass__(cls, **kwargs):
    #     pass

    def __init__(self):
        self.attr_1 = "attr_1"

    def __del__(self):
        print(f"{self} Объект удалён")

    def __repr__(self):
        return f"Class: {self.__class__.__name__}, attrs: {self.__dict__}"

    def __str__(self):
        return self.attr_1


if __name__ == '__main__':
    car = Car()
