from functools import reduce
# func = lambda x: x**2
#
# print(func(5))

my_list = [1, 3, 5, 654, 123, 32, 3]
# result = list(filter(lambda x: x % 2 == 0, my_list))
# print(result)

# result = [i for i in my_list if i % 2 == 0]
# print(result)


data = [
    {"id": 6, "name": "Виктор", "views": 10},
    {"id": 5, "name": "Дмитрий", "views": 24},
    {"id": 2, "name": "Олег", "views": 23},
    {"id": 1, "name": "Иван", "views": 1},
]

result = sorted(data, key=lambda item: item["name"])
print(result)

# reduce
summa = reduce(lambda x, y: {"views": x["views"] + y["views"]}, data)
print(summa)