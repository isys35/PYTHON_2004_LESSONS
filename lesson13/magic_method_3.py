class User:

    def __init__(self, name):
        self.name = name
        self.status = "PUBLIC"

    def __getattribute__(self, item):
        if item == "name" and self.status == "PRIVATE":
            raise AttributeError
        return super().__getattribute__(item)

    def __setattr__(self, key, value):
        if key not in self.__dict__:
            return super().__setattr__(key, value)


if __name__ == '__main__':
    user = User("bob")
    print(user.__dir__())
    print(dir(user))
    print(user.name)
    user.name = "Олег"
    print(user.name)
