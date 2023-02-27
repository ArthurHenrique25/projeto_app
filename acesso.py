import customtkinter

from tkinter import *

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")



janela = customtkinter.CTk()

janela.geometry("800x500")
janela.title("CONSIGNADOS AGORA")
janela.iconbitmap("image//ICONE.ico")
janela.resizable(False,False)


janela.mainloop()