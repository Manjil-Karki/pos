from views.app import MyApp
from models.sales import SalesModel
from models.inventory import InventoryModel
from models.purchase import PurchaseModel
from models.udaro import UdaroModel
from controllers.sales import SalesController
from controllers.purchase import PurchaseController
from controllers.dash import DashController
from controllers.inventory import InventoryController

if __name__ == "__main__":
    sales_model = SalesModel()
    inventory_model = InventoryModel()
    purchase_model = PurchaseModel()
    udaro_model = UdaroModel()
    inventory_controller = InventoryController(inventory_model)
    sale_controller = SalesController(sales_model = sales_model, inventory_controller = inventory_controller, view = None)
    purchase_controller = PurchaseController(purchase_model = purchase_model, sales_controller=sale_controller, inventory_controller=inventory_controller, view=None)
    dash_controller = DashController(sale_model=sales_model, inventory_model=inventory_model, purchase_model=purchase_model, udaro_model=udaro_model, view=None)
    app = MyApp(sale_controller, purchase_controller, dash_controller)
    sale_controller.view = app.sales_view
    purchase_controller.view = app.inventory_view
    dash_controller.view = app.dash_view
    app.mainloop()
