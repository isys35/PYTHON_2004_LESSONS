message = "Глобальная переменная"


def my_function():
    message = "Локальная переменная с таким же имененем"
    print("Мы внутри функции")
    print(message)

    message_1 = "Локальная переменная"
    print(message_1)


my_function()
print("Мы за функцией")
print(message)
# print(message_1)