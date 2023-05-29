def add_one(x):
    return x + 1


def call_with_five(function):
    return function(5)


def double(function):
    def inner(argument):
        return function(argument)

    return inner


def multiply_by_five(x):
    return x * 5

inner_func = double(multiply_by_five)
print()

# print(call_with_five(add_one))
# print(add_one(5))
