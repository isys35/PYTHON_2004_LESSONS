from typing import Final


class BankAccount:
    MAX_DEPOSIT: Final = 10000

    def __init__(self, balance: float, account_number: str):
        self.__balance = balance
        self.__account_number = account_number

    @property
    def balance(self) -> float:
        return self.__balance

    @balance.setter
    def balance(self, value: float) -> None:
        self.__balance = value

    @property
    def account_number(self) -> str:
        return self.__account_number[:-4] + "*" * 4

    @account_number.setter
    def account_number(self, value: str) -> None:
        self.__account_number = value

    def deposit(self, amount: float) -> None:
        if amount < 0:
            raise Exception("Сумма депозита должна быть больше 0")
        elif amount >= self.MAX_DEPOSIT:
            raise Exception("Превышена максимальная сумма депозита")
        self.__balance += amount

    def withdraw(self, amount: float) -> None:
        if amount > self.__balance:
            raise Exception("Сумма для вывода превышает сумму баланса")
        self.__balance -= amount


if __name__ == '__main__':
    bank_account = BankAccount(10000, "DDAS123123")
    assert bank_account.account_number == "DDAS12****"
    assert bank_account.balance == 10000
    bank_account.deposit(100)
    assert bank_account.balance == 10100
    bank_account.withdraw(200)
    assert bank_account.balance == 9900