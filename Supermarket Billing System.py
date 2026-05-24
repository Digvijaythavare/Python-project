import tkinter as tk
from tkinter import messagebox, scrolledtext, filedialog

# ================== Initialize Main Window ==================
root = tk.Tk()
root.title("SmartCart - Supermarket Billing System")
root.geometry("800x600")
root.config(bg="#f2f2f2")  # light gray background
root.resizable(False, False)

# ================== Data ==================
items_prices = {
    "Apple": 20, "Banana": 10, "Milk": 40, "Bread": 30, "Eggs": 5,
    "Rice": 50, "Sugar": 45, "Oil": 80, "Butter": 60, "Cheese": 90,
    "Tomato": 15, "Potato": 12, "Onion": 18, "Chicken": 200, "Fish": 250,
    "Cereal": 120, "Juice": 50, "Water": 20, "Chocolate": 35, "Snack": 25
}

cart = []

# ================== Functions ==================
def add_item():
    item = item_var.get()
    if item in items_prices:
        cart.append(item)
        update_cart()
    else:
        messagebox.showerror("Error", "Select a valid item!")

def delete_item():
    try:
        selected_index = cart_list.curselection()[0]
        cart.pop(selected_index)
        update_cart()
    except IndexError:
        messagebox.showerror("Error", "Select an item to delete!")

def update_cart():
    cart_list.delete(0, tk.END)
    for i, item in enumerate(cart, 1):
        cart_list.insert(tk.END, f"{i}. {item} - ₹{items_prices[item]}")
    update_total()

def update_total():
    total_price = sum(items_prices[item] for item in cart)
    discount = 0
    if len(cart) >= 20:
        discount = 0.20
    elif len(cart) >= 10:
        discount = 0.15
    discounted_price = total_price * (1 - discount)
    total_label.config(
        text=f"Total Items: {len(cart)}\nTotal Price: ₹{total_price}\nDiscount: {int(discount*100)}%\nFinal Price: ₹{discounted_price:.2f}"
    )

def generate_bill():
    if not cart:
        messagebox.showinfo("Bill", "No items in cart!")
        return
    bill_text = "===== SmartCart Bill =====\n"
    for i, item in enumerate(cart, 1):
        bill_text += f"{i}. {item} - ₹{items_prices[item]}\n"
    total_price = sum(items_prices[item] for item in cart)
    discount = 0
    if len(cart) >= 20:
        discount = 0.20
    elif len(cart) >= 10:
        discount = 0.15
    final_price = total_price * (1 - discount)
    bill_text += f"\nTotal Items: {len(cart)}"
    bill_text += f"\nTotal Price: ₹{total_price}"
    bill_text += f"\nDiscount: {int(discount*100)}%"
    bill_text += f"\nFinal Price: ₹{final_price:.2f}"
    
    # Bill popup
    bill_window = tk.Toplevel(root)
    bill_window.title("Final Bill")
    bill_window.geometry("450x500")
    bill_window.config(bg="#ffffff")
    
    text_area = scrolledtext.ScrolledText(bill_window, width=50, height=30, font=("Courier", 12))
    text_area.pack(pady=10, padx=10)
    text_area.insert(tk.END, bill_text)
    text_area.config(state='disabled')
    
    def save_bill():
        file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file:
            with open(file, 'w') as f:
                f.write(bill_text)
            messagebox.showinfo("Saved", f"Bill saved as {file}")
    
    save_btn = tk.Button(bill_window, text="Save Bill", command=save_bill, bg="#4CAF50", fg="white", font=("Arial", 12))
    save_btn.pack(pady=5)

# ================== GUI Layout ==================

# Header
header_frame = tk.Frame(root, bg="#4CAF50", height=60)
header_frame.pack(fill="x")
header_label = tk.Label(header_frame, text="SmartCart - Supermarket Billing", bg="#4CAF50", fg="white", font=("Arial", 20, "bold"))
header_label.pack(pady=10)

# Main Frame
main_frame = tk.Frame(root, bg="#f2f2f2")
main_frame.pack(fill="both", expand=True, padx=20, pady=10)

# Left Frame - Item Selection
left_frame = tk.Frame(main_frame, bg="#f2f2f2")
left_frame.pack(side="left", fill="y", padx=10)

item_label = tk.Label(left_frame, text="Select Item:", font=("Arial", 12, "bold"), bg="#f2f2f2")
item_label.pack(pady=5)

item_var = tk.StringVar()
item_var.set("Select Item")
item_menu = tk.OptionMenu(left_frame, item_var, *items_prices.keys())
item_menu.config(width=20, font=("Arial", 12))
item_menu.pack(pady=5)

add_btn = tk.Button(left_frame, text="Add Item", width=15, bg="#2196F3", fg="white", font=("Arial", 12), command=add_item)
add_btn.pack(pady=5)
delete_btn = tk.Button(left_frame, text="Delete Item", width=15, bg="#f44336", fg="white", font=("Arial", 12), command=delete_item)
delete_btn.pack(pady=5)

# Right Frame - Cart & Total
right_frame = tk.Frame(main_frame, bg="#f2f2f2")
right_frame.pack(side="right", fill="both", expand=True, padx=10)

cart_label = tk.Label(right_frame, text="Cart:", font=("Arial", 12, "bold"), bg="#f2f2f2")
cart_label.pack(pady=5)

cart_scroll = tk.Scrollbar(right_frame)
cart_scroll.pack(side=tk.RIGHT, fill=tk.Y)

cart_list = tk.Listbox(right_frame, width=40, height=20, yscrollcommand=cart_scroll.set, font=("Arial", 12))
cart_list.pack(pady=5)
cart_scroll.config(command=cart_list.yview)

total_label = tk.Label(right_frame, text="Total Items: 0\nTotal Price: ₹0\nDiscount: 0%\nFinal Price: ₹0", font=("Arial", 12, "bold"), bg="#f2f2f2")
total_label.pack(pady=10)

# Bottom Frame - Generate Bill
bottom_frame = tk.Frame(root, bg="#f2f2f2")
bottom_frame.pack(fill="x", pady=10)
bill_btn = tk.Button(bottom_frame, text="Generate Bill", width=25, height=2, bg="#4CAF50", fg="white", font=("Arial", 14, "bold"), command=generate_bill)
bill_btn.pack()

# ================== Run ==================
root.mainloop()