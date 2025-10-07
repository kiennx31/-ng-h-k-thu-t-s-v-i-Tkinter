import tkinter as tk
from tkinter import messagebox
import time
import threading

def start_timer():
    try:
        total_seconds = int(entry_min.get()) * 60 + int(entry_sec.get())
        if total_seconds <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Lỗi", "⛔ Vui lòng nhập số phút/giây hợp lệ!")
        return

    def countdown():
        remaining = total_seconds
        while remaining > 0:
            mins, secs = divmod(remaining, 60)
            label_time.config(text=f"{mins:02d}:{secs:02d}")
            time.sleep(1)
            remaining -= 1
        label_time.config(text="00:00")
        messagebox.showinfo("Hoàn tất!", "⏰ Hết giờ rồi!")

    thread = threading.Thread(target=countdown)
    thread.daemon = True
    thread.start()

# Tạo cửa sổ chính
root = tk.Tk()
root.title("⏳ Countdown Timer")
root.geometry("300x250")
root.resizable(False, False)

# Giao diện
tk.Label(root, text="Phút:").pack()
entry_min = tk.Entry(root, width=5, justify="center")
entry_min.pack()

tk.Label(root, text="Giây:").pack()
entry_sec = tk.Entry(root, width=5, justify="center")
entry_sec.pack()

label_time = tk.Label(root, text="00:00", font=("Arial", 32, "bold"))
label_time.pack(pady=20)

tk.Button(root, text="▶️ Bắt đầu", command=start_timer, bg="green", fg="white").pack()

root.mainloop()
