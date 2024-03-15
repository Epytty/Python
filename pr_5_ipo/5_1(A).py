'Калькулятор простых и вещественных чисел'

import tkinter as tk
root = tk.Tk()
root.title("Калькулятор")
entry = tk.Entry(root)
entry.pack()
button = tk.Button(root, text="Вычислить", command=lambda: listbox.insert(tk.END, eval(entry.get())))
button.pack()
listbox = tk.Listbox(root)
listbox.pack()
root.mainloop()