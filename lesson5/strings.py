name = 'Виктор'
name_2 = "Виктор"
name_3 = "Виктор О'Нил"

text = """Привет, 
Как дела?
Что делаешь"""

text_oneline = 'Привет, \nКак дела?\nЧто делаешь'

tab_text = "Пример строки с табуляцией \n\tСтрока начаинается с отступом"

path = "D:\\\\path\\new_folder"

path_r = r"D:\\path\new_folder"

# Строка - коллекция символов

word = "peace"

# Длина строки
len(word)

# Первый символ в строке
print(word[0])

# Последний символ в строке
word[-1]

# Срезы
print(word[1:3])  # 'ea'
print(word[:3])  # 'pea'
print(word[:])  # 'peace'
print(word[:-1])  # 'peac'

# Оюъединение строк
string_1 = "some text"
string_2 = "string"
print(string_1 + string_2)

result = "some" "text"
print(result)

# Повторение строки
print(result * 4)


# Извлечение атрибута
# object.attribute

# Вызов функции
# function(arguments)

# Вызов метода
# object.method(arguments)

# Очищаем от пробелов по краям
h3 = "     Заголовок текста       "
print(h3.strip())

# Разбиваем строку
cities = "Minsk, Bobruisk, Mogilev, Gomel"
cities = cities.split(", ")

# Объединяем список в строку
", ".join(cities)
'Minsk, Bobruisk, Mogilev, Gomel'