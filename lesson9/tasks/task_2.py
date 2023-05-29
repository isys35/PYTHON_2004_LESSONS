BASE_PRICE = 4.00
BASE_DISTANCE = 0.14
PRICE_PER_DISTANCE = 0.25


def calculation_taxi_pay(distance):
    return BASE_PRICE + (distance // BASE_DISTANCE) * PRICE_PER_DISTANCE


if __name__ == "__main__":
    distance = float(input("Введите дальность поездки (км): "))
    print(f"Cумма за вашу поездку: {calculation_taxi_pay(distance)}")