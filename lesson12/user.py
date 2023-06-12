class User:
    # type = "Пользователь"
    # description = "Описание"
    name = "Undefined"

    # def __init__(self, name=None):
    #     if name:
    #         self.name = name
    #     else:
    #         self.name = User.name

    def show_name(self):
        print(f"Имя {self.name}")

    # def change_name(self, name):
    #     self.name = name
    #     print("Имя успешно изменено")


def main():
    user = User()
    print(user)


if __name__ == '__main__':
    main()
