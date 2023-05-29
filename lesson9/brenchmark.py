import time


def brenchmark(function):
    def inner():
        now = time.time()
        function()
        result = time.time() - now
        print(f"{function.__name__} выполнялась {result} c")

    return inner


def test_function():
    time.sleep(5)


def test_cycle():
    for i in range(100):
        print(i)


test_cycle = brenchmark(test_cycle)

test_cycle()
