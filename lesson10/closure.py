# def outer_func():
#     def inner_func():
#         print("Hello world")
#
#     inner_func()
#
#
# outer_func()


# def multiply(num_1):
#     def inner(num_2):  # Замыкание
#         return num_1 * num_2
#
#     return inner
#
#
# result = multiply(32)
# print(result(3))


def func_1():
    number = 1
    string = "abc"
    items = [1, 2, 3]

    def func_2():
        items.append(4)
        nonlocal number
        nonlocal string
        number += 1
        string += "?"
        return items, number, string

    return func_2

call_func_1 = func_1()
print(call_func_1())