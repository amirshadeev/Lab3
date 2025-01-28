class Account:
    def __init__(self,owner,balance = 0):
        self.owner = owner
        self.balance = balance
    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            print(f"Счет пополнен на {amount}.Ваш счет составляет {self.balance}")
        else:
            print("Error")
    def withdrawals(self, amount):
        if amount > self.balance:
            print("Не достаточно средств!")
        else:
            self.balance -=amount
            print(f"Ваш баланс:{self.balance}")
    def __str__(self):
        print(f"Владелец счета:{self.owner}.\nВаш текущий счет {self.balance}")

owner = input("Ваше имя:")
balance = int(input("Ваш баланс:"))
Mir = Account(owner,balance)
amount = int(input("Сумма пополнения:"))
Mir.deposit(amount)
amount = int(input("Сумма снятия:"))
Mir.withdrawals(amount)