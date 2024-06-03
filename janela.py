import tkinter as tk
from tkinter import ttk

def cadastrar():
    # Limpar os campos de entrada
    entry_cliente.delete(0, tk.END)
    entry_produto.delete(0, tk.END)
    entry_quantidade.delete(0, tk.END)
    entry_categoria.delete(0, tk.END)

# Criar a janela
root = tk.Tk()
root.title("Cadastro de Vendas")

# Frame para o formulário
frame_form = ttk.Frame(root, padding="10")
frame_form.grid(row=0, column=0)

# Labels
label_cliente = ttk.Label(frame_form, text="Cliente:")
label_cliente.grid(row=0, column=0, sticky="W")

label_produto = ttk.Label(frame_form, text="Produto:")
label_produto.grid(row=1, column=0, sticky="W")

label_quantidade = ttk.Label(frame_form, text="Quantidade:")
label_quantidade.grid(row=2, column=0, sticky="W")

label_categoria = ttk.Label(frame_form, text="Categoria:")
label_categoria.grid(row=3, column=0, sticky="W")

# Campos de entrada
entry_cliente = ttk.Entry(frame_form, width=30)
entry_cliente.grid(row=0, column=1)

entry_produto = ttk.Entry(frame_form, width=30)
entry_produto.grid(row=1, column=1)

entry_quantidade = ttk.Entry(frame_form, width=30)
entry_quantidade.grid(row=2, column=1)

entry_categoria = ttk.Entry(frame_form, width=30)
entry_categoria.grid(row=3, column=1)

# Botão de cadastrar
btn_cadastrar = ttk.Button(frame_form, text="Cadastrar", command=cadastrar)
btn_cadastrar.grid(row=4, columnspan=2, pady=10)

root.mainloop()