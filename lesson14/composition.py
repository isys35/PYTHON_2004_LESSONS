class Engine:
    pass


class Car:
    engine: Engine

    def __init__(self) -> None:
        self.engine = Engine()


if __name__ == '__main__':
    car = Car()
