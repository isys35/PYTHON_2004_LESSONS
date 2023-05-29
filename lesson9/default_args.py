def find_square(value=2):
    return value * value


# print(find_square(5))


def func(param=None):
    if param is None:
        param = []
    param.append(1)
    print(param)


func()
func()
func()
func()


def print_data(data, *, start=0, end=100):
    for value in data[start:end]:
        print(value)

print_data(["a", "b", "c", "d"])
