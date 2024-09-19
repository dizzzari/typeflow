import tkinter as tk
from tkinter import ttk

def open():
    print("Меню открыто")


ROOT = tk.Tk()
ROOT.title("typeflow")
ROOT.geometry("400x300")  # Задаем размеры окна

MAIN_menu = ttk.Frame(ROOT)
MAIN_menu.pack()

Frame_buttons = ttk.Frame(MAIN_menu)
Frame_buttons.pack()

btn_speedtest = ttk.Button(
    Frame_buttons, text="На скорость", command=open)
btn_speedtest.pack()



ROOT.mainloop()
