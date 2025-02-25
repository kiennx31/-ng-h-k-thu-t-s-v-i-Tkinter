import tkinter as tk
from time import strftime

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Đồng Hồ Kỹ Thuật Số")

# Thiết lập giao diện
root.configure(bg="black")

# Label hiển thị thời gian
time_label = tk.Label(root, font=("Arial", 50, "bold"), fg="cyan", bg="black")
time_label.pack(pady=20)

# Label hiển thị ngày
date_label = tk.Label(root, font=("Arial", 20), fg="white", bg="black")
date_label.pack()

# Hàm cập nhật thời gian
def update_time():
    current_time = strftime("%H:%M:%S")
    current_date = strftime("%A, %d %B %Y")  # Thứ, ngày tháng năm
    time_label.config(text=current_time)
    date_label.config(text=current_date)
    root.after(1000, update_time)  # Cập nhật mỗi giây

# Bắt đầu cập nhật thời gian
update_time()

# Chạy chương trình
root.mainloop()
