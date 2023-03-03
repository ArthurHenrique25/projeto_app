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

def salvar_usuario():
    # ler dados dos campos de entrada
    nome = entry1.get()
    email = entry2.get()
    senha = entry3.get()

    # criar um dicionário com os dados do usuário
    usuario = {
        "nome": nome,
        "email": email,
        "senha": senha
    }

    # salvar o dicionário em um arquivo JSON
    with open("Users//usuarios.json", "w") as arquivo:
        json.dump(usuario, arquivo)

    # exibir uma mensagem de confirmação
    messagebox.showinfo("Cadastro realizado", "Seu cadastro foi salvo com sucesso.")


import json

def validar_usuario():
    # carregar o arquivo JSON
    with open('Users//usuarios.json', 'r') as arquivo:
        dados_usuarios = json.load(arquivo)

    # extrair o email do usuário
    email = entry1.get()

    if email in [usuario["email"] for usuario in dados_usuarios]:
        # se for válido
        messagebox.showinfo("Confirmação", f"Email '{email}' confirmado.")
        janela.destroy()
        os.system(' '.join(['python', 'acesso.py']))
    else:
        # se for inválido
        messagebox.showerror("Erro", f"Email {email} não cadastrado")




button = customtkinter.CTkButton(master=janela,text="Enviar",command=salvar_usuario)
button.place(x=560,y=320)

def voltar_pagina_acesso():
    janela.destroy()
    os.system('python login.py')
      # Fecha a janela atual após voltar para a página de acesso

button2 = customtkinter.CTkButton(master=janela,text="Voltar",command=voltar_pagina_acesso)
button2.place(x=100,y=400)
janela.mainloop()