import customtkinter
import os
from tkinter import *

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")



janela = customtkinter.CTk()

janela.geometry("800x500")
janela.title("CONSIGNADOS AGORA")
janela.iconbitmap("image//ICONE.ico")
janela.resizable(False,False)
laber3 = customtkinter.CTkLabel(master=janela, text= "Esqueci minha senha",font=("Arial", 25) ).place(x=280,y=60)
laber = customtkinter.CTkLabel(master=janela, text= "Email:",font=("Arial", 15)).place(x=80,y=160)

entry1 = customtkinter.CTkEntry(master=janela,width=600).place(x=80, y=190)
button = customtkinter.CTkButton(master=janela,text="Enviar").place(x=300,y=230)
label2 = customtkinter.CTkLabel(master=janela,text="*O campo de email é obrigatorio",text_color="green",).place(x=126, y=160)

def voltar_pagina_acesso():
    janela.destroy()
    os.system('python login.py')

button2 = customtkinter.CTkButton(master=janela,text="Voltar",command=voltar_pagina_acesso)
button2.place(x=100,y=400)




janela.mainloop()