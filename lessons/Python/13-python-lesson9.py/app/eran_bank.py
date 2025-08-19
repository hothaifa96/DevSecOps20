from abc import ABC, abstractmethod


class BankAccount(ABC):
    def __init__(self, holder, balance, account_number):
        self.holder = holder
        self._balance = balance  # private
        self.account_number = account_number

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def get_balance(self):
        pass

    @abstractmethod
    def set_balance(self, balance):
        pass

    def __str__(self):
        return f'balance : {self._balance}'


class CheckingAccount(BankAccount):
    def __init__(self, holder, account_number, last_activities, credit_limit):
        super().__init__(holder, 0, account_number)
        self.last_activities = last_activities
        self.credit_limit = credit_limit

    def withdraw(self, amount):
        return amount if self._balance > amount else 0

    def deposit(self, amount):
        self._balance += amount

    def get_balance(self):
        return self._balance * 0.82

    def set_balance(self, balance):
        if balance < 0:
            return
        self._balance = balance - 5.9


# class SavingAccount(BankAccount):
#     def __init__(self, holder, account_number, gate_date, rate):
#         super().__init__(holder, 0, account_number)
#         self.gate_date = gate_date
#         self.rate = rate
#
#     def withdraw(self, amount):
#         return amount if self.balance > amount else 0
#
#     def deposit(self, amount):
#         self.balance += amount


if __name__ == '__main__':
    acc1 = CheckingAccount('roman', 1233, [], 15000)
    print('test', acc1)
