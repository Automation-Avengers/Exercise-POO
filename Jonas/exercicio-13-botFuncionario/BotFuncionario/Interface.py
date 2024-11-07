import tkinter as tk
from tkinter import messagebox, Toplevel, font
from Funcionario import Horista, Mensalista, Comissionado

class FuncionarioApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Cadastro de Funcionários")
        self.master.geometry("600x600")

        self.master.configure(bg="#e3f2fd")

        self.frame_principal = tk.Frame(master, bg="#e3f2fd", padx=20, pady=20)
        self.frame_principal.pack(pady=20)

        self.tipo_var = tk.StringVar(value="horista")

        self.default_font = font.Font(family="Arial", size=12, weight="bold")

        self.horista_button = tk.Button(self.frame_principal, text="Horista", command=lambda: self.mostrar_frame("horista"), font=self.default_font, bg="#4CAF50", fg="white", width=12)
        self.horista_button.pack(side=tk.LEFT, padx=10)

        self.mensalista_button = tk.Button(self.frame_principal, text="Mensalista", command=lambda: self.mostrar_frame("mensalista"), font=self.default_font, bg="#2196F3", fg="white", width=12)
        self.mensalista_button.pack(side=tk.LEFT, padx=10)

        self.comissionado_button = tk.Button(self.frame_principal, text="Comissionado", command=lambda: self.mostrar_frame("comissionado"), font=self.default_font, bg="#FF9800", fg="white", width=12)
        self.comissionado_button.pack(side=tk.LEFT, padx=10)

        self.frame_horista = self.criar_frame_horista(master)
        self.frame_mensalista = self.criar_frame_mensalista(master)
        self.frame_comissionado = self.criar_frame_comissionado(master)

        self.mostrar_frame("horista")

    def criar_frame_horista(self, master):
        frame = tk.Frame(master, bg="#ffffff", padx=20, pady=20)

        tk.Label(frame, text="Nome:", bg="#ffffff", font=self.default_font).grid(row=0, column=0, sticky='e', pady=5)
        self.nome_entry_horista = tk.Entry(frame, font=self.default_font)
        self.nome_entry_horista.grid(row=0, column=1, pady=5)

        tk.Label(frame, text="Matrícula:", bg="#ffffff", font=self.default_font).grid(row=1, column=0, sticky='e', pady=5)
        self.matricula_entry_horista = tk.Entry(frame, font=self.default_font)
        self.matricula_entry_horista.grid(row=1, column=1, pady=5)

        tk.Label(frame, text="Valor Hora:", bg="#ffffff", font=self.default_font).grid(row=2, column=0, sticky='e', pady=5)
        self.valor_hora_entry = tk.Entry(frame, font=self.default_font)
        self.valor_hora_entry.grid(row=2, column=1, pady=5)

        tk.Label(frame, text="Horas Trabalhadas:", bg="#ffffff", font=self.default_font).grid(row=3, column=0, sticky='e', pady=5)
        self.horas_entry_horista = tk.Entry(frame, font=self.default_font)
        self.horas_entry_horista.grid(row=3, column=1, pady=5)

        self.cadastrar_horista_button = tk.Button(frame, text="Cadastrar Horista", command=self.cadastrar_horista, font=self.default_font, bg="#4CAF50", fg="white")
        self.cadastrar_horista_button.grid(row=4, columnspan=2, pady=10)

        return frame

    def criar_frame_mensalista(self, master):
        frame = tk.Frame(master, bg="#ffffff", padx=20, pady=20)

        tk.Label(frame, text="Nome:", bg="#ffffff", font=self.default_font).grid(row=0, column=0, sticky='e', pady=5)
        self.nome_entry_mensalista = tk.Entry(frame, font=self.default_font)
        self.nome_entry_mensalista.grid(row=0, column=1, pady=5)

        tk.Label(frame, text="Matrícula:", bg="#ffffff", font=self.default_font).grid(row=1, column=0, sticky='e', pady=5)
        self.matricula_entry_mensalista = tk.Entry(frame, font=self.default_font)
        self.matricula_entry_mensalista.grid(row=1, column=1, pady=5)

        tk.Label(frame, text="Salário Mensal:", bg="#ffffff", font=self.default_font).grid(row=2, column=0, sticky='e', pady=5)
        self.salario_entry_mensalista = tk.Entry(frame, font=self.default_font)
        self.salario_entry_mensalista.grid(row=2, column=1, pady=5)

        self.cadastrar_mensalista_button = tk.Button(frame, text="Cadastrar Mensalista", command=self.cadastrar_mensalista, font=self.default_font, bg="#2196F3", fg="white")
        self.cadastrar_mensalista_button.grid(row=3, columnspan=2, pady=10)

        return frame

    def criar_frame_comissionado(self, master):
        frame = tk.Frame(master, bg="#ffffff", padx=20, pady=20)

        tk.Label(frame, text="Nome:", bg="#ffffff", font=self.default_font).grid(row=0, column=0, sticky='e', pady=5)
        self.nome_entry_comissionado = tk.Entry(frame, font=self.default_font)
        self.nome_entry_comissionado.grid(row=0, column=1, pady=5)

        tk.Label(frame, text="Matrícula:", bg="#ffffff", font=self.default_font).grid(row=1, column=0, sticky='e', pady=5)
        self.matricula_entry_comissionado = tk.Entry(frame, font=self.default_font)
        self.matricula_entry_comissionado.grid(row=1, column=1, pady=5)

        tk.Label(frame, text="Salário Base:", bg="#ffffff", font=self.default_font).grid(row=2, column=0, sticky='e', pady=5)
        self.salario_base_entry = tk.Entry(frame, font=self.default_font)
        self.salario_base_entry.grid(row=2, column=1, pady=5)

        tk.Label(frame, text="Vendas:", bg="#ffffff", font=self.default_font).grid(row=3, column=0, sticky='e', pady=5)
        self.vendas_entry = tk.Entry(frame, font=self.default_font)
        self.vendas_entry.grid(row=3, column=1, pady=5)

        tk.Label(frame, text="Taxa de Comissão:", bg="#ffffff", font=self.default_font).grid(row=4, column=0, sticky='e', pady=5)
        self.taxa_comissao_entry = tk.Entry(frame, font=self.default_font)
        self.taxa_comissao_entry.grid(row=4, column=1, pady=5)

        self.cadastrar_comissionado_button = tk.Button(frame, text="Cadastrar Comissionado", command=self.cadastrar_comissionado, font=self.default_font, bg="#FF9800", fg="white")
        self.cadastrar_comissionado_button.grid(row=5, columnspan=2, pady=10)

        return frame

    def mostrar_frame(self, tipo):
        self.frame_horista.pack_forget()
        self.frame_mensalista.pack_forget()
        self.frame_comissionado.pack_forget()

        if tipo == "horista":
            self.frame_horista.pack(pady=10)
        elif tipo == "mensalista":
            self.frame_mensalista.pack(pady=10)
        elif tipo == "comissionado":
            self.frame_comissionado.pack(pady=10)

    def mostrar_informacoes(self, funcionario_info):
        info_window = Toplevel(self.master)
        info_window.title("Informações do Funcionário")
        info_window.configure(bg="#e3f2fd")

        for i, (key, value) in enumerate(funcionario_info.items()):
            tk.Label(info_window, text=f"{key}: {value}", font=self.default_font, bg="#e3f2fd").grid(row=i, column=0, padx=10, pady=5, sticky='w')

        tk.Button(info_window, text="Fechar", command=info_window.destroy, font=self.default_font, bg="#f44336", fg="white").grid(row=len(funcionario_info), column=0, pady=10)

    def cadastrar_horista(self):
        try:
            nome = self.nome_entry_horista.get()
            matricula = self.matricula_entry_horista.get()
            horas_trabalhadas = float(self.horas_entry_horista.get())
            valor_hora = float(self.valor_hora_entry.get())
            
            funcionario = Horista(nome, matricula, horas_trabalhadas, valor_hora)
            salario = funcionario.calcular_salario()
            info = {
                "Nome": nome,
                "Matrícula": matricula,
                "Tipo": "Horista",
                "Horas Trabalhadas": horas_trabalhadas,
                "Valor da Hora": valor_hora,
                "Salário": salario
            }
            self.mostrar_informacoes(info)
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores válidos.")

    def cadastrar_mensalista(self):
        try:
            nome = self.nome_entry_mensalista.get()
            matricula = self.matricula_entry_mensalista.get()
            salario_mensal = float(self.salario_entry_mensalista.get())
            
            funcionario = Mensalista(nome, matricula, salario_mensal)
            salario = funcionario.calcular_salario()
            info = {
                "Nome": nome,
                "Matrícula": matricula,
                "Tipo": "Mensalista",
                "Salário Mensal": salario
            }
            self.mostrar_informacoes(info)
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores válidos.")

    def cadastrar_comissionado(self):
        try:
            nome = self.nome_entry_comissionado.get()
            matricula = self.matricula_entry_comissionado.get()
            salario_base = float(self.salario_base_entry.get())
            vendas = float(self.vendas_entry.get())
            taxa_comissao = float(self.taxa_comissao_entry.get())
            
            funcionario = Comissionado(nome, matricula, salario_base, vendas, taxa_comissao)
            salario = funcionario.calcular_salario()
            info = {
                "Nome": nome,
                "Matrícula": matricula,
                "Tipo": "Comissionado",
                "Salário Base": salario_base,
                "Vendas": vendas,
                "Taxa de Comissão": taxa_comissao,
                "Salário": salario
            }
            self.mostrar_informacoes(info)
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores válidos.")

if __name__ == "__main__":
    root = tk.Tk()
    app = FuncionarioApp(root)
    root.mainloop()
