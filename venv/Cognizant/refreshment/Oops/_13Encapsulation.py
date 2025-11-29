class BankAccount:
    x = 10
    def __init__(self,balance):
        self.__balance = balance


    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

    def withdraw(self,amount):
        self.__balance -= amount

acc = BankAccount(1000)
acc.deposit(500)
print(acc.get_balance())
acc.withdraw(1000)
print(acc.get_balance())

x = 9
_y = 2
__z = 3