
def calculate_hypotenuse(katet_1, katet_2):
    return (katet_1 ** 2 + katet_2 ** 2)**.5


if __name__ == "__main__":
   katet_1 = float(input("Введите значение 1-го катета: "))
   katet_2 = float(input("Введите значение 2-го катета: "))
   print(f"Гипотенуза равна {calculate_hypotenuse(katet_1, katet_2)}")