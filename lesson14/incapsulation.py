class User:

    def __init__(self, age: int = 0):
        self.__age = age

    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, age: int) -> None:
        if age < 18:
            raise Exception
        self.__age = age


if __name__ == '__main__':
    user = User(12)
    print(user.age)
    user.age = 3
    # print(user.get_age())
