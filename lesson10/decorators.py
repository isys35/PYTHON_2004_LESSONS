def uppercase_decorator(func):
    def wrapper():
        return func().upper()

    return wrapper


# def get_hello_world():
#     return "Hello world!"
#
# get_hello_world = uppercase_decorator(get_hello_world)

@uppercase_decorator
def get_first_name():
    return "Дмитрий"


print(get_first_name())
