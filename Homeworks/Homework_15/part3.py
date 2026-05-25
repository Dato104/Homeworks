


class BankAccount:
    bank_name = "Step Bank"
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient funds!")
        else:
            self.balance -= amount
        return self.balance



    def show_balance(self):
        print(f"ბანკის სახელი: {self.bank_name}")
        print(f"მფლობელი: {self.owner}")
        print(f"მიმდინარე ბალანსი: {self.balance} ")

bank = BankAccount("Irakli", 10000000)
print(bank.deposit(100))
print(bank.withdraw(10000000))
bank.show_balance()





























