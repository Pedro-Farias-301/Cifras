Sistema de Cifras Musicais
Um aplicativo Python para músicos que desejam gerenciar letras de músicas com suas cifras musicais (acordes) de forma organizada. O sistema permite adicionar, modificar e apagar trechos de letras com cifras, organizá-los em seções (estrofes/refrões), realizar edição em massa, exportar para PDF e usar uma interface gráfica amigável.
Funcionalidades

Gerenciamento de Seções: Suporte para estrofes, refrões ou outras seções da música.
Adição de Trechos: Associe cifras (ex.: C, Am, G7) a palavras ou sílabas da letra.
Edição Individual e em Massa: Modifique cifras de um trecho específico ou de vários trechos de uma vez.
Visualização: Exibe cifras acima das palavras, como em um cifrado de partitura.
Persistência: Salve e carregue músicas em arquivos JSON.
Exportação para PDF: Gere arquivos PDF com as cifras e letras formatadas usando LaTeX.
Interface Gráfica: Interface amigável com tkinter para facilitar a edição.

Pré-requisitos

Python 3.6+: Necessário para executar o programa.
tkinter: Biblioteca para a interface gráfica (geralmente incluída, mas pode requerer instalação em Linux).
LaTeX: Para exportação de PDF (recomenda-se texlive-full e latexmk).
Sistema operacional: Testado em Linux (Ubuntu), mas compatível com Windows e macOS.

Instalação

Clone o repositório:
git clone https://github.com/seu-usuario/sistema-cifras-musicais.git
cd sistema-cifras-musicais


Instale o Python 3 (se não estiver instalado):

Ubuntu/Debian:sudo apt update
sudo apt install python3


Windows/macOS: Baixe do site oficial do Python.


Instale o tkinter (necessário para a interface gráfica):

Ubuntu/Debian:sudo apt install python3-tk


Windows/macOS: Geralmente incluído no Python.


Instale o LaTeX (para exportação de PDF):

Ubuntu/Debian:sudo apt install texlive-full latexmk


Para uma instalação menor:sudo apt install texlive texlive-fonts-extra latexmk




Verifique os arquivos:Certifique-se de que os seguintes arquivos estão no diretório:

cifras_musicais.py: Lógica principal do sistema.
interface_grafica.py: Interface gráfica com tkinter.
main.py: Interface de linha de comando (opcional).



Uso
Interface Gráfica

Execute o programa:python3 interface_grafica.py


Na interface:
Adicionar Seção: Insira o nome (ex.: "Estrofe 1") e clique em "Adicionar Seção".
Adicionar Trecho: Insira a seção, palavra/trecho e cifra, e clique em "Adicionar Palavra/Cifra".
Modificar Cifra: Insira a seção, posição e nova cifra, e clique em "Modificar Cifra".
Edição em Massa: Insira a seção, posições (ex.: "1,2,3") e nova cifra, e clique em "Modificar em Massa".
Apagar: Insira a seção e posição, e clique em "Apagar Palavra/Cifra".
Exibir: Clique em "Atualizar Exibição" para ver as cifras acima das palavras.
Salvar/Carregar/Exportar: Use os botões para gerenciar arquivos JSON ou exportar para PDF.



Interface de Linha de Comando

Execute:python3 main.py


Siga o menu interativo para adicionar seções, trechos, modificar cifras, etc.

Exemplo de Saída
Ao adicionar trechos à "Estrofe 1":
Estrofe 1:
G      C     
Sol    brilha

Exportação para PDF

Use a opção "Exportar para PDF" na interface gráfica ou o menu de linha de comando.
Exemplo de saída no PDF:Estrofe 1:
G      C
Sol    brilha



Estrutura do Projeto

cifras_musicais.py: Contém a classe CifrasMusicais com a lógica para gerenciar seções, trechos e cifras.
interface_grafica.py: Interface gráfica usando tkinter.
main.py: Interface de linha de comando para interação via terminal.
README.md: Este arquivo, com instruções do projeto.

Contribuição

Faça um fork do repositório.
Crie uma branch para sua feature:git checkout -b minha-feature


Faça commit das suas alterações:git commit -m "Adiciona minha feature"


Envie para o repositório remoto:git push origin minha-feature


Abra um Pull Request no GitHub.

Sugestões de melhorias:

Suporte para múltiplas linhas por seção.
Validação avançada de acordes (ex.: Cmaj7, Bb).
Exportação para formatos de imagem (ex.: PNG).

Licença
Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para detalhes.
Contato
Para sugestões ou problemas, abra uma issue no repositório ou entre em contato com pedrobarbosafarias9696@gmail.com.
