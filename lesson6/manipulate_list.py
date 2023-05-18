tuple_1 = (1, 2, 3)
tuple_2 = (4, 5)
tuple_3 = tuple_1 + tuple_2
print(tuple_3)

list_1 = ["a", "b", "c"]
list_2 = ["d", "e"]
list_3 = [*list_1, *list_2]

list_3.insert(2, "l")
print(list_3)
list_3.append("f")
print(list_3)
list_3.extend(list_1)
print(list_3)
print(list_3.pop())
print(list_3)
print(list_3.pop(0))
print(list_3)
