import tkinter as tk
from time import strftime

def update_time():
    current_time = strftime('%H:%M:%S')
    label.config(text=current_time)
    label.after(1000, update_time)  # cập nhật mỗi 1 giây

root = tk.Tk()
root.title("🕒 Đồng hồ số")
root.geometry("300x150")

label = tk.Label(root, font=("Arial", 48), fg="white", bg="black")
label.pack(expand=True)

update_time()
root.mainloop()
