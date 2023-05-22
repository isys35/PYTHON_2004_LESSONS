some_string = "abcde"

for letter in some_string:
    print(letter)


# coordinates = [(10, 20, 30), (49, 21, 32), (13, 33, 14)]
#
# for x, _, z in coordinates:
#     print(f"x: {x}, z: {z}")

coordinates = [(10, 20), (49, 21, 32, 44, 55), (13, 33, 14, 22)]

# for x, y, *extra in coordinates:
#     print(x, y, extra)
#
#
# for *firsts, x, y in coordinates:
#     print(firsts, x, y)
#

# for first, *_, last in coordinates:
#     print(first, last)


# dict_1 = {"a": 1, "b": 2}
#
# for key, item in dict_1.items():
#     print(key, item)

names = ["Kirill", "Victor", "Dima"]

for index, name in enumerate(names):
    print(f"Индекс: {index}, Имя: {name};")