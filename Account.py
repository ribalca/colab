#Задание ООП
'''
Нужно реализовать класс Account, который отражает абстракцию базового
поведения банковского аккаунта:
● создать банковский аккаунт с параметрами: имя; стартовый баланс с
которым зарегистрирован аккаунт; история операций*;
● реализовать два метода, которые позволяют положить деньги на счёт
или снять деньги со счёта;
● продумать, как можно хранить историю поступления или снятия
денег, чтобы с ней было удобно работать*.
'''

class Account:
    def __init__(self, name, initial_balance):
        self.name = name
        self.balance = initial_balance
        self.history = []

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сумма депозита должна быть больше нуля.")

        self.balance += amount
        self.history.append(f"Депозит: {amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Недостаточно средств на счету.")

        self.balance -= amount
        self.history.append(f"Снятие: {amount}")

    def get_history(self):
        return self.history



account = Account('Александр Пушкин', 10000)

print("Test 1")
# Пополнение баланса
account.deposit(1000)
print(f'Внесена сумма 1000, итого на счету: {account.balance}')

# Снятие средств
account.withdraw(500)
print(f'Снята сумма 500, итого на счету: {account.balance}')

# Просмотр истории операций
history = account.get_history()
print("\nИстория операций:")
for operation in history:
    print(operation)

print("Test 2")
# Пополнение баланса
account.deposit(500)
print(f'Внесена сумма 500, итого на счету: {account.balance}')

# Снятие средств
account.withdraw(10000)
print(f'Снята сумма 10000, итого на счету: {account.balance}')

# Просмотр истории операций
history = account.get_history()
print("\nИстория операций:")
for operation in history:
    print(operation)
