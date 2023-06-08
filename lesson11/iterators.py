class CounterState:
    def __init__(self, step):
        self.step = step

    def __next__(self):
        if self.step <= 0:
            raise StopIteration
        self.step -= 1
        return self.step


class CountDown:
    def __init__(self, step):
        self.step = step

    def __iter__(self):
        return CounterState(self.step)


counter = CountDown(step=12)
iter_counter = iter(counter)
print(next(iter_counter))
print(next(iter_counter))
print(next(iter_counter))
for i in counter:
    print(i)

for i in counter:
    print(i)
