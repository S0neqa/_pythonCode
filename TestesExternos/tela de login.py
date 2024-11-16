import customtkinter as tk

# tema e cor da janela
tk.set_appearance_mode("dark")
tk.set_default_color_theme("dark-blue")

# tamanho da janela
janela = tk.CTk()
janela.geometry("500x300")


# função clique para ser chamada quando o botão de login for pressionado
def clique():
    print("Fazer Login")


# elementos da janela
# texto
texto = tk.CTkLabel(janela, text="Faça login")
# email
email = tk.CTkEntry(janela, placeholder_text="E-mail")
# senha
senha = tk.CTkEntry(janela, placeholder_text="Senha", show="*")
# botão
botao = tk.CTkButton(janela, text="Login", command=clique)

# define um espaçamento e uma posição para os elementos
texto.pack(padx=10, pady=10)
email.pack(padx=10, pady=10)
senha.pack(padx=10, pady=10)
botao.pack(padx=10, pady=10)

# gera a janela
janela.mainloop()
