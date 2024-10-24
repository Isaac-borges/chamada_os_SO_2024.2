import os

def main():
    nome_dir: str = input('Nome do diretorio: ').strip()
    nome_arq: str = input('Nome do arquivo: ').strip()
    mensagem: str = input(f'Digite a mensagem a ser inserida dentro de {nome_arq}: ')
    mk_dir_and_file(nome_dir, nome_arq, mensagem)

def mk_dir_and_file(diretorio: str, n_arquivo: str, conteudo: str):
    
        if not os.path.exists(diretorio):
            os.makedirs(diretorio)
        
        caminho = os.path.join(diretorio, n_arquivo)

        with open(caminho, 'w') as arquivo:
            arquivo.write(conteudo)

        print(f'[{caminho}] criado.')
        


main()
