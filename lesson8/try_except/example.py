while True:
    try:
        user_input = int(input("Введите число от 1 до 12: "))
        for mult in range(1, 10):
            if user_input <= 0 or user_input >= 13:
                raise ValueError
            print(f"{user_input} x {mult} = {mult * user_input}")
    except ValueError:
        print("Введите правильное значение")