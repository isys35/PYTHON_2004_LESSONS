coordinates = input("Введите координаты через ',' ").split(',')

match coordinates:
    case x, y:
        print(f"2D x: {x} y: {y}")
    case x, y, z:
        print("3D")
    case x, y, z, *args:
        print(args)
    case _:
        print("Шаблон не найден")