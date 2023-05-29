# def greet(name, message):
#     print(f"Привет, {name}! {message}")

# # Позиционные аргументы
# greet("Олег", "Как ты?")
#
# # Именнованные аргументы
# greet(name="Олег", message="Как дела?")
#
# # Именнованные аргументы (не по порядку)
# greet(message="Как дела?", name="Олег")
#
# greet("Олег", message="Как дела?")


def greet(*args):
    for name in args:
        print(f"Привет, {name}")


greet("Олег", "Виктор", "Дима", "Владимир")


def greet_me(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")


greet_me(name="Олег", age=22, profesion="Водитель")


def multi_greet(*args, **kwargs):
    for arg in args:
        print(f"Позиционные аргументы {arg}")
    for key, value in kwargs.items():
        print(f"Именованные аргументы: {key} = {value}")


multi_greet(1, 2, 3, name="Олег")
