import tkinter as tk
from tkinter import ttk, messagebox


class PurchaseView(ttk.Frame):
    def __init__(self, root, controller):
        super().__init__(root)

        
        self.controller = controller

        self.label_product = tk.Label(self, text="Product:")
        self.label_product.grid(row=0, column=0, padx=10, pady=5)

        self.entry_product = tk.Entry(self)
        self.entry_product.grid(row=0, column=1, padx=10, pady=5)

        self.label_quantity = tk.Label(self, text="Quantity(Sacks):")
        self.label_quantity.grid(row=0, column=2, padx=10, pady=5)

        self.entry_quantity = tk.Entry(self)
        self.entry_quantity.grid(row=0, column=3, padx=10, pady=5)

        self.label_kgpersack = tk.Label(self, text="Kgs/sack:")
        self.label_kgpersack.grid(row=0, column=4, padx=10, pady=5)

        self.entry_kgpersack = tk.Entry(self)
        self.entry_kgpersack.grid(row=0, column=5, padx=10, pady=5)

        self.label_costpsack = tk.Label(self, text="cost/sack(NRs):")
        self.label_costpsack.grid(row=1, column=1, padx=10, pady=5)

        self.entry_costpsack = tk.Entry(self)
        self.entry_costpsack.grid(row=1, column=2, padx=10, pady=5)

        self.label_sp = tk.Label(self, text="Selling rate/kg(NRs):")
        self.label_sp.grid(row=1, column=3, padx=10, pady=5)

        self.entry_sp = tk.Entry(self)
        self.entry_sp.grid(row=1, column=4, padx=10, pady=5)
    

        self.label_total = tk.Label(self, text="Cost (NRs):")
        self.label_total.grid(row=2, column=2, padx=10, pady=5)
        
        self.text_total = tk.Label(self, text='0.0')
        self.text_total.grid(row=2, column=3, padx=10, pady=5)


        self.button_verify = tk.Button(self, text="Calculate and Verify", command=self.controller.verify_cart)
        self.button_verify.grid(row=3, column=2, padx=10, pady=5)

        self.button_checkout = tk.Button(self, text="Add", state=tk.DISABLED, command=self.controller.checkout)
        self.button_checkout.grid(row=3, column=3, padx=10, pady=5)

    def show_warning(self, message):
        messagebox.showwarning("Warning", message)
   

    def verify(self):
        total = float(self.entry_quantity.get()) * float(self.entry_costpsack.get())
        self.text_total.config(text=total)
        self.button_checkout.config(state = tk.NORMAL)

    def get_product_details(self):
        details = [None] * 6
        details[1] = self.entry_product.get().upper()
        details[2] = self.entry_quantity.get()
        details[3] = self.entry_kgpersack.get()
        details[4] = self.entry_costpsack.get()
        details[5] = self.entry_sp.get()
        return details

    def checkout(self):
        self.entry_product.delete(0, tk.END)
        self.entry_quantity.delete(0, tk.END)
        self.entry_kgpersack.delete(0, tk.END)
        self.entry_costpsack.delete(0, tk.END)
        self.entry_sp.delete(0, tk.END)
        self.text_total.config(text="0.0")
        self.button_checkout.config(state = tk.DISABLED)

    def show_checkout_details(self, summary):
        messagebox.showinfo("Checkout", f"Product: {summary[0]}\nQunatity: {summary[1]} sacks")
