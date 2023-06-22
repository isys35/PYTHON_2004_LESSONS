class Engine:
    pass


class Car:

    def __init__(self, engine: Engine):
        self.engine = engine


if __name__ == '__main__':
    engine = Engine()
    car = Car(engine)
