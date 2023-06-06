from datetime import datetime
from controllers.inventory import InventoryController


class PurchaseController:
    def __init__(self, view, purchase_model):
        self.view = view
        self.model = purchase_model
        self.inventory = InventoryController()

    def verify_cart(self):
        if not (self.view.entry_quantity.get() and self.view.entry_costpsack.get()):
            self.view.show_warning("Please Fill every field properly")
        self.view.verify()

    def checkout(self):
        details = self.view.get_product_details()
        details[0] = datetime.now().strftime("20%y/%m/%d %H:%M:%S")
        if '' in details:
            self.view.show_warning("Donot leave any field empty Re-enter.")
            return
        for i in range(len(details)):
            if i > 1:
                details[i] = float(details[i])
        self.model.add_purchase(details)
        self.inventory.update_inventory(details)
        self.view.show_checkout_details(details[1:3])
        self.view.checkout()


    