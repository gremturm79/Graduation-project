
import tkinter
from random import randint

import customtkinter

customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('green')
app = customtkinter.CTk('red')
app.geometry('380x280')

gen_num = randint(1, 4)


def button():
    global res
    save = enter.get()
    count = 0
    while count != save:
        count += 1
        if res == gen_num:
            final_text = tkinter.StringVar(value='Вы угадали')
            final_text = customtkinter.CTkLabel(master=app, textvariable=final_text, width=200, height=20, fg_color='white')
            final_text.place(relx=0.2, rely=0.4)
        elif res != gen_num:
            final_text = tkinter.StringVar(value='Вы не угадали')
            final_text = customtkinter.CTkLabel(master=app, textvariable=final_text, width=200, height=20, fg_color='white')
            final_text.place(relx=0.2, rely=0.4)

        elif res == count:
            final_text = tkinter.StringVar(value='Вы использовали все попытки')
            final_text = customtkinter.CTkLabel(master=app, textvariable=final_text, width=200, height=20,
                                                fg_color='white')
            final_text.place(relx=0.2, rely=0.4)
        else:
            continue


button1 = customtkinter.CTkButton(master=app, width=200, height=20, text='начать игру')
button1.place(relx=0.45, rely=0.01)
enter = customtkinter.CTkEntry(master=app, width=150, height=20, placeholder_text='напишите кол-во попыток',
                               bg_color='white')
enter.place(relx=0.01, rely=0.01)
num_player_enter = customtkinter.CTkEntry(master=app, width=100, height=20,
                                          placeholder_text='напишите число ',
                                          bg_color='white')
num_player_enter.place(relx=0.1, rely=0.2)
check_value = customtkinter.CTkButton(master=app, width=100, height=20, text='проверить', command=button)
check_value.place(relx=0.45, rely=0.2)
res = num_player_enter.get()
print(res)

app.mainloop()
