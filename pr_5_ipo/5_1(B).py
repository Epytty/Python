'''Просмотр рисунков'''

import tkinter as tk
from PIL import ImageTk, Image

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x500")
        self.root.title("Просмотр рисунков")
        self.options = ["Центр", "Справа", "Слева"]
        self.var = tk.StringVar(self.root)
        self.var.set(self.options[0])
        self.menu = tk.OptionMenu(self.root, self.var, *self.options)
        self.menu.pack()
        self.images = [
            ImageTk.PhotoImage(Image.open("image1.jpg")),
            ImageTk.PhotoImage(Image.open("image2.jpg")),
            ImageTk.PhotoImage(Image.open("image3.jpg")),
            ImageTk.PhotoImage(Image.open("image4.jpg")),
            ImageTk.PhotoImage(Image.open("image5.jpg"))
        ]
        for i in range(len(self.images)):
            button = tk.Button(self.root, image=self.images[i], command=lambda i=i: self.show_image(i))
            button.pack(side=tk.TOP)
    def show_image(self, index):
        if self.var.get() == "Центр":
            x = (self.root.winfo_width() - self.images[index].width()) // 2
            y = (self.root.winfo_height() - self.images[index].height()) // 2
        elif self.var.get() == "Справа":
            x = self.root.winfo_width() - self.images[index].width()
            y = (self.root.winfo_height() - self.images[index].height()) // 2
        elif self.var.get() == "Слева":
            x = 0
            y = (self.root.winfo_height() - self.images[index].height()) // 2
        top = tk.Toplevel(self.root)
        top.geometry(f"{self.images[index].width()}x{self.images[index].height()}+{x}+{y}")
        top.title(f"Рисунок {index + 1}")
        label = tk.Label(top, image=self.images[index])
        label.pack()
    def run(self):
        self.root.mainloop()
app = App()
app.run()