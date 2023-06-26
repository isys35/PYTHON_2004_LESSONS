class Base:

    def price(self):
        return 10


class InterFoo(Base):

    def price(self):
        return super().price() * 1.1


class Discount(InterFoo):

    def price(self):
        return super().price() * 0.8


if __name__ == '__main__':
    discount = Discount()
    print(discount.price())
