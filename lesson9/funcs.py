def hello(name):
    if not name:
        return
    message = f"Добро пожаловать, {name}"
    print(message)
    return message


# print(hello)
# print(type(hello))
# print(id(hello))
#
# hello("Дмитрий")


def times(x, y):
    return x * y


result = times(4, 5)

# print(result)

say = hello

say("Олег")
