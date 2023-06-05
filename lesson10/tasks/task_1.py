"ss".isalpha()

def calculate_max_min_avg(*args):
    return min(args), max(args), sum(args) / len(args)


if __name__ == '__main__':
    print(calculate_max_min_avg(2, 4, 6, 3, 4, 22))
