from settings import escolher_senha
import msvcrt
import sys
def carregar_palavras_do_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as file:
            palavras = [linha.strip() for linha in file.readlines()]
        return palavras
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado.")
        return []

def verify_credentials(senha_inf):
    arquivo_palavras = "palavras.txt"
    palavras_originais = carregar_palavras_do_arquivo(arquivo_palavras)
    login = "ADMINISTRATOR"
    senha = escolher_senha(palavras_originais)

def getpass_windows(prompt=">"):
    senha = ""
    sys.stdout.write(prompt)
    sys.stdout.flush()

    while True:
        char = msvcrt.getch().decode("utf-8")
        if char == "\r" or char == "\n":
            break
        elif char == "\b":
            senha = senha[:-1]
        else:
            senha += char
            sys.stdout.write("*")
            sys.stdout.flush()

    sys.stdout.write("\n")
    return senha