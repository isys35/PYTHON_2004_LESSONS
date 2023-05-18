list_1 = [-2, -1, 0, 1, 2, 3, 4, 5]
# list_2 = [x for x in list_1]
# list_2 = list_1(list_1)
# list_2 = list_1[:]
# list_2 = list_1.copy()

list_2 = [x**2 for x in list_1 if x > 0]
set_3 = {x**2 for x in list_1 if x > 0}
dict_3 = {list_1.index(x): x for x in list_1}
print(dict_3)


users = ["isss", "vadim", "kiril"]
views = [12, 42, 45]

if len(users) != len(views):
    raise Exception("Разная длинна")

dict_4 = {users[index]: views[index] for index in range(len(users))}
print(dict_4)


print(dict(zip(users, views)))
# for user, view in zip(users, views):
#     print(user, view)

