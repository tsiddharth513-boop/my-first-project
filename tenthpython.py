# 







class account:
    def __init__(self, balance, acc_no):
        self.balance = balance
        self.acc_no = acc_no

    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("total balance =", self.balance)

    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited")
        print("total balance =", self.balance)

    def get_balance(self):
        return self.balance    

acc1 = account(1000, 12345)

acc1.debit(2000)
acc1.credit(5000)
acc1.debit(60000)
