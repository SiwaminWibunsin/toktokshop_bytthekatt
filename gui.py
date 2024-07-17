import tkinter as tk
from tkinter import messagebox
from bot import run_bot  # ต้องแน่ใจว่า bot.py มีฟังก์ชัน run_bot ที่อัพเดตแล้ว

def start_bot():
    try:
        username = username_entry.get()
        password = password_entry.get()
        product_url = url_entry.get()
        quantity = int(quantity_entry.get())
        basket = basket_entry.get()
        card_number = card_number_entry.get()
        expiry_date = expiry_date_entry.get()
        cvv = cvv_entry.get()
        
        # เรียกใช้ฟังก์ชันหลักเพื่อเริ่มต้นบอท
        run_bot(username, password, product_url, quantity, basket, card_number, expiry_date, cvv)
        messagebox.showinfo("Success", "Bot has successfully completed the task!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

app = tk.Tk()
app.title("TikTok Shop Bot")

# กำหนดขนาดหน้าจอ GUI
app.geometry('500x500')

# ปรับแต่งการจัดเรียงองค์ประกอบ
tk.Label(app, text="Username").grid(row=0, column=0, padx=10, pady=5, sticky='w')
tk.Label(app, text="Password").grid(row=1, column=0, padx=10, pady=5, sticky='w')
tk.Label(app, text="Product URL").grid(row=2, column=0, padx=10, pady=5, sticky='w')
tk.Label(app, text="Quantity").grid(row=3, column=0, padx=10, pady=5, sticky='w')
tk.Label(app, text="Basket").grid(row=4, column=0, padx=10, pady=5, sticky='w')
tk.Label(app, text="Card Number").grid(row=5, column=0, padx=10, pady=5, sticky='w')
tk.Label(app, text="Expiry Date").grid(row=6, column=0, padx=10, pady=5, sticky='w')
tk.Label(app, text="CVV").grid(row=7, column=0, padx=10, pady=5, sticky='w')

username_entry = tk.Entry(app)
password_entry = tk.Entry(app, show="*")
url_entry = tk.Entry(app)
quantity_entry = tk.Entry(app)
basket_entry = tk.Entry(app)
card_number_entry = tk.Entry(app)
expiry_date_entry = tk.Entry(app)
cvv_entry = tk.Entry(app)

username_entry.grid(row=0, column=1, padx=10, pady=5)
password_entry.grid(row=1, column=1, padx=10, pady=5)
url_entry.grid(row=2, column=1, padx=10, pady=5)
quantity_entry.grid(row=3, column=1, padx=10, pady=5)
basket_entry.grid(row=4, column=1, padx=10, pady=5)
card_number_entry.grid(row=5, column=1, padx=10, pady=5)
expiry_date_entry.grid(row=6, column=1, padx=10, pady=5)
cvv_entry.grid(row=7, column=1, padx=10, pady=5)

tk.Button(app, text='Start Bot', command=start_bot).grid(row=8, column=1, pady=10)

app.mainloop()
