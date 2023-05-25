
try:
    file = open("file.txt", "w")
    try:
        file.write("Какой-то текст")
    except Exception as exc:
        print(exc)
    finally:
        file.close()
        print("Файл закрыт")
except FileNotFoundError:
    print("Файл не найден")