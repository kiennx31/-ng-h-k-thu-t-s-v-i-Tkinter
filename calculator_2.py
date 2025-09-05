import tkinter as tk

def calculate(op):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        if op == "+":
            result.set(num1 + num2)
        elif op == "-":
            result.set(num1 - num2)
        elif op == "*":
            result.set(num1 * num2)
        elif op == "/":
            if num2 != 0:
                result.set(num1 / num2)
            else:
                result.set("⚠️ Lỗi chia 0")
    except ValueError:
        result.set("⚠️ Nhập sai")

root = tk.Tk()
root.title("🧮 Máy tính mini")
root.geometry("300x250")

tk.Label(root, text="Số 1:").pack()
