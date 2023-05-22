PRICES = ((3, 0), (12, 14), (65, 23), (200, 18))  # ((макc_возраст, цена),)
total_price = 0

while True:
    user_input = input("Введите возраст: ")
    if not user_input:
        break
    age = int(user_input)
    for max_age, price in PRICES:
        if age < max_age:
            total_price += price
            break
    print(f"Итоговая цена посещения: {total_price}")
