from abc import ABC, ABCMeta, abstractmethod


# class Hero(metaclass=ABCMeta):
#     pass

class Hero(ABC):
    @abstractmethod
    def attack(self):
        pass


class Archer(Hero):

    def attack(self):
        print("Выстрел из лука")


class C(ABC):

    @classmethod
    @abstractmethod
    def my_abstract_class_method(cls):
        ...

    @staticmethod
    @abstractmethod
    def my_abstract_static_method(cls):
        ...

    @property
    @abstractmethod
    def my_abstract_property(self):
        ...

    @my_abstract_property.setter
    @abstractmethod
    def my_abstract_property(self):
        ...


if __name__ == '__main__':
    archer = Archer()
    archer.attack()
