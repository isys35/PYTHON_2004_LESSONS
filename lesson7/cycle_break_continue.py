# numbers = [3, 24, 23, 22, 11]
#
# for number in numbers:
#     print(number)
#     if not number % 3:
#         print(f"Найдено число, которое делится на 3: {number}")
#         break


items_lists = [3, "Виктор", 23, 42.23, 32.0, "Олег", 45, 34]

for item in items_lists:
    print(item)
    if not isinstance(item, int):
        continue
    print(item)
    if not item % 5:
        print(f"Найдено число, которое делится на 5: {item}")
        break
else:
   print("Не выполнен оператор break")