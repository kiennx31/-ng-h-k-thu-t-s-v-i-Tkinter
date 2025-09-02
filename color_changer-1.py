import tkinter as tk
from tkinter import ttk

def change_color(event=None):
    selected = color_var.get()
    root.configure(bg=selected)

root = tk.Tk()
root.title("🎨 Color Changer")
root.geometry("300x200")

# Biến lưu màu
color_var = tk.StringVar(value="white")

# Danh sách màu
colors = ["white", "lightblue", "lightgreen", "pink", "yellow", "gray"]

label = tk.Label(root, text="Chọn màu nền:", font=("Arial", 14))
label.pack(pady=10)

combo = ttk.Combobox(root, textvariable=color_var, values=colors, state="readonly")
combo.pack(pady=5)
combo.bind("<<ComboboxSelected>>", change_color)

# Nút đổi màu
btn = tk.Button(root, text="Đổi màu", command=change_color)
btn.pack(pady=10)

root.mainloop()
