import tkinter as tk
from tkinter import ttk, messagebox

class SalesView(ttk.Frame):
    def __init__(self, root, controller):
        super().__init__(root)

        self.controller = controller

        self.variable = tk.StringVar(self)
        
        self.label_product = tk.Label(self, text="Product:")
        self.label_product.grid(row=0, column=0, padx=10, pady=5)

        self.entry_product = tk.OptionMenu(self, self.variable, *self.controller.get_products())
        self.entry_product.config(width=5)
        self.entry_product.grid(row=0, column=1, columnspan=1, padx=10, pady=5)

        self.label_quantity = tk.Label(self, text="Quantity(KGs):")
        self.label_quantity.grid(row=0, column=2, padx=10, pady=5)

        self.entry_quantity = tk.Entry(self)
        self.entry_quantity.grid(row=0, column=3, padx=10, pady=5)

        self.button_add = tk.Button(self, text="Add", command=self.controller.add_to_cart)
        self.button_add.grid(row=0, column=4, padx=10, pady=5)

        self.cart_listbox = tk.Listbox(self)
        self.cart_listbox.grid(row=1, column = 0, columnspan=3, rowspan=4, padx=10, pady=5)

        self.label_total = tk.Label(self, text="Total(NRs):")
        self.label_total.grid(row=1, column=3, padx=10, pady=5)
        
        self.text_total = tk.Label(self, text='0.0')
        self.text_total.grid(row=1, column=4, padx=10, pady=5)

        self.label_discount = tk.Label(self, text="Discount(NRs):")
        self.label_discount.grid(row=2, column=3, padx=10, pady=5)
        
        self.entry_discount = tk.Entry(self)
        self.entry_discount.grid(row=2, column=4, padx=10, pady=5)

        self.label_buyer = tk.Label(self, text="Buyer's Name:")
        self.label_buyer.grid(row=3, column=3, padx=10, pady=5)

        self.entry_buyer = tk.Entry(self)
        self.entry_buyer.grid(row=3, column=4, padx=10, pady=5)

        self.label_paid = tk.Label(self, text="Paid Amount(NRs):")
        self.label_paid.grid(row=4, column=3, padx=10, pady=5)

        self.entry_paid = tk.Entry(self)
        self.entry_paid.grid(row=4, column=4, padx=10, pady=5)

        self.button_clear = tk.Button(self, text="clear", command=self.clear_cart)
        self.button_clear.grid(row=5, column=1, padx=10, pady=5)

        self.button_checkout = tk.Button(self, text="Checkout", command=self.controller.checkout)
        self.button_checkout.grid(row=5, column=4, padx=10, pady=5)


    def recreate_optionMenu(self):
        self.entry_product.destroy()
        self.entry_product = tk.OptionMenu(self, self.variable, *self.controller.get_products())
        self.entry_product.config(width=5)
        self.entry_product.grid(row=0, column=1, columnspan=1, padx=10, pady=5)

    def update_total(self, new_amt):
        prev_total = float(self.text_total.cget('text'))
        total = prev_total + new_amt
        self.text_total.config(text=total)

    def get_product(self):
        return self.variable.get()

    def get_quantity(self):
        return self.entry_quantity.get()

    def get_tkend(self):
        return tk.END

    def add_item_to_cart(self, item):
        self.cart_listbox.insert(tk.END, item)

    def clear_inputs(self):
        self.variable.set("")
        self.entry_quantity.delete(0, tk.END)

    def show_warning(self, message):
        messagebox.showwarning("Warning", message)

    def show_checkout_details(self, summary):
        messagebox.showinfo("Checkout", f"Total: Rs{summary[0]:.2f}\nDiscount: Rs{summary[1]:.2f}\nPaid: Rs{summary[2]:.2f}\nReturn: Rs{summary[3]:.2f}\nRemaining: Rs{summary[4]:.2f}")

    def clear_cart(self):
        self.text_total.config(text="0.0")
        self.cart_listbox.delete(0, tk.END)
        self.entry_buyer.delete(0, tk.END)
        self.entry_discount.delete(0, tk.END)
        self.entry_paid.delete(0, tk.END)


if __name__ == "__main__":
    pass