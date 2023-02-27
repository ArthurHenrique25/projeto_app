import json
import customtkinter
import os
from tkinter import *
from tkinter import messagebox

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()

janela.geometry("800x500")
janela.title("CONSIGNADOS AGORA")
janela.iconbitmap("image//ICONE.ico")
janela.resizable(False,False)

laber = customtkinter.CTkLabel(master=janela, text="Área de cadastro",font=("Arial", 25)).place(x=280,y=60)
laber1 = customtkinter.CTkLabel(master=janela, text="Nome Completo:",font=("Arial", 18)).place(x=100,y=120)
laber2 = customtkinter.CTkLabel(master=janela, text="Email:",font=("Arial", 18)).place(x=100,y=180)
laber3 = customtkinter.CTkLabel(master=janela, text="Senha:",font=("Arial", 18)).place(x=100,y=240)

entry1 = customtkinter.CTkEntry(master=janela, width=600)
entry1.place(x=100, y=150)

entry2 = customtkinter.CTkEntry(master=janela, width=600)
entry2.place(x=100, y=210)

entry3 = customtkinter.CTkEntry(master=janela, width=600)
entry3.place(x=100, y=270)

chekbox = customtkinter.CTkCheckBox(master=janela, text="Concordo com os termos")
chekbox.place(x=100,y=320)

def enviar():
    nome = entry1.get()
    senha = entry3.get()

    with open("usuarios.json", "r") as f:
        usuarios = json.load(f)

    if nome in usuarios:
        messagebox.showerror("Erro", f"O usuário '{nome}' já existe!")
    else:
        usuarios[nome] = {"senha": senha}
        with open("usuarios.json", "w") as f:
            json.dump(usuarios, f)
        messagebox.showinfo("Confirmação", f"Usuário '{nome}' registrado com sucesso!")

button = customtkinter.CTkButton(master=janela,text="Enviar", command=enviar)
button.place(x=560,y=320)

def voltar_pagina_acesso():
    janela.destroy()
    os.system('python login.py')
      # Fecha a janela atual após voltar para a página de acesso

button2 = customtkinter.CTkButton(master=janela,text="Voltar",command=voltar_pagina_acesso)
button2.place(x=100,y=400)
janela.mainloop()