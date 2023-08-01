import tkinter as tk
from tkinter import ttk, Frame, Toplevel

class DashView(ttk.Frame):
    def __init__(self, root, controller):
        super().__init__(root)
        self.controller = controller
        self.view_flag = None

        self.edit_widget_list = list()

        self.button_sales = tk.Button(self, text="Sales", command=self.controller.sales_view)
        self.button_sales.grid(row=0, column=1, padx=10, pady=5)

        self.button_inventory = tk.Button(self, text="Inventory", command=self.controller.inventory_view)
        self.button_inventory.grid(row=0, column=2, padx=10, pady=5)

        self.button_purchase = tk.Button(self, text="Purchase", command=self.controller.purchase_view)
        self.button_purchase.grid(row=0, column=3, padx=10, pady=5)

        self.button_edit = tk.Button(self, text="Edit", command=self.create_edit_window)
        self.button_edit.grid(row=0, column=4, padx=10, pady=5)


        self.tree_frame = ttk.Frame(self)
        self.tree_frame.grid(row = 1, columnspan = 6, padx=10, pady=5)
        self.treeview = ttk.Treeview(self.tree_frame, columns = [])

        self.create_treeview(cols = [], data = [])

        
    def create_treeview(self, cols, data):
        self.treeview.destroy()

        self.treeview = ttk.Treeview(self.tree_frame, columns = cols)
        self.treeview.pack(expand=True, fill=tk.BOTH)

        self.treeview.heading("#0", text="ID")
        self.treeview.column("#0",minwidth=30, width = 30)
        self.cur_cols = cols
        for i in range(len(cols)):
            col_width = len(cols[i]) * 10
            if i == 0 or i == len(cols) - 1:
                col_width = 150
            self.treeview.heading(cols[i], text=cols[i])
            self.treeview.column(cols[i], minwidth = col_width, width=col_width)

        for d in data:
            self.treeview.insert("", "end", text=d[0], values=d[1:])


    def create_edit_window(self):
        item, values, flag = self.get_selected_item()

        if not values:
            return
        values = iter(values)
        self.edit_window = Toplevel(self)
        self.edit_window.title(flag)
        self.edit_window.grab_set()
        self.edit_window.transient(self)

        self.edit_widget_list = list()

        i = 0       


        for col in self.cur_cols:
        
            edit_widget = tk.Label(self.edit_window, text=col)
            edit_widget.grid(row=i, column=0, padx=10, pady=5)

            self.edit_widget_list.append(edit_widget)
            

            edit_widget = tk.Entry(self.edit_window)
            edit_widget.insert(0, next(values))
            if i == 0:
                edit_widget.config(state='readonly')

            edit_widget.grid(row=i, column=1, padx=10, pady=5)

            self.edit_widget_list.append(edit_widget)


            i += 2

        self.edit_widget_list[-1].config(state = 'readonly')
        button_cancel = tk.Button(self.edit_window, text="cancel", command=self.cancel_update)
        button_cancel.grid(row=i, column=0, padx=10, pady=5)

        button_update = tk.Button(self.edit_window, text="update", command=self.perform_update)
        button_update.grid(row=i, column=1, padx=10, pady=5)

        
    def get_selected_item(self):
        curItem = self.treeview.focus()
        values = self.treeview.item(curItem, 'values')
        return curItem, values, self.view_flag
    

    def cancel_update(self):
        self.edit_window.destroy()

    def perform_update(self):
        self.updated_values = [w.get() for w in self.edit_widget_list[1:-1:2]]
        self.controller.perform_update(self.cur_cols, self.updated_values, self.view_flag)
        self.edit_window.destroy()