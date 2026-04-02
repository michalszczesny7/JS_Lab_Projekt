class InvoiceItem:
    def __init__(self, name, quantity, unit_net_price, vat_rate):
        self.name = name
        self.quantity = quantity
        self.unit_net_price = unit_net_price
        self.vat_rate = vat_rate
    def brutto_worth_price(self):
        return self.net_worth_price() + self.calculate_vat()
    def calculate_vat(self):
        return self.net_worth_price() * self.vat_rate
    def net_worth_price(self):
        return self.unit_net_price * self.quantity
    def to_dict(self): 
        return {
  "name": self.name,
  "quantity": self.quantity,
  "net": self.net_worth_price(),
  "vat": self.calculate_vat(),
  "gross": self.brutto_worth_price()
}



item = InvoiceItem("Laptop", 2, 1000, 0.23)

print(item.net_worth_price())
print(item.calculate_vat())
print(item.brutto_worth_price())