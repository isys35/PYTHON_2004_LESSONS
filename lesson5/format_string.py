TEMPLATE = "Имя: {0}. Возраст: {1}"

name = "Bob"
age = 23

info = TEMPLATE.format(name, age)
print(info)

info_2 = "Ваше имя: %s. Возраст: %d" % (name, age)
print(info_2)