from abc import ABC, abstractmethod

class Order:
    items = []
    quantities = []
    prices = []
    status = 'open'

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total

class PaymentProcessor(ABC):

    @abstractmethod
    def pay(self, order):
        pass

class SecurityProcessor(PaymentProcessor):
    def __init__(self, order, security_code):
        self.order = order
        self.security_code = security_code

class EmailProcessor(PaymentProcessor):
    def __init__(self, order, email_address):
        self.order = order
        self.email_address = email_address

class TwoFactorAuthentication(ABC):
    verified = False
    @abstractmethod
    def verify_code(self, code):
        pass

    @abstractmethod
    def is_verified(self) -> bool:
        pass

class DebitPaymentProcessor(SecurityProcessor, TwoFactorAuthentication):
    def pay(self, order):
        print("Processing debit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = 'paid'

    def verify_code(self, code):
        print(f'verifying SMS code {code}')
        self.verified = True
    
    def is_verified(self):
        return self.verified

class CreditPaymentProcessor(SecurityProcessor):
    def pay(self, order):
        print('Processing Credit Payment type')
        print(f'verifying security code: {self.security_code}')
        order.status = 'paid'

class PaypalPaymentProcessor(EmailProcessor):
    def pay(self, order):
        print("Processing Paypal Payment type")
        print(f'verifying email address: {self.email_address}')
        order.status = 'paid'
        

order = Order()
order.add_item("keyboard", 1, 50)
order.add_item('SSD', 1, 150)
order.add_item('USB cable', 2, 5)
print(order.total_price())

processor = DebitPaymentProcessor(order, '123456789')
processor.verify_code(123456)
print(processor.is_verified())
processor.pay(order)