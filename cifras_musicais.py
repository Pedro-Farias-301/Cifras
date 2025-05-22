import json
import re
import os

class CifrasMusicais:
    def __init__(self):
    
        self.secoes = {}  

    def validar_cifra(self, cifra):
        
        if not cifra:
            return True
        padrao = r'^[A-G](m|maj|dim|aug|sus[2|4])?([0-9])?(\/[A-G])?$'
        return bool(re.match(padrao, cifra))

    def adicionar_secao(self, nome_secao):
    
        if nome_secao not in self.secoes:
            self.secoes[nome_secao] = []
            return True
        return False

    def adicionar_palavra_cifra(self, nome_secao, palavra, cifra):
       
        if nome_secao not in self.secoes:
            raise ValueError(f"Seção '{nome_secao}' não existe.")
        if not isinstance(palavra, str) or not palavra.strip():
            raise ValueError("A palavra deve ser uma string não vazia.")
        if not self.validar_cifra(cifra):
            raise ValueError("A cifra deve ser um acorde válido (ex.: C, Am, G7) ou vazia.")
        posicao = len(self.secoes[nome_secao]) + 1
        self.secoes[nome_secao].append((posicao, palavra.strip(), cifra))

    def modificar_cifra(self, nome_secao, posicao, nova_cifra):
        
        if nome_secao not in self.secoes:
            raise ValueError(f"Seção '{nome_secao}' não existe.")
        if not isinstance(posicao, int) or posicao < 1 or posicao > len(self.secoes[nome_secao]):
            raise ValueError(f"Posição inválida. Escolha entre 1 e {len(self.secoes[nome_secao])}.")
        if not self.validar_cifra(nova_cifra):
            raise ValueError("A nova cifra deve ser um acorde válido (ex.: C, Am, G7) ou vazia.")
        for i, (pos, palavra, _) in enumerate(self.secoes[nome_secao]):
            if pos == posicao:
                self.secoes[nome_secao][i] = (pos, palavra, nova_cifra)
                return
        raise ValueError(f"Posição {posicao} não encontrada.")

    def modificar_cifras_em_massa(self, nome_secao, posicoes, nova_cifra):
       
        if nome_secao not in self.secoes:
            raise ValueError(f"Seção '{nome_secao}' não existe.")
        if not self.validar_cifra(nova_cifra):
            raise ValueError("A nova cifra deve ser um acorde válido (ex.: C, Am, G7) ou vazia.")
        for posicao in posicoes:
            if not isinstance(posicao, int) or posicao < 1 or posicao > len(self.secoes[nome_secao]):
                raise ValueError(f"Posição {posicao} inválida.")
            for i, (pos, palavra, _) in enumerate(self.secoes[nome_secao]):
                if pos == posicao:
                    self.secoes[nome_secao][i] = (pos, palavra, nova_cifra)

    def remover_palavra_cifra(self, nome_secao, posicao):
        if nome_secao not in self.secoes:
            raise ValueError(f"Seção '{nome_secao}' não existe.")
        if not isinstance(posicao, int) or posicao < 1 or posicao > len(self.secoes[nome_secao]):
            raise ValueError(f"Posição inválida. Escolha entre 1 e {len(self.secoes[nome_secao])}.")
        self.secoes[nome_secao] = [(p, w, c) for p, w, c in self.secoes[nome_secao] if p != posicao]
        
        for i, (_, palavra, cifra) in enumerate(self.secoes[nome_secao]):
            self.secoes[nome_secao][i] = (i + 1, palavra, cifra)

    def exibir_musica(self):
        
        if not self.secoes:
            return "Nenhuma seção cadastrada."
        resultado = []
        for nome_secao, trechos in self.secoes.items():
            if not trechos:
                resultado.append(f"{nome_secao}: (Vazia)")
                continue
            max_len = max(max(len(palavra), len(cifra)) for _, palavra, cifra in trechos)
            linha_cifras = []
            linha_palavras = []
            for _, palavra, cifra in sorted(trechos):
                linha_cifras.append(cifra.ljust(max_len))
                linha_palavras.append(palavra.ljust(max_len))
            resultado.append(f"{nome_secao}:\n{' '.join(linha_cifras)}\n{' '.join(linha_palavras)}")
        return "\n\n".join(resultado)

    def salvar_em_arquivo(self, nome_arquivo):
        
        with open(nome_arquivo, 'w', encoding='utf-8') as f:
            json.dump(self.secoes, f, ensure_ascii=False)

    def carregar_de_arquivo(self, nome_arquivo):
     
        try:
            with open(nome_arquivo, 'r', encoding='utf-8') as f:
                self.secoes = json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"O arquivo {nome_arquivo} não foi encontrado.")

    def exportar_pdf(self, nome_arquivo):
     
        latex_content = self.gerar_latex()
        with open("template.tex", 'w', encoding='utf-8') as f:
            f.write(latex_content)
        os.system(f"latexmk -pdf -jobname={nome_arquivo.replace('.pdf', '')} template.tex")
  
        for ext in ['.aux', '.log', '.out', '.fdb_latexmk', '.fls']:
            try:
                os.remove(f"template{ext}")
            except FileNotFoundError:
                pass

    def gerar_latex(self):
        
        latex = [
            r"\documentclass[a4paper,12pt]{article}",
            r"\usepackage[utf8]{inputenc}",
            r"\usepackage[T1]{fontenc}",
            r"\usepackage{geometry}",
            r"\geometry{left=2cm, right=2cm, top=2cm, bottom=2cm}",
            r"\usepackage{noto}",
            r"\usepackage{verbatim}",
            r"\begin{document}",
            r"\section*{Cifras Musicais}",
            r"\begin{verbatim}"
        ]
        for nome_secao, trechos in self.secoes.items():
            if not trechos:
                latex.append(f"{nome_secao}: (Vazia)")
                continue
            max_len = max(max(len(palavra), len(cifra)) for _, palavra, cifra in trechos)
            linha_cifras = []
            linha_palavras = []
            for _, palavra, cifra in sorted(trechos):
                linha_cifras.append(cifra.ljust(max_len))
                linha_palavras.append(palavra.ljust(max_len))
            latex.append(f"{nome_secao}:")
            latex.append(" ".join(linha_cifras))
            latex.append(" ".join(linha_palavras))
            latex.append("") 
        latex.extend([
            r"\end{verbatim}",
            r"\end{document}"
        ])
        return "\n".join(latex)

    def __str__(self):
       
        if not self.secoes:
            return "Nenhuma seção cadastrada."
        resultado = []
        for nome_secao, trechos in self.secoes.items():
            resultado.append(f"Seção {nome_secao}:")
            if not trechos:
                resultado.append("  (Vazia)")
            else:
                for pos, palavra, cifra in sorted(trechos):
                    resultado.append(f"  Posição {pos}: Palavra: {palavra}, Cifra: {cifra or 'Nenhuma'}")
        return "\n".join(resultado)