import tkinter as tk
from time import strftime

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Đồng Hồ Kỹ Thuật Số")
root.configure(bg="black")

# Biến kiểm soát chế độ giờ
is_24_hour = True  

# Hiển thị thời gian
time_label = tk.Label(root, font=("Arial", 50, "bold"), fg="cyan", bg="black")
time_label.pack(pady=20)

# Hiển thị ngày
date_label = tk.Label(root, font=("Arial", 20), fg="white", bg="black")
date_label.pack()

# Hàm cập nhật thời gian
def update_time():
    global is_24_hour
    format_s
