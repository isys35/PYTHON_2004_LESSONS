try:
    number = int(input("Введите число: "))
    print(100 / number)
    my_file = open("file.txt", "r")
except (ValueError, ZeroDivisionError):
    print("Введите корректное число")
except Exception as exc:
    print("Неизвестная ошибка: ", exc)