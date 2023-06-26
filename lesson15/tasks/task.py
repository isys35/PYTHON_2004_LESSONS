import time


def time_calc(func):
    def time_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Функция: {func.__name__}. Время выполнения составляет: {total_time}')
        return result

    return time_wrapper


def log_methods(name, parents, attrs):
    new_attrs = {}
    for name, value in attrs.items():
        new_attrs[name] = value
        if hasattr(value, "__call__"):
            new_attrs[name] = time_calc(value)
    return type(name, parents, new_attrs)


class TestClass(metaclass=log_methods):

    def __init__(self, attr):
        self.attr = attr

    def test_method(self):
        print("test method")


test_obj = TestClass("dasdsa")
# test_obj.test_method()
# for item in dir(test_obj):
#     attr = getattr(test_obj, item)
#     if hasattr(attr, "__call__"):
#         attr()