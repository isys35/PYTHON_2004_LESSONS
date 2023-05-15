age = int(input("Введите возраст: "))
name = input("Введите имя: ")

prefix = "Здравствуйте!" if age > 18 else "Привет!"

print(f"{prefix} {name.title()}")