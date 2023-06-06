from models.inventory import InventoryModel

class InventoryController:
    def __init__(self):
        self.model = InventoryModel()

    def get_products(self):
        return self.model.get_product_names()

    def update_inventory(self, details):
        products = self.get_products()
        if details[1] in products:
            record = self.model.get_product_details(details[1])
            new_record = [None] * 2
            new_record[0] = details[5]
            new_record[1] = record[3] + details[2] * details[3]
            self.model.update_product_details(new_record, record[0])
        else:
            record = [None] * 3
            record[0] = details[1]
            record[1] = details[5]
            record[2] = details[2] * details[3]
            self.model.add_produt_details(record)