#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction = None

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.last_transaction = price * quantity
        for _ in range(quantity):
            self.items.append(title)

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
        else:
            self.total = self.total - (self.total * self.discount / 100)
            formatted_total = int(self.total) if self.total.is_integer() else self.total
            print(f"After the discount, the total comes to ${formatted_total}.")

    def void_last_transaction(self):
        self.total -= self.last_transaction
        self.last_transaction = None


     


