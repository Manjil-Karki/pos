class DashController:
    def __init__(self, sale_model, inventory_model, purchase_model, view):
        self.sale_model = sale_model
        self.inventory_model = inventory_model
        self.purchase_model = purchase_model
        self.view = view

    def sales_view(self):
        cols = self.sale_model.get_colnames()
        data = self.sale_model.get_allsales()
        self.view.create_treeview(cols, data)


    def inventory_view(self):
        cols = self.inventory_model.get_colnames()
        data = self.inventory_model.get_allproducts()
        self.view.create_treeview(cols, data)

    def purchase_view(self):
        cols = self.purchase_model.get_colnames()
        data = self.purchase_model.get_allpurchases()
        self.view.create_treeview(cols, data)