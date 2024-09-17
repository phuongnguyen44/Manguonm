import tkinter as tk
from tkinter import messagebox
import numpy as np
import pandas as pd
from IPython.display import display

def get_matrix():
    matrix = []
    matrix_1x3 = []
    try:
        for i in range(5):
            row = [int(entries[i][j].get()) for j in range(3)]
            matrix.append(row)
        for j in range(3):
            matrix_1x3.append(float(entries_1x3[j].get()))
        sales_amount=matrix #So luong cac loai qua ban duoc trong tuan
        weekly_sales = pd.DataFrame(sales_amount,index=["Mon","Tue","Wed","Thurs","Fri"],
                            columns=["Táo","Chuối","Dưa hấu"])
        display(weekly_sales)
        prices=np.array(matrix_1x3)
        table_prices=pd.DataFrame(prices.reshape(1,3),index=["Price"],columns=["Táo","Chuối","Dưa hấu"])
        display(table_prices)
        total_price=weekly_sales.dot(table_prices.T)
        display(total_price)

    
      
        
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập các số nguyên hợp lệ.")

root = tk.Tk()
root.title("Nhập số lượng cua các loại quả")


# Tạo lưới nhập dữ liệu
entries = []
for i in range(5):
    row_entries = []
    for j in range(3):
        entry = tk.Entry(root, width=10)
        entry.grid(row=i, column=j)
        row_entries.append(entry)
    entries.append(row_entries)
tk.Label(root, text="Nhập giá : ").grid(row=6, column=0, columnspan=3)
entries_1x3 = []
for j in range(3):
    entry = tk.Entry(root, width=10)
    entry.grid(row=7, column=j)
    entries_1x3.append(entry)

# Nút để lấy dữ liệu từ ma trận
submit_button = tk.Button(root, text="Lấy Ma Trận", command=get_matrix)

submit_button.grid(row=8, column=0, columnspan=3)

root.mainloop()