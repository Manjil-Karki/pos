import tkinter as tk
from tkinter import ttk

class DashView(ttk.Frame):
    def __init__(self, root, controller):
        super().__init__(root)
        self.controller = controller

        self.button_sales = tk.Button(self, text="Sales", command=self.controller.sales_view)
        self.button_sales.grid(row=0, column=0, padx=10, pady=5)

        self.button_inventory = tk.Button(self, text="Inventory", command=self.controller.inventory_view)
        self.button_inventory.grid(row=0, column=1, padx=10, pady=5)

        self.button_purchase = tk.Button(self, text="Purchase", command=self.controller.purchase_view)
        self.button_purchase.grid(row=0, column=2, padx=10, pady=5)