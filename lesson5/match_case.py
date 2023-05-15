command = input("Введите комманду: ").lower()
step = input("Введите кол-во шагов")

match command, step:
    case "вперёд" | "вверх", int(step):
        print(f"Персонаж идёт вперёд на {step} шагов")
    case "назад":
        print("Персонаж идёт назад")
    case "налево":
        print("Персонаж идёт налево")
    case "направо":
        print("Персонаж идёт направо")
    case _:
        print("Не указано направление")