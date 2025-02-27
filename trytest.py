from tkinter import *
from tkinter import messagebox
import time
import keyboard
import mouse

window = Tk()
window.geometry("500x300")
window.title("Auto Clicker")
window.config(bg="#def6fa")
running = False
delay = 0


def exit_app():
    global running
    running = False
    messagebox.showinfo("Auto Clicker", "Auto Clicker зупинено.")
    window.destroy()  # Закриття вікна Tkinter


def start_clicker():
    global running, delay  # "знаходимо" змінні, що існують поза функцією
    clicks_per_second = int(entry.get())
    delay = 1 / clicks_per_second  # рахуємо затримку між кліками
    messagebox.showinfo("Auto Clicker", "Auto Clicker розпочинає роботу.")
    running = True
    # Запуск процесу кліків
    schedule_click()


def schedule_click():
    if running:
        mouse.click()  # тут потім додамо клацання миші замість print
        time.sleep(delay)  # затримка між кліками


def show_info(event):
    messagebox.showinfo("Інформація", "Це автоклікер, він буде клікати мишкою зі швидкістю, яку ти вкажеш!")

def on_label_click(event):
    print("Клікнуто лівою кнопкою миші!")


Label(window, font=("", 24), text="Auto Clicker", bg="#def6fa", pady=10, fg="#027870").place(relx=0.5, rely=0.1,
                                                                                             anchor="center")
Label(window, font=("", 14), text="Кліків на секунду:", bg="#def6fa", pady=10, fg="#027870").place(relx=0.5, rely=0.25,
                                                                                                   anchor="center")
entry = Entry(window, font=("", 16))
entry.place(relx=0.5, rely=0.3125, anchor="n")
Button(window, bg="#68d164", activebackground="#1d691a", text="Почати", fg="white", command=start_clicker).place(
    relx=0.4, rely=0.5, anchor="center")
Button(window, bg="#f56042", activebackground="#69271a", text="Вийти", fg="white",
       command=lambda: window.destroy()).place(relx=0.6, rely=0.5, anchor="center")


leftclick = Label(window, text="Клікни сюди", font=("Arial 16 bold"), bg="#87ceeb", padx=20, pady=10)
leftclick.place(relx=0.5, rely=0.7, anchor="center")

leftclick.bind("<Button-1>", on_label_click)
window.bind("i", show_info)
keyboard.add_hotkey('esc', exit_app)
window.mainloop()