import customtkinter as ctk
from random import randint
import time


class App:
    rand = str(randint(1, 3))

    def __init__(self, master: ctk.CTk):
        self.master = master
        self.master.geometry('250x250')
        self.master.resizable(False, False)
        self.master.wm_title('Guess the Number')

        self.button = ctk.CTkButton(self.master, text='Начнём игру', command=self.start, corner_radius=20)
        self.button.place(relx=0.5, rely=0.2, anchor='center')

    def start(self):
        self.enter = ctk.CTkEntry(self.master, placeholder_text='введите число', corner_radius=20)
        self.enter.place(relx=0.5, rely=0.4, anchor='center')
        self.button_check = ctk.CTkButton(self.master, text='проверить', corner_radius=20, bg_color='green',
                                          command=self.check)
        self.button_check.place(relx=0.5, rely=0.6, anchor='center')

    def check(self):
        num = self.enter.get()
        print(num)
        print(App.rand, 'App rand', type(App.rand))
        print(num, 'App num', type(num))
        self.enter.delete(0, 2)
        try:
            if num == App.rand:
                self.finish = ctk.CTkLabel(self.master, text='Вы угадали', fg_color='green')
                self.finish.place(relx=0.5, rely=0.06, anchor='center')
            else:
                self.finish = ctk.CTkLabel(self.master, text='Вы не угадали', fg_color='green')
                self.finish.place(relx=0.5, rely=0.8, anchor='center')
                self.finish.bell()
                time.sleep(2)
        except Exception as e:
            print(f'{e}')

    def destroy(self):
        self.finish.destroy()


if __name__ == '__main__':
    app = ctk.CTk()
    gui = App(master=app)
    app.mainloop()
