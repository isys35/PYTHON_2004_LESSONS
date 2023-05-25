COUNT_EXTREME = 2


def remove_extreme(values, n):
    sorted_values = sorted(values)
    print("Исходный список: ", sorted_values)
    print("Финальный список: ", sorted_values[n:-n])


def main():
    values = []
    user_input = input("Введите значениу (Enter для выхода): ")
    while user_input != "":
        values.append(float(user_input))
        user_input = input("Введите значениу (Enter для выхода): ")
    if len(values) < 4:
        raise ValueError("Мало значений")
    remove_extreme(values, COUNT_EXTREME)


if __name__ == '__main__':
    try:
        main()
    except ValueError as exc:
        print("Ошибка: ", exc)
