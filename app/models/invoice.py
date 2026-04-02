from invoice_item import InvoiceItem
import json

class Invoice:
    def __init__(self, invoice_number, buyer_name):
        self.invoice_number = invoice_number
        self.buyer_name = buyer_name
        self.items = []

    def add_item(self, item: InvoiceItem):
        self.items.append(item)
    
    def netto_invoice_sum(self):
        total = 0
        for x in self.items:
            total += x.net_worth_price()
        return total
    def vat_invoice_sum(self):
        total = 0
        for x in self.items:
            total += x.calculate_vat()
        return total
    def brutto_invoice_sum(self):
        total = 0
        for x in self.items:
            total += x.brutto_worth_price()
        return total
    
    def to_dict(self):
        return {
  "invoice_number": self.invoice_number,
  "buyer_name": self.buyer_name,
  "items": [item.to_dict() for item in self.items],
  "net_total": self.netto_invoice_sum(),
  "vat_total": self.vat_invoice_sum(),
  "gross_total": self.brutto_invoice_sum()
}
    def to_json(self):
        with open("invoice.json", "w") as f:
            json.dump(self.to_dict(), f)


    @staticmethod
    def from_json(filename): 
        with open(filename, "r") as f:
            data = json.load(f)
            invoice = Invoice(data.getValue("invoice_number"), data.getValue("buyer_name"))
            return invoice

    

item1 = InvoiceItem("Laptop", 1, 3000, 0.23)
item2 = InvoiceItem("Mysz", 2, 100, 0.23)

invoice = Invoice("FV/1/2026", "Jan Kowalski")

invoice.add_item(item1)
invoice.add_item(item2)

print(invoice.netto_invoice_sum())
print(invoice.vat_invoice_sum())
print(invoice.brutto_invoice_sum())



print(invoice.to_dict())
invoice.to_json()
invoice.from_json("invoice.json")