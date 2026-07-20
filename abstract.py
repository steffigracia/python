from abc import ABC,abstractmethod
class payment(ABC):
    def pay(self,amount):
        pass
class UPI(payment):
    def pay(self,amount):
        print(f"Paid Rs.{amount} using UPI")
class Card(payment):
    def pay(self,amount):
        print(f"Paid Rs. {amount} using Debit card")
class COD(payment):
    def pay(self,amount):
        print(f"Cash on Delivery: Pay Rs. {amount} to delivery boy")
def checkout(payment_method,amount):
    payment_method.pay(amount)

p1 = UPI()
p2 = Card()
p3 = COD()
checkout(p1, amount=500)
checkout(p1, amount=1200)
checkout(p1, amount=299)
