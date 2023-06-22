class Cat:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print("Это кот")

    def make_sound(self):
        print("Мяу")


class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print("Это собака")

    def make_sound(self):
        print("Гав")


if __name__ == '__main__':
    cat = Cat("Кот", 3)
    dog = Dog("Собака", 4)

    for animal in [cat, dog]:
        animal.make_sound()
        animal.info()
