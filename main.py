from cifras_musicais import CifrasMusicais

def main():
    cifras = CifrasMusicais()
    
    while True:
        print("\n=== Sistema de Cifras Musicais ===")
        print("1. Adicionar nova seção (estrofe/refrão)")
        print("2. Adicionar palavra e cifra a uma seção")
        print("3. Modificar cifra de uma palavra")
        print("4. Modificar cifras em massa")
        print("5. Apagar palavra e cifra")
        print("6. Exibir música com cifras")
        print("7. Salvar música em arquivo")
        print("8. Carregar música de arquivo")
        print("9. Exportar para PDF")
        print("10. Sair")
        
        opcao = input("Escolha uma opção (1-10): ")
        
        if opcao == "1":
            nome_secao = input("Digite o nome da seção (ex.: Estrofe 1, Refrão): ")
            if cifras.adicionar_secao(nome_secao):
                print(f"Seção '{nome_secao}' adicionada!")
            else:
                print(f"Seção '{nome_secao}' já existe.")
                
        elif opcao == "2":
            nome_secao = input("Digite o nome da seção: ")
            palavra = input("Digite a palavra ou trecho da letra: ")
            cifra = input("Digite a cifra musical (ex.: C, Am, G7) ou deixe vazio: ")
            try:
                cifras.adicionar_palavra_cifra(nome_secao, palavra, cifra)
                print(f"Palavra '{palavra}' com cifra '{cifra or 'Nenhuma'}' adicionada em '{nome_secao}'!")
            except ValueError as e:
                print(f"Erro: {e}")
                
        elif opcao == "3":
            nome_secao = input("Digite o nome da seção: ")
            try:
                posicao = int(input("Digite a posição da palavra a modificar (1, 2, 3...): "))
                nova_cifra = input("Digite a nova cifra (ex.: C, Am, G7) ou deixe vazio: ")
                cifras.modificar_cifra(nome_secao, posicao, nova_cifra)
                print(f"Cifra na posição {posicao} de '{nome_secao}' modificada para '{nova_cifra or 'Nenhuma'}'!")
            except ValueError as e:
                print(f"Erro: {e}")
                
        elif opcao == "4":
            nome_secao = input("Digite o nome da seção: ")
            posicoes_str = input("Digite as posições a modificar (ex.: 1,2,3): ")
            nova_cifra = input("Digite a nova cifra (ex.: C, Am, G7) ou deixe vazio: ")
            try:
                posicoes = [int(p) for p in posicoes_str.split(",")]
                cifras.modificar_cifras_em_massa(nome_secao, posicoes, nova_cifra)
                print(f"Cifras nas posições {posicoes} de '{nome_secao}' modificadas para '{nova_cifra or 'Nenhuma'}'!")
            except ValueError as e:
                print(f"Erro: {e}")
                
        elif opcao == "5":
            nome_secao = input("Digite o nome da seção: ")
            try:
                posicao = int(input("Digite a posição da palavra a apagar (1, 2, 3...): "))
                cifras.remover_palavra_cifra(nome_secao, posicao)
                print(f"Palavra e cifra na posição {posicao} de '{nome_secao}' removidas!")
            except ValueError as e:
                print(f"Erro: {e}")
                
        elif opcao == "6":
            print("\n" + cifras.exibir_musica())
            
        elif opcao == "7":
            nome_arquivo = input("Digite o nome do arquivo para salvar (ex.: musica.json): ")
            try:
                cifras.salvar_em_arquivo(nome_arquivo)
                print(f"Música salva em {nome_arquivo}!")
            except Exception as e:
                print(f"Erro ao salvar: {e}")
                
        elif opcao == "8":
            nome_arquivo = input("Digite o nome do arquivo para carregar (ex.: musica.json): ")
            try:
                cifras.carregar_de_arquivo(nome_arquivo)
                print(f"Música carregada de {nome_arquivo}!")
            except Exception as e:
                print(f"Erro ao carregar: {e}")
                
        elif opcao == "9":
            nome_arquivo = input("Digite o nome do arquivo PDF (ex.: musica.pdf): ")
            try:
                cifras.exportar_pdf(nome_arquivo)
                print(f"Música exportada para {nome_arquivo}!")
            except Exception as e:
                print(f"Erro ao exportar: {e}")
                
        elif opcao == "10":
            print("Saindo do programa...")
            break
            
        else:
            print("Opção inválida! Escolha um número entre 1 e 10.")

if __name__ == "__main__":
    main()