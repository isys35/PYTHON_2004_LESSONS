users = ["alex", "dimo12", "kill212", "ula2"]
users_views = {
    "alex": 12,
    "dimo12": 23,
    "kill212": 1234,
    "ula2": 100
}

print(len(users),  " - длина списка")
print(len(users_views),  " - длина словаря")

# check_user = input("Введите имя пользователя:")
#
# if check_user in users:
#     print(check_user, " - пользователь находится в списке users")
# else:
#     print(check_user, " - пользователя нету в списке users")
#
#
# if check_user in users_views:
#     print(check_user, " - пользователь находится в ключах словаря users_views")
# else:
#     print(check_user, " - пользователь нету в ключах словаря users_views")
#
# check_views = int(input("Введите кол-во просмотров: "))
#
#
# if check_views in users_views.values():
#     print(check_views, " - такое кол-во просмотров есть в значениях словаря users_views")
#
# if (check_user, check_views) in users_views.items():
#     print((check_user, check_views), " - такая пара значений есть в словаре users_views")


# # Итерация по списку
# for user in users:
#     print(f"Пользователь: {user}")
#
# # Итерация по ключам в словаре
# for user in users_views:
#     print(f"Пользователь: {user}")
#
# # Итерация по значения в  словаре
# for view in users_views.values():
#     print(f"Просмотры: {view}")
#
# # Итерация по парам в словаре
# for user, view in users_views.items():
#     print(f"Пользователь: {user}; просмотры: {view}")

max_views = max(users_views.values())
sum_views = sum(users_views.values())
print(max_views, " - максимальное кол-во просмотров")
print(sum_views, " - всего просмотров")
# print(users.index("kill212"))
# users.clear()
# print(users)