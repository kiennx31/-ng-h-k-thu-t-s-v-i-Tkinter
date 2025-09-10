import tkinter as tk
from tkinter import messagebox

def start_countdown():
    try:
        total_seconds = int(entry.get())
        countdown(total_seconds)
    except ValueError:
        messagebox.showerror("Lỗi", "⚠️ Vui lòng nhập số giây hợp lệ")

def countdown(time_left):
    if time_left >= 0:
        mins, secs = divmod(time_left, 60)
        timer_label.config(text=f"{mins:02d}:{secs:02d}")
        root.after(1000, countdown, time_left - 1)
    else:
        messagebox.showinfo("Hết giờ", "⏰ Thời gian đã kết thúc!")

root = tk.Tk()
root.title("⏳ Countdown Timer")
root.geometry("300x200")

tk.Label(root, text="Nhập số giây:", font=("Arial", 12)).pack(pady=10)
entry = tk.Entry(root, font=("Arial", 14), justify="center")
entry.pack(pady=5)

start_btn = tk.Button(root, text="Start", command=start_countdown, font=("Arial", 12))
start_btn.pack(pady=10)

timer_label = tk.Label(root, text="00:00", font=("Arial", 32), fg="red")
timer_label.pack(pady=15)

root.mainloop()
