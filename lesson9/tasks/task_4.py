

def get_mediana(*args):
    sorted_args = sorted(args)
    len_args = len(sorted_args)
    if not len_args % 2:
        return (sorted_args[(len_args//2) - 1] + sorted_args[(len_args//2)])/2
    return sorted_args[(len_args//2)]


if __name__ == '__main__':
    values = []
    user_input = input("Введите число: ")
    while user_input:
        values.append(float(user_input))
        user_input = input("Введите число: ")
    print(f"Список значений: {values}")
    print(f"Медиана {get_mediana(*values)}")