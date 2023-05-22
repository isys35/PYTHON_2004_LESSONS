user_numbers = []

while True:
    number = float(input("Введите число: "))
    if not user_numbers and not number:
        raise ValueError("0 не может быть первым числом")
    if not number:
        break
    user_numbers.append(number)
    print(f"Среднее значение: {sum(user_numbers)/len(user_numbers):.2f}")