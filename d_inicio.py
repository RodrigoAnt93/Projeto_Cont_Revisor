import tkinter as tk
import json
from datetime import datetime

class SalvarData:

    def __init__(self, root):
        self.root = root
        self.root.title("DATA INÍCIO DA REVISÃO")
        self.root.geometry("200x100+900+100")

        self.label = tk.Label(root, text="Digite uma data (dd/mm/yyyy):")
        self.label.pack()

        self.entrada = tk.Entry(root)
        self.entrada.pack()

        self.salvar_botao = tk.Button(root, text="Salvar", command=self.salvar_conteudo)
        self.salvar_botao.pack()

        self.status_label = tk.Label(root, text="")
        self.status_label.pack()


    def salvar_em_json(self, conteudo):
        data = {'conteudo': conteudo}

        with open('bd_dInicio.json', 'w') as file:
            json.dump(data, file)


    def salvar_conteudo(self):
        conteudo = self.entrada.get()

        try:
            # Tenta converter o conteúdo para um objeto de data
            data = datetime.strptime(conteudo, '%d/%m/%Y')
            self.salvar_em_json(data.strftime('%d/%m/%Y'))
            self.status_label.config(text="Data salva com sucesso!")
        except ValueError:
            self.status_label.config(text="Formato de data inválido")


def executar():
    root = tk.Tk()
    app = SalvarData(root)
    root.mainloop()
