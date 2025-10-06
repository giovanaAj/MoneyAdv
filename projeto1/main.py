from moneyAdvicer import pegarcotacoes
import tkinter as tk
from tkinter import simpledialog

def mostrar_cotacao():
    cod_cotacao = simpledialog.askstring("Cotação", "Digite o nome da moeda:")
    if cod_cotacao:
        cotacao = pegarcotacoes(cod_cotacao)
        texto = f"A cotação do {cod_cotacao.upper()} é R$ {cotacao}"
        label_cotacao.config(text=texto, fg="#2e7d32")
    else:
        label_cotacao.config(text="Nenhuma moeda informada.", fg="#cb2929")

root = tk.Tk()
root.title("Cotação da Moeda")
root.geometry("350x220")
root.configure(bg="#f5f5f5")

frame = tk.Frame(root, bg="#f5f5f5")
frame.pack(expand=True)

titulo = tk.Label(frame, text="Cotação de Moedas", font=("Arial", 16, "bold"), bg="#f5f5f5", fg="#1565c0")
titulo.pack(pady=(20, 10))

label_cotacao = tk.Label(frame, text="", font=("Arial", 12), bg="#f5f5f5")
label_cotacao.pack(pady=10)

btn_cotacao = tk.Button(frame, text="Buscar Cotação", font=("Arial", 12), bg="#1976d2", fg="white", command=mostrar_cotacao, relief="raised", bd=2)
btn_cotacao.pack(pady=15)

root.mainloop()