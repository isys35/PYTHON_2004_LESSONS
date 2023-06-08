
def fibonachi():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b

# fib = fibonachi()
#
# print([next(fib) for i in range(10)])


def gen_squares(number):
    for i in range(number):
        yield i ** 2

#
# for i in gen_squares(23):
#     print(i)


# variable = (yield)
def psyhologic():
    print("Пожалуйста, расскажите о вашей проблеме")
    while True:
        answer = (yield)
        if answer.endswith("?"):
            print("Не задавайте себе слишком много вопросов")
        elif "хорошо" in answer:
            print("Это хорошо, продолжай.")
        elif "плохо" in answer:
            print("Не будьте таким негативным.")


gen_psy = psyhologic()
next(gen_psy)