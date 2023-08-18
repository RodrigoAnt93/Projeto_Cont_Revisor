import tkinter as tk
from tkinter import ttk
import json
from datetime import datetime

class LeitorDadosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("FILTRO POR DATA")
        self.root.geometry("200x350+900+100")

        self.label_data_inicio = tk.Label(root, text="Data Inicial (DD/MM/YYYY):")
        self.label_data_inicio.pack()

        self.entry_data_inicio = ttk.Entry(root)
        self.entry_data_inicio.pack()

        self.label_data_fim = tk.Label(root, text="Data Final (DD/MM/YYYY):")
        self.label_data_fim.pack()

        self.entry_data_fim = ttk.Entry(root)
        self.entry_data_fim.pack()

        self.botao_filtrar = tk.Button(root, text="Filtrar", command=self.filtrar_dados)
        self.botao_filtrar.pack()

        self.label_resultados = tk.Label(root, text="")
        self.label_resultados.pack()

    def filtrar_dados(self):
        data_inicio = self.entry_data_inicio.get()
        data_fim = self.entry_data_fim.get()

        registros = self.carregar_dados()

        total_contador1 = 0
        total_contador2 = 0
        total_opcoes = {opcao: 0 for opcao in ["RG", "CR", "FOTO"]}

        for registro in registros:
            if self.esta_no_intervalo(registro["data"], data_inicio, data_fim):
                total_contador1 += registro["APROVADOS"]
                total_contador2 += registro["REPROVADOS"]
                for opcao in total_opcoes:
                    total_opcoes[opcao] += registro["opcoes_selecionadas"].get(opcao, 0)

        resultados_text = "\nSoma de índices durante o período:\n\n"
        resultados_text += f"APROVADOS:  {total_contador1}\n"
        resultados_text += f"\nREPROVADOS:  {total_contador2}\n"
        for opcao, total in total_opcoes.items():
            resultados_text += f"{opcao}:  {total}\n"

        resultados_text += f"\nTOTAL DE REVISADOS:  {total_contador1 + total_contador2}\n"

        self.label_resultados.config(text=resultados_text)

    def esta_no_intervalo(self, data_registro, data_inicio, data_fim):
        data_registro = datetime.strptime(data_registro, "%d/%m/%Y")
        data_inicio = datetime.strptime(data_inicio, "%d/%m/%Y")
        data_fim = datetime.strptime(data_fim, "%d/%m/%Y")
        return data_inicio <= data_registro <= data_fim

    def carregar_dados(self):
        try:
            with open("dados.json", "r") as arquivo:
                registros = json.load(arquivo)
                return registros
        except (FileNotFoundError, json.JSONDecodeError, KeyError):
            pass
        return []

def executar():
    root = tk.Tk()
    app = LeitorDadosApp(root)
    root.mainloop()



