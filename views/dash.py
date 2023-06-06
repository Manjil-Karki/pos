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


        self.tree_frame = ttk.Frame(self)
        self.tree_frame.grid(row = 1, columnspan = 3, padx=10, pady=5)
        self.treeview = ttk.Treeview(self.tree_frame, columns = [])
        self.create_treeview(cols = [], data = [])
    
    def create_treeview(self, cols, data):
        self.treeview.destroy()
        self.treeview = ttk.Treeview(self.tree_frame, columns = cols)
        self.treeview.pack()

        self.treeview.heading("#0", text="ID")
        self.treeview.column("#0", stretch="NO")
        for col in cols:
            self.treeview.heading(col, text=col)
            self.treeview.column(col, stretch="NO")

        for d in data:
            self.treeview.insert("", "end", text=d[0], values=d[1:])
        # treeview.heading("Name", text="Name")
        # treeview.heading("Age", text="Age")