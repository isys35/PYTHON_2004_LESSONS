class WeekIterator:

    def __init__(self):
        self.day = 0

    def __next__(self):
        if self.day == 7:
            raise StopIteration
        self.day += 1
        return self.day


class Week:
    LENGHT = 7

    def __len__(self):
        return self.LENGHT

    def __iter__(self):
        return WeekIterator()

    def __getitem__(self, item):
        if item > 6 or item < 0:
            raise IndexError
        return item + 1

    #     __contains__ проверка с помощью in


if __name__ == '__main__':
    week = Week()
    for day in week:
        print(day)

    print(len(week))
    print(week[2])
    week[2] = "dsadas"
