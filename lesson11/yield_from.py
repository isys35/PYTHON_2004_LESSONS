def count_up(stop):
    n = 1
    while n <= stop:
        yield n
        n += 1


def count_down(start):
    n = start
    while n > 0:
        yield n
        n -= 1


def up_and_down(n):
    yield from count_up(n)
    yield from count_down(n)
    # for i in count_up(n):
    #     yield i
    # for i in count_down(n):
    #     yield i


for i in up_and_down(15):
    print(i)