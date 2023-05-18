dict_1 = {"a": 1, "b": 2}
dict_2 = {"b": 3, "d": 4}

dict_3 = dict_1.copy()
dict_3.update(dict_2)
print(dict_3)

dict_4 = {**dict_2, **dict_1}
print(dict_4)

dict_5 = dict_1 | dict_2
print(dict_5)


dict_5["e"] = 5

print(dict_5)
dict_5["b"] = 1


# print(dict_5["k"])
element = dict_5.get("k", 0)
print(element)