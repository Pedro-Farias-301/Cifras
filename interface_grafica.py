import tkinter as tk
from tkinter import messagebox, filedialog
from cifras_musicais import CifrasMusicais

class InterfaceCifras:
    def __init__(self, root):
        self.cifras = CifrasMusicais()
        self.root = root
        self.root.title("Sistema de Cifras Musicais")
        self.root.geometry("800x600")
        
        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        tk.Label(self.frame, text="Seção (ex.: Estrofe 1, Refrão):").grid(row=0, column=0, sticky="w")
        self.entry_secao = tk.Entry(self.frame)
        self.entry_secao.grid(row=0, column=1, sticky="ew")
        tk.Button(self.frame, text="Adicionar Seção", command=self.adicionar_secao).grid(row=0, column=2, padx=5)
        
        tk.Label(self.frame, text="Palavra/Trecho:").grid(row=1, column=0, sticky="w")
        self.entry_palavra = tk.Entry(self.frame)
        self.entry_palavra.grid(row=1, column=1, sticky="ew")
        tk.Label(self.frame, text="Cifra (ex.: C, Am):").grid(row=2, column=0, sticky="w")
        self.entry_cifra = tk.Entry(self.frame)
        self.entry_cifra.grid(row=2, column=1, sticky="ew")
        tk.Button(self.frame, text="Adicionar Palavra/Cifra", command=self.adicionar_palavra_cifra).grid(row=2, column=2, padx=5)
        
        tk.Label(self.frame, text="Posição:").grid(row=3, column=0, sticky="w")
        self.entry_posicao = tk.Entry(self.frame)
        self.entry_posicao.grid(row=3, column=1, sticky="ew")
        tk.Button(self.frame, text="Modificar Cifra", command=self.modificar_cifra).grid(row=3, column=2, padx=5)
        
        tk.Label(self.frame, text="Posições (ex.: 1,2,3):").grid(row=4, column=0, sticky="w")
        self.entry_posicoes = tk.Entry(self.frame)
        self.entry_posicoes.grid(row=4, column=1, sticky="ew")
        tk.Button(self.frame, text="Modificar em Massa", command=self.modificar_em_massa).grid(row=4, column=2, padx=5)
        
        tk.Button(self.frame, text="Apagar Palavra/Cifra", command=self.apagar_palavra_cifra).grid(row=5, column=2, padx=5)
        
        self.text_exibir = tk.Text(self.frame, height=20, width=60)
        self.text_exibir.grid(row=6, column=0, columnspan=3, pady=10)
        tk.Button(self.frame, text="Atualizar Exibição", command=self.atualizar_exibicao).grid(row=7, column=0, pady=5)
        
        tk.Button(self.frame, text="Salvar em Arquivo", command=self.salvar_arquivo).grid(row=7, column=1, pady=5)
        tk.Button(self.frame, text="Carregar de Arquivo", command=self.carregar_arquivo).grid(row=7, column=2, pady=5)
        tk.Button(self.frame, text="Exportar para PDF", command=self.exportar_pdf).grid(row=8, column=1, pady=5)
        
        self.frame.columnconfigure(1, weight=1)

    def adicionar_secao(self):
        nome_secao = self.entry_secao.get().strip()
        if not nome_secao:
            messagebox.showerror("Erro", "Digite um nome para a seção.")
            return
        if self.cifras.adicionar_secao(nome_secao):
            messagebox.showinfo("Sucesso", f"Seção '{nome_secao}' adicionada!")
            self.atualizar_exibicao()
        else:
            messagebox.showerror("Erro", f"Seção '{nome_secao}' já existe.")

    def adicionar_palavra_cifra(self):
        nome_secao = self.entry_secao.get().strip()
        palavra = self.entry_palavra.get().strip()
        cifra = self.entry_cifra.get().strip()
        try:
            self.cifras.adicionar_palavra_cifra(nome_secao, palavra, cifra)
            messagebox.showinfo("Sucesso", f"Palavra '{palavra}' com cifra '{cifra or 'Nenhuma'}' adicionada!")
            self.atualizar_exibicao()
            self.entry_palavra.delete(0, tk.END)
            self.entry_cifra.delete(0, tk.END)
        except ValueError as e:
            messagebox.showerror("Erro", str(e))

    def modificar_cifra(self):
        nome_secao = self.entry_secao.get().strip()
        try:
            posicao = int(self.entry_posicao.get())
            nova_cifra = self.entry_cifra.get().strip()
            self.cifras.modificar_cifra(nome_secao, posicao, nova_cifra)
            messagebox.showinfo("Sucesso", f"Cifra na posição {posicao} modificada!")
            self.atualizar_exibicao()
            self.entry_posicao.delete(0, tk.END)
            self.entry_cifra.delete(0, tk.END)
        except ValueError as e:
            messagebox.showerror("Erro", str(e))

    def modificar_em_massa(self):
        nome_secao = self.entry_secao.get().strip()
        posicoes_str = self.entry_posicoes.get().strip()
        nova_cifra = self.entry_cifra.get().strip()
        try:
            posicoes = [int(p) for p in posicoes_str.split(",")]
            self.cifras.modificar_cifras_em_massa(nome_secao, posicoes, nova_cifra)
            messagebox.showinfo("Sucesso", f"Cifras nas posições {posicoes} modificadas!")
            self.atualizar_exibicao()
            self.entry_posicoes.delete(0, tk.END)
            self.entry_cifra.delete(0, tk.END)
        except ValueError as e:
            messagebox.showerror("Erro", str(e))

    def apagar_palavra_cifra(self):
        nome_secao = self.entry_secao.get().strip()
        try:
            posicao = int(self.entry_posicao.get())
            self.cifras.remover_palavra_cifra(nome_secao, posicao)
            messagebox.showinfo("Sucesso", f"Palavra e cifra na posição {posicao} removidas!")
            self.atualizar_exibicao()
            self.entry_posicao.delete(0, tk.END)
        except ValueError as e:
            messagebox.showerror("Erro", str(e))

    def atualizar_exibicao(self):
        self.text_exibir.delete(1.0, tk.END)
        self.text_exibir.insert(tk.END, self.cifras.exibir_musica())

    def salvar_arquivo(self):
        nome_arquivo = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if nome_arquivo:
            try:
                self.cifras.salvar_em_arquivo(nome_arquivo)
                messagebox.showinfo("Sucesso", f"Música salva em {nome_arquivo}!")
            except Exception as e:
                messagebox.showerror("Erro", str(e))

    def carregar_arquivo(self):
        nome_arquivo = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if nome_arquivo:
            try:
                self.cifras.carregar_de_arquivo(nome_arquivo)
                messagebox.showinfo("Sucesso", f"Música carregada de {nome_arquivo}!")
                self.atualizar_exibicao()
            except Exception as e:
                messagebox.showerror("Erro", str(e))

    def exportar_pdf(self):
        nome_arquivo = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if nome_arquivo:
            try:
                self.cifras.exportar_pdf(nome_arquivo)
                messagebox.showinfo("Sucesso", f"Música exportada para {nome_arquivo}!")
            except Exception as e:
                messagebox.showerror("Erro", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = InterfaceCifras(root)
    root.mainloop()