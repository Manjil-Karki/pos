from datetime import datetime

class SalesController:
    def __init__(self, sales_model, inventory_model, view):
        
        self.sales_model = sales_model
        self.inventory_model = inventory_model
        self.products = self.inventory_model.get_product_names()
        self.view = view


    def add_to_cart(self):
        product = self.view.get_product()
        quantity = self.view.get_quantity()
        if product and quantity:
            rate = self.inventory_model.get_product_rate(product)
            amount = float(quantity) * rate
            item = f"{product} : {quantity} X {rate} = {amount}"
            self.view.update_total(amount)
            self.view.add_item_to_cart(item)
            self.view.clear_inputs()
        else:
            self.view.show_warning("Please enter product and quantity.")

    def store_sales(self, items, buyer, paid):
        
        record = [None] * 8       
        total = 0
        products = []
        quantities = []
        rates = []

        paid = float(paid)

        for item in items:
            product, item = item.split(" : ")
            products.append(product) 
            quantity, item = item.split(" X ")
            quantities.append(quantity)
            rate, amount = item.split(" = ")
            rates.append(rate)
            amount = float(rate) * float(quantity)
            total += float(amount)
        
        record[0] = datetime.now().strftime("20%y/%m/%d %H:%M:%S")
        record[1] = ', '.join(products)
        record[2] = buyer
        record[3] = ', '.join(quantities)
        record[4] = ', '.join(rates)
        record[5] = total
        record[6] = paid
        record[7] = total - paid if total > paid else 0

        print(record)
        self.sales_model.add_sale(record)

        rtrn = paid - total if paid > total else 0
        remaining = total - paid if total > paid else 0

        return [total, paid, rtrn, remaining]


    def checkout(self):
        items = self.view.cart_listbox.get(0, self.view.get_tkend())
        buyer = self.view.entry_buyer.get()
        paid_amt = self.view.entry_paid.get()

        if buyer:
            if paid_amt:
                if items:
                    summary = self.store_sales(items, buyer, paid_amt)
                    self.view.show_checkout_details(summary)
                    self.view.clear_cart()
                else:
                    self.view.show_warning("Cart is empty.")
            else:
                self.view.show_warning("Enter paid Amount.\nEnter 0 for credit buy")
        else:
            self.view.show_warning("Enter Buyer's Name")



if __name__ == "__main__":
    controller = SalesController()
