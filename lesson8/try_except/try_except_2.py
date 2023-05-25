items = [1]
# try:
#     print(items[0])
# except IndexError:
#     print("Ошибка")
# else:
#     print("Исключения не возникали")


try:
    print(items[0])
    print("Исключения не возникали")
except IndexError:
    print("Ошибка")