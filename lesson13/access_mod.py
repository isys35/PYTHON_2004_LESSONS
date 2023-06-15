
class Car:
    def __init__(self):
        self.name = "corrola"
        self._model = 1999
        self.__make = "toyota"

    def __get_model(self):
        print("protected_method")


if __name__ == '__main__':
    car = Car()
    print(car._model)
    print(car._Car__make)
    car._Car__get_model()

