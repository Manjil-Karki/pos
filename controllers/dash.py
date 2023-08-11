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
        self.view.view_flag = 0



    def inventory_view(self):
        cols = self.inventory_model.get_colnames()
        data = self.inventory_model.get_allproducts()
        self.view.create_treeview(cols, data)
        self.view.view_flag = 1


    def purchase_view(self):
        cols = self.purchase_model.get_colnames()
        data = self.purchase_model.get_allpurchases()
        self.view.create_treeview(cols, data)
        self.view.view_flag = 2


    def udharo_view(self):
        cols, data = self.sale_model.get_udaro_data()
        self.view.create_treeview(cols, data)
        self.view.view_flag = 3


    def perform_update(self, cols, values, table):
        
        if table == 0:
            # which means sales table
            self.sale_model.update_by_date(values)
            self.sales_view()
        elif table == 1:
            # which means inventory table
            self.inventory_model.update_by_name(values)
            self.inventory_view()
        elif table == 2:
            # purchase table
            self.purchase_model.update_by_date(values)
            
            self.purchase_view()
        else:
            print("error")
        print(cols, values, table)



    def delete_record(self, record, table):
        if table == 0:
            # which means sales table
            self.sale_model.delete_by_date(record[0])
            self.sales_view()
        elif table == 1:
            # which means inventory table
            self.inventory_model.delete_by_name(record[0])
            self.inventory_view()
        elif table == 2:
            # purchase table
            a = self.purchase_model.delete_by_date(record[0])
            if a:
                self.inventory_model.update_deleted(record[1], float(record[2])*float(record[3]))
            self.purchase_view()
        else:
            print("error")
