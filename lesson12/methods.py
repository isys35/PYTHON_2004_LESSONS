
class Toy:
    def instance_method(self):
        return "Метод объекта", self

    @classmethod
    def class_method(cls):
        return "Метод класса", cls

    @staticmethod
    def static_method():
        return "Статический метод"


if __name__ == '__main__':
    toy = Toy()
    print(toy.instance_method())
    print(toy.class_method())
    print(Toy.class_method())
    print(Toy.instance_method(toy))
    print(Toy.static_method())
    print(toy.static_method())
    print(isinstance(toy, Toy))
