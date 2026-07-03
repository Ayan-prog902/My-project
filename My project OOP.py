from abc import ABC, abstractmethod


# -------------------------
# Abstraction
# -------------------------
class BankAccount(ABC):

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance      # Encapsulation

    # Encapsulation (Getter)
    def get_balance(self):
        return self.__balance

    # Encapsulation (Setter methods)
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Rs.{amount} deposited successfully.")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Rs.{amount} withdrawn successfully.")
        else:
            print("Insufficient Balance!")

    # Abstraction
    @abstractmethod
    def account_type(self):
        pass


# -------------------------
# Inheritance
# -------------------------
class SavingsAccount(BankAccount):

    # Polymorphism
    def account_type(self):
        print("Savings Account")


class CurrentAccount(BankAccount):

    # Polymorphism
    def account_type(self):
        print("Current Account")


# -------------------------
# Main Program
# -------------------------
account1 = SavingsAccount("Ayan", 5000)
account2 = CurrentAccount("Ali", 10000)

print("Customer:", account1.name)
account1.account_type()
print("Balance:", account1.get_balance())

account1.deposit(2000)
account1.withdraw(1000)
print("Final Balance:", account1.get_balance())

print("\n-----------------\n")

print("Customer:", account2.name)
account2.account_type()
print("Balance:", account2.get_balance())

account2.withdraw(12000)
account2.deposit(5000)
print("Final Balance:", account2.get_balance())