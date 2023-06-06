import tkinter as tk
from tkinter import ttk
from views.sales import SalesView
from views.purchase import PurchaseView
from views.dash import DashView

class MyApp(tk.Tk):
    def __init__(self, sale_controller, purchase_controller, dash_controller):
        super().__init__()
        self.title("POS")
        self.notebook = ttk.Notebook(self)

        # Sales
        tab1 = ttk.Frame(self.notebook)
        self.notebook.add(tab1, text="Sales")
        self.sales_view = SalesView(tab1, sale_controller)
        self.sales_view.pack()

        # Create the second tab with nested tabs
        tab2 = ttk.Frame(self.notebook)
        self.notebook.add(tab2, text="Dashboard")
        self.dash_view = DashView(tab2, dash_controller)
        self.dash_view.pack()

        # Create the third tab
        tab3 = ttk.Frame(self.notebook)
        self.notebook.add(tab3, text="Inventory")
        self.inventory_view = PurchaseView(tab3, purchase_controller)
        self.inventory_view.pack()

        self.notebook.pack(padx=10, pady=10)
