def repeat(count):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(count):
                func(*args, **kwargs)
        return wrapper
    return decorator


@repeat(12)
def calculate_sum(num_1, num_2):
    result = num_1 + num_2
    print(result)


# calculate_sum = repeat(12)(calculate_sum)

calculate_sum(3, 5)
