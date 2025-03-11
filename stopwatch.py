import tkinter as tk
import time

class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("⏱️ Đồng hồ bấm giờ")

        self.time_elapsed = 0
        self.running = False

        self.label = tk.Label(root, text="00:00:00", font=("Arial", 30))
        self.label.pack(pady=20)

        self.start_button = tk.Button(root, text="▶ Bắt đầu", command=self.start, font=("Arial", 12))
        self.start_button.pack(side="left", padx=10)

        self.stop_button = tk.Button(root, text="⏸ Dừng", command=self.stop, font=("Arial", 12))
        self.stop_button.pack(side="left", padx=10)

        self.reset_button = tk.Button(root, text="🔄 Đặt lại", command=self.reset, font=("Arial", 12))
        self.reset_button.pack(side="left", padx=10)

    def update_time(self):
        if self.running:
            self.time_elapsed += 1
            time_str = time.strftime("%H:%M:%S", time.gmtime(self.time_elapsed))
            self.label.config(text=time_str)
            self.root.after(1000, self.update_time)

    def start(self):
        if not self.running:
            self.running = True
            self.update_time()

    def stop(self):
        self.running = False

    def reset(self):
        self.running = False
        self.time_elapsed = 0
        self.label.config(text="00:00:00")

if __name__ == "__main__":
    root = tk.Tk()
    app = Stopwatch(root)
    root.mainloop()
