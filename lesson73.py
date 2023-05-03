import tkinter
from tkinter import filedialog as fd
import customtkinter
import requests
import re

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk('green')  # create CTk window like you do with the Tk window
app.geometry("380x140")


def button_function():
    global enter, r
    try:
        vl = enter.get()
        html_text = requests.get(vl).text
        reg = r'[^"]\w+://\w\.\w+\.\w+/\w/\d+\.mp3'
        url1 = re.findall(reg, html_text, flags=re.MULTILINE)
        r = requests.get(url1[0])
        print(r)
    except Exception as e:
        text3 = tkinter.StringVar(value='что-то пошло не так')  # label about not successful download
        text4 = customtkinter.CTkLabel(master=app, textvariable=text3, width=200, height=20, fg_color='white')
        text4.place(relx=0.01, rely=0.36)
        print(e)

    if r:
        text3 = tkinter.StringVar(value='файл успешно скачан')  # label about successful download
        text4 = customtkinter.CTkLabel(master=app, textvariable=text3, width=200, height=20, fg_color='white')
        text4.place(relx=0.01, rely=0.36)
        enter1.place(relx=0.01, rely=0.65)
        button1 = customtkinter.CTkButton(master=app, text='Сохранить', command=button_function1)
        button1.place(relx=0.55, rely=0.6)
        text = tkinter.StringVar(value='Сохранить как')  # label link for set file name
        text = customtkinter.CTkLabel(master=app, textvariable=text, width=200, height=20, fg_color='white')
        text.place(relx=0.01, rely=0.5)


def button_function1():
    save = enter1.get()
    with open(save + '.mp3', 'wb') as f:
        f.write(r.content)
        text2 = tkinter.StringVar(value='файл сохранён')  # оповещение о сохранении файла
        text2 = customtkinter.CTkLabel(master=app, textvariable=text2, width=200, height=20, fg_color='white')
        text2.place(relx=0.01, rely=0.85)
        print('hello')


def extract_text():
    file_name = fd.asksaveasfilename(filetypes='*.mp3')
    f = open(file_name, 'w')
    s = enter1.get()
    f.write(s)
    f.close()


# Use CTkButton instead of tkinter Button


text1 = tkinter.StringVar(value='Вставить ссылку')  # label link for set link for download
text1 = customtkinter.CTkLabel(master=app, textvariable=text1, width=200, height=20, fg_color='white')
text1.place(relx=0.01, rely=0.05)  # расположение описания окна ниже (ввод ссылки)
enter = customtkinter.CTkEntry(master=app, width=200, height=20, bg_color='green',
                               placeholder_text='https://www.voicecards.ru')  # command string
enter.place(relx=0.01, rely=0.2)  # расположение ввода
button = customtkinter.CTkButton(master=app, text="Скачать mp3 файл", command=button_function, bg_color='red')  #
# button
button.place(relx=0.55, rely=0.18)  # download

enter1 = customtkinter.CTkEntry(master=app, width=200, height=20, bg_color='green',
                                placeholder_text='напишите название файла')

app.mainloop()
