from views.app import MyApp
from models.sales import SalesModel
from models.inventory import InventoryModel
from models.purchase import PurchaseModel
from controllers.sales import SalesController
from controllers.purchase import PurchaseController
from controllers.dash import DashController


if __name__ == "__main__":
    sales_model = SalesModel()
    inventory_model = InventoryModel()
    purchase_model = PurchaseModel()
    sale_controller = SalesController(sales_model = sales_model, inventory_model = inventory_model, view = None)
    purchase_controller = PurchaseController(purchase_model = purchase_model, view=None)
    dash_controller = DashController(sale_model=sales_model, inventory_model=inventory_model, purchase_model=purchase_model, view=None)
    app = MyApp(sale_controller, purchase_controller, dash_controller)
    sale_controller.view = app.sales_view
    purchase_controller.view = app.inventory_view
    dash_controller.view = app.dash_view
    app.mainloop()
