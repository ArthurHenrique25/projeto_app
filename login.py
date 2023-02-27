import customtkinter
import subprocess
from tkinter import *
import sys
import os
import time
import json

from tkinter import messagebox




customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")



janela = customtkinter.CTk()

janela.geometry("800x500")
janela.title("CONSIGNADOS AGORA")
janela.iconbitmap("image//ICONE.ico")
janela.resizable(   False,False)



img = PhotoImage(file="image//vsloe.png")
label_img = customtkinter.CTkLabel(master=janela,image=img)
label_img.place(x=-200, y =0)

frame = customtkinter.CTkFrame(master=janela,width=200,height=500)
frame.pack(side=RIGHT)

label = customtkinter.CTkLabel(master=frame, text="SISTEMA DE LOGIN",font=("Arial", 15),text_color="white")
label.place(x=30 ,y=140)



with open("Users//usuarios.json") as f:
    dados_usuarios = json.load(f)

with open("Users//lembrar_usuario.json") as f:
    lembrar_usuario = json.load(f)



def validar_usuario():
    usuario = entry1.get()
    senha = entry2.get()

    if usuario in dados_usuarios and senha == dados_usuarios[usuario]["senha"]:
    # se for válido
        messagebox.showinfo("Confirmação", f"Usuário '{usuario}' confirmado.")
        janela.destroy()
        os.system(' '.join(['python', 'acesso.py']))
    else:
    # se for inválido
        messagebox.showerror("Erro",f"Usuário ou senha {usuario} incorreto")



entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Usuario", text_color="white", width=180)
entry1.place(x=10, y=175)

# label1 = customtkinter.CTkLabel(master=frame, text="*O campo usuario é obrigatorio.", text_color="green").place(x=10, y=180)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Senha", text_color="white", width=180,show="******")
entry2.place(x=10,y=220)

# label2 = customtkinter.CTkLabel(master=frame,text="*O campo senha é obrigatorio",text_color="green").place(x=10, y=255)

def salvar_checkbox(estado):
    # Salvar o estado da checkbox em um arquivo JSON
    with open("lembrar_usuario.json", "w") as f:
        json.dump({"lembrar": estado, "usuario": entry1.get(), "senha": entry2.get()}, f)
        
# def lebrarsenha():
#     with open("usuarios.json") as f:
#         dados_usuarios = json.load(f)
#     with open("lembrar_usuario.json") as f:
#         dados_lembrar = json.load(f)
#     if entry1.get() in dados_usuarios:
#         if chekbox.is_checked():
#             # Se a checkbox já estiver marcada, salve o estado como True
#             salvar_checkbox(True)
#             # Armazena as informações do último usuário e senha utilizados
#             dados_lembrar["ultimo_usuario"] = entry1.get()
#             dados_lembrar["ultimo_senha"] = entry2.get()
#         else:
#             # Se a checkbox não estiver marcada, salve o estado como False
#             salvar_checkbox(False)
#             # Limpa as informações do último usuário e senha utilizados
#             dados_lembrar["ultimo_usuario"] = ""
#             dados_lembrar["ultimo_senha"] = ""
#         with open("lembrar_usuario.json", "w") as f:
#             json.dump(dados_lembrar, f)
#     if dados_lembrar["lembrar"] and dados_lembrar["ultimo_usuario"] == entry1.get():
#         entry2.delete(0, END)  # clear the password field
#         entry2.insert(0, dados_lembrar["ultimo_senha"])
#         chekbox.check()
#     else:
#         entry2.delete(0, END)  # clear the password field
#         chekbox.uncheck()


# chekbox = customtkinter.CTkCheckBox(master=frame,text="lembra-se de min sempre",command=lebrarsenha).place(x=10,y=290)





def pressionar_tecla(event):
    # função que é chamada quando uma tecla é pressionada
    if event.keysym == "Return":  # verifica se a tecla pressionada é "Enter"
        validar_usuario()  # chama a função "validar_usuario"

button = customtkinter.CTkButton(master=frame, text="Entrar", command=validar_usuario)
button.place(x=27, y=265)

# adiciona o bind para capturar a tecla pressionada na janela
janela.bind("<Key>", pressionar_tecla)
def voltar2():
    janela.destroy()
    os.system('python Esqueceu_senha.py')

click = customtkinter.CTkLabel(master=frame, text="Esqueceu a senha", text_color="white", cursor="hand2")
click.place(x=45,y=450)
click.bind("<Button-1>", lambda e: voltar2())

# if lembrar_usuario["lembrar"]:
#         # Se a checkbox "lembre de mim" foi marcada, preencha o campo de usuário e senha com os valores salvos
#     entry1.insert(0, lembrar_usuario["usuario"])
#     entry2.insert(0, lembrar_usuario["senha"])
#     chekbox.check()


def openNewWindow2():
    subprocess.Popen(['python', 'cadastro.py'])

def voltar_pagina_acesso():
    janela.destroy()
    os.system('python cadastro.py')

click2 = customtkinter.CTkLabel(master=frame, text="cadastrar", text_color="white", cursor="hand2")
click2.place(x=68, y=470)
click2.bind("<Button-1>", lambda e: voltar_pagina_acesso())

os.system('cls' if os.name == 'nt' else 'clear')

print("Programa rodando")
  
print("Aguardando usuario")       

     
      
janela.mainloop()


print("Programa finalizado")