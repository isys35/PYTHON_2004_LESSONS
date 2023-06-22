from typing import Protocol


class AnimalType(Protocol):
    name: str
    age: int

    def info(self) -> None:
        ...

    def make_sound(self) -> None:
        ...


class Cat:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def info(self) -> None:
        print("Это кот")

    def make_sound(self) -> None:
        print("Мяу")


class Dog:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def info(self) -> None:
        print("Это собака")

    def make_sound(self) -> None:
        print("Гав")


if __name__ == '__main__':
    cat = Cat("Кот", 3)
    dog = Dog("Собака", 4)
    animals: list[AnimalType] = [cat, dog]
    for animal in animals:
        animal.make_sound()
        animal.info()
