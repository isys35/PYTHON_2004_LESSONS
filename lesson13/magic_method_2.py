class User:

    def __init__(self, username, email, phone, age):
        self.username = username
        self.email = email
        self.phone = phone
        self.age = age

    def __eq__(self, other):
        return self.username == other.username

    def __gt__(self, other):
        return self.age > other.age


if __name__ == '__main__':
    user_1 = User("bob12", "bob12@mail.ru", "+37512331123", 12)
    user_2 = User("bob12", "bob32@mail.ru", "+37512423423", 22)
    if user_1 == user_2:
        print("Объекты равны")
    if user_1 < user_2:
        print("user_1 < user_2")
