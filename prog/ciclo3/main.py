import tkinter as tk
from decimal import Decimal, InvalidOperation


def calculate():
    try:
        altura = Decimal(altura_input.get("1.0", "end-1c"))
    except InvalidOperation:
        resultado_lb.config(text="A altura é invalida.")
        return

    if altura <= 0:
        resultado_lb.config(text="A altura tem que ser maior que zero.")
        return

    try:
        peso = Decimal(peso_input.get("1.0", "end-1c"))
    except InvalidOperation:
        resultado_lb.config(text="O peso é invalido.")
        return

    if peso <= 0:
        resultado_lb.config(text="O peso tem que ser maior que zero.")
        return

    altura = altura / 100
    imc = peso / (altura * altura)
    resultado_lb.config(text=f"IMC é {imc:.2f}")


def restart():
    paciente_input.delete(1.0, "end-1c")
    endereco_input.delete(1.0, "end-1c")
    altura_input.delete(1.0, "end-1c")
    peso_input.delete(1.0, "end-1c")


def end():
    window.destroy()


window = tk.Tk()
window.title("Cálculo do IMC - Indice de massa corporal")
window.geometry("700x300")

# Paciente
paciente_lb = tk.Label(window, text="Nome do paciente:")
paciente_lb.grid(column=0, row=0, pady=10, sticky=tk.E)

paciente_input = tk.Text(window, height=1, width=60)
paciente_input.grid(column=1, row=0, pady=10, columnspan=3, sticky=tk.W)

# Endereço
endereco_lb = tk.Label(window, text="Endereço Completo:")
endereco_lb.grid(column=0, row=1, pady=10, sticky=tk.E)

endereco_input = tk.Text(window, height=1, width=60)
endereco_input.grid(column=1, row=1, pady=10, columnspan=3, sticky=tk.W)

# Altura (cm)
altura_lb = tk.Label(window, text="Altura (cm):")
altura_lb.grid(column=0, row=2, pady=10, sticky=tk.E)

altura_input = tk.Text(window, height=1, width=35)
altura_input.grid(column=1, row=2, pady=10, sticky=tk.W)
altura_input.grid_columnconfigure(1, weight=1)

# Peso (kg)
peso_lb = tk.Label(window, text="Peso (kg):")
peso_lb.grid(column=0, row=3, pady=10, sticky=tk.E)

peso_input = tk.Text(window, height=1, width=35)
peso_input.grid(column=1, row=3, pady=10, sticky=tk.W)

# Resultado
resultado_lb = tk.Label(window, text="Resultado", borderwidth=2, relief="groove")
resultado_lb.grid(column=2, row=2, pady=10, rowspan=2, columnspan=2, sticky=tk.N+tk.S+tk.W+tk.E)

# Ações
calcula_btn = tk.Button(window, text="Calcular", command=calculate)
calcula_btn.grid(column=1, row=4, sticky=tk.E)

reinicia_btn = tk.Button(window, text="Reiniciar", command=restart)
reinicia_btn.grid(column=2, row=4, sticky=tk.W)

sair_btn = tk.Button(window, text="Sair", command=end)
sair_btn.grid(column=3, row=4, sticky=tk.E)

# Main loop
window.mainloop()
