import requests
# usado o '*' para pegar tudo na biblioteca, não necessário mais chamar a biblioteca
from tkinter import *


def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''

    texto_cota["text"] = texto



# inicia a janela para configurar
janela = Tk()

# edição do titulo
janela.title("Cotação")
janela.geometry("220x180")

# Cria um texto para aparecer na tela
# label(qual janela, texto)
texto_orientacao = Label(janela, text="Clique no botão para ver as cotações")
# posição do elemento em relação a uma malha (grid)
# pad = espaçamento (padding)
texto_orientacao.grid(column=0, row=0, padx=10, pady=10)

# Cria um botão para aparecer na tela
botao = Button(janela, text="Buscar cotações", command=pegar_cotacoes)
botao.grid(column=0, row=1, padx=10, pady=10)

# texto vazio para as cotações
texto_cota = Label(janela, text="")
texto_cota.grid(column=0, row=2, padx=10, pady=10)

# cria a janela configurada até agora
janela.mainloop()
