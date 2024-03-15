'''Разработайте программу, которая отображает случайное
слово на английском языке (из заранее созданного словаря). Пользователь
вводит перевод этого слова. Интерфейс программы:'''
import tkinter as tk
import random
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Случайное слово")
        self.pack()
        self.create_widgets()
    def create_widgets(self):
        self.word = tk.Label(self)
        self.word["text"] = random.choice(words)
        self.word.pack(side="top")
        self.answer = tk.Entry(self)
        self.answer.pack(side="top")
        self.check = tk.Button(self)
        self.check["text"] = "Проверить"
        self.check["command"] = self.check_answer
        self.check.pack(side="left")

        self.quit = tk.Button(self, text="Выход", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="right")
    def check_answer(self):
        if self.answer.get() == translations[self.word["text"]]:
            self.word["text"] = random.choice(words)
            self.answer.delete(0, tk.END)
            result_label.config(text="Правильно!")
            result_label.config(fg="green")
        else:
            result_label.config(text="Неправильно!")
            result_label.config(fg="red")
words = ["apple", "banana", "cherry", "math", "star"]
translations = {"apple": "яблоко", "banana": "банан", "cherry": "вишня",
                "math": "математика", "star": "звезда"}
root = tk.Tk()
app = Application(master=root)
result_label = tk.Label(root, text="")
result_label.pack()
app.mainloop()
