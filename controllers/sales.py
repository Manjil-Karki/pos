from datetime import datetime
from controllers.udaro import UdaroController

class SalesController:
    def __init__(self, sales_model, inventory_controller, view):
        
        self.sales_model = sales_model
        self.inventory_controller = inventory_controller
        self.view = view
        self.udaro_controller = UdaroController()


    def get_products(self):
        return self.inventory_controller.get_products()

    def add_to_cart(self):
        product = self.view.get_product()
        quantity = self.view.get_quantity()
        if product and quantity:
            rate = self.inventory_controller.get_rate(product)
            amount = float(quantity) * rate
            item = f"{product} : {quantity} X {rate} = {amount}"
            self.view.update_total(amount)
            self.view.add_item_to_cart(item)
            self.view.clear_inputs()
        else:
            self.view.show_warning("Please enter product and quantity.")

    def store_sales(self, items, buyer, discount, paid):
        
        record = [None] * 9       
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
            self.inventory_controller.update_sales_inventory([product, float(quantity)])
        
        record[0] = datetime.now().strftime("20%y/%m/%d %H:%M:%S")
        record[1] = ', '.join(products)
        record[2] = buyer
        record[3] = ', '.join(quantities)
        record[4] = ', '.join(rates)
        record[5] = total
        record[6] = discount
        record[7] = paid
        record[8] = total - paid - discount if total > paid + discount else 0

        print(record)
        
        self.sales_model.add_sale(record)
        

        rtrn = paid + discount - total if paid > total + discount else 0
        remaining = total - paid - discount if total > paid + discount else 0

        if remaining > 0:
            self.udaro_controller.add_update_udaro(record)

        return [total, discount, paid, rtrn, remaining]


    def checkout(self):
        items = self.view.cart_listbox.get(0, self.view.get_tkend())
        buyer = self.view.entry_buyer.get().upper()
        paid_amt = self.view.entry_paid.get()
        discount = self.view.entry_discount.get()
        discount = float(discount) if discount else 0


        if buyer:
            if paid_amt:
                if items:
                    summary = self.store_sales(items, buyer, discount , paid_amt)
                    self.view.show_checkout_details(summary)
                    self.view.clear_cart()
                else:
                    self.view.show_warning("Cart is empty.")
            else:
                self.view.show_warning("Enter paid Amount.\nEnter 0 for credit buy")
        else:
            self.view.show_warning("Enter Buyer's Name")


    def recreate_optionmenu(self):
        self.view.recreate_optionMenu()

if __name__ == "__main__":
    controller = SalesController()
