from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card.")

class UpiPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI.")

# client code
def process_payment(payment_method, amount):
    payment_method.pay(amount)

# Using abstraction
cc = CreditCardPayment()
upi = UpiPayment()


process_payment(cc, 5000)
process_payment(upi, 1200)
