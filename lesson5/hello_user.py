name = input("Введите имя: ").title()

welcome = f"Добро пожаловать, {name}!"
print(welcome)

number_1 = int(input("Введите первое число: "))
number_2 = int(input("Введите второе число: "))
print(f"Сумма чисел: {number_1 + number_2}")

year_salary = int(input("Введите желаюмую годовую зарплату: "))
monthly_payment = year_salary / 12
print(f"Ежемесячная выплата: {monthly_payment:12,.2f}")

discount = .2
print(f"Ваша скидка: {discount:20.0%}")


