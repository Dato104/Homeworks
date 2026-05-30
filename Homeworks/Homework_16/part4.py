

class CreditCardPayment:
    def pay(self, amount):
        return f"Paid {amount}$ with Credit Card"

class PayPalPayment:
    def pay(self, amount):
        return f"Paid {amount}$ with PayPal"

class CryptoPayment:
    def pay(self, amount):
        return f"Paid {amount}$ with Crypto"


credit = CreditCardPayment()
paypal = PayPalPayment()
crypto = CryptoPayment()

print(credit.pay(100))
print(paypal.pay(200))
print(crypto.pay(300))







































