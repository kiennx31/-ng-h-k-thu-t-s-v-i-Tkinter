import tkinter as tk
from tkinter import filedialog, messagebox

def new_file():
    text_area.delete("1.0", tk.END)

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        text_area.delete("1.0", tk.END)
        text_area.insert(tk.END, content)

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(text_area.get("1.0", tk.END))
        messagebox.showinfo("Lưu file", "💾 Đã lưu thành công!")

root = tk.Tk()
root.title("📝 Tkinter Notepad")
root.geometry("500x400")

# Menu
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Vùng nhập văn bản
text_area = tk.Text(root, wrap="word", font=("Arial", 12))
text_area.pack(expand=True, fill="both")

root.mainloop()
