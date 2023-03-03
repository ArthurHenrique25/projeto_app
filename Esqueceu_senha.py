import customtkinter
import os
import json
from tkinter import *
from tkinter import messagebox

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()

janela.geometry("800x500")
janela.title("CONSIGNADOS AGORA")
janela.iconbitmap("image//ICONE.ico")
janela.resizable(False,False)
laber3 = customtkinter.CTkLabel(master=janela, text= "Esqueci minha senha",font=("Arial", 25) ).place(x=280,y=60)
laber = customtkinter.CTkLabel(master=janela, text= "Email:",font=("Arial", 15)).place(x=80,y=160)

entry1 = customtkinter.CTkEntry(master=janela,width=600)
entry1.place(x=80, y=190)

label2 = customtkinter.CTkLabel(master=janela,text="*O campo de email é obrigatorio",text_color="green",).place(x=126, y=160)

def voltar_pagina_acesso():
    janela.destroy()
    os.system('python login.py')

def validar_usuario():
    # carregar o arquivo JSON
    with open('Users//usuarios.json', 'r') as arquivo:
        dados_usuarios = json.load(arquivo)

    # extrair os dados do usuário e senha
    email = entry1.get()
    

    # verificar se o nome de usuário e senha estão corretos
    if "email" in dados_usuarios  == dados_usuarios["email"] :
        # se for válido
        messagebox.showinfo("Confirmação", f"Usuário '{email}' confirmado.")
        janela.destroy()
        #
    else:
        # se for inválido
        messagebox.showerror("Erro", f"Usuário ou senha {email} incorreto")

button = customtkinter.CTkButton(master=janela,text="Enviar",command=validar_usuario)
button.place(x=300,y=230)

button2 = customtkinter.CTkButton(master=janela,text="Voltar",command=voltar_pagina_acesso)
button2.place(x=100,y=400)

janela.mainloop()