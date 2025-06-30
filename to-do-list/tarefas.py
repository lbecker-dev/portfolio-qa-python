import tkinter as tk
from tkinter import messagebox, simpledialog
from datetime import datetime
import os

ARQUIVO_TAREFAS = 'C:\\Users\lbecker\\AppData\\Local\\Programs\\Python\\Python312\\tarefas_gui.txt'

# Carrega tarefas do arquivo
def carregar_tarefas():
    tarefas = []
    if os.path.exists(ARQUIVO_TAREFAS):
        with open(ARQUIVO_TAREFAS, 'r') as f:
            for linha in f:
                titulo, status, data = linha.strip().split('|')
                tarefas.append({'titulo': titulo, 'status': status, 'data': data})
    return tarefas

# Salva tarefas no arquivo
def salvar_tarefas(tarefas):
    with open(ARQUIVO_TAREFAS, 'w') as f:
        for t in tarefas:
            f.write(f"{t['titulo']}|{t['status']}|{t['data']}\n")

# Classe principal da interface
class GerenciadorTarefas:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciador de Tarefas")
        self.tarefas = carregar_tarefas()

        self.listbox = tk.Listbox(root, width=60, height=10)
        self.listbox.pack(pady=10)

        self.btn_adicionar = tk.Button(root, text="Adicionar Tarefa", command=self.adicionar)
        self.btn_concluir = tk.Button(root, text="Concluir Tarefa", command=self.concluir)
        self.btn_relatorio = tk.Button(root, text="Gerar Relatório", command=self.relatorio)
        self.btn_sair = tk.Button(root, text="Salvar e Sair", command=self.sair)

        self.btn_adicionar.pack(pady=2)
        self.btn_concluir.pack(pady=2)
        self.btn_relatorio.pack(pady=2)
        self.btn_sair.pack(pady=10)

        self.atualizar_lista()

    def atualizar_lista(self):
        self.listbox.delete(0, tk.END)
        for i, t in enumerate(self.tarefas):
            self.listbox.insert(tk.END, f"{i+1}. {t['titulo']} | {t['status']} | {t['data']}")

    def adicionar(self):
        titulo = simpledialog.askstring("Nova Tarefa", "Digite o título da tarefa:")
        if titulo:
            data = datetime.now().strftime("%d/%m/%Y %H:%M")
            self.tarefas.append({'titulo': titulo, 'status': 'pendente', 'data': data})
            self.atualizar_lista()

    def concluir(self):
        try:
            selecionado = self.listbox.curselection()[0]
            self.tarefas[selecionado]['status'] = 'concluída'
            self.atualizar_lista()
        except IndexError:
            messagebox.showwarning("Atenção", "Selecione uma tarefa para concluir.")

    def relatorio(self):
        total = len(self.tarefas)
        concluidas = len([t for t in self.tarefas if t['status'] == 'concluída'])
        pendentes = total - concluidas
        mensagem = f"📊 Relatório:\n\nTotal: {total}\nPendentes: {pendentes}\nConcluídas: {concluidas}"
        messagebox.showinfo("Relatório de Tarefas", mensagem)

    def sair(self):
        salvar_tarefas(self.tarefas)
        self.root.destroy()

# Executa o app
if __name__ == "__main__":
    root = tk.Tk()
    app = GerenciadorTarefas(root)
    root.mainloop()
