import tkinter as tk

def click(event):
    current = display.get()
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(current)
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        except:
            display.delete(0, tk.END)
            display.insert(tk.END, "Lỗi")
    elif text == "C":
        display.delete(0, tk.END)
    else:
        display.insert(tk.END, text)

root = tk.Tk()
root.title("🧮 Máy tính đơn giản")

# Hiển thị kết quả
display = tk.Entry(root, font="Arial 20", bd=10, relief=tk.RIDGE, justify='right')
display.pack(fill=tk.BOTH, padx=10, pady=10)

# Các nút bấm
button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", "C", "=", "+"
]

row = 0
col = 0
for btn_text in buttons:
    btn = tk.Button(button_frame, text=btn_text, font="Arial 18", width=5, height=2)
    btn.grid(row=row, column=col, padx=5, pady=5)
    btn.bind("<Button-1>", click)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
