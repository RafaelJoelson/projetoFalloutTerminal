from settings import escolher_senha, escolher_cheat
import random
def dar_feedback(palavra_correta, palavra_escolhida):
    feedback = ""
    for i in range(len(palavra_correta)):
        if palavra_correta[i] == palavra_escolhida[i]:
            feedback += palavra_correta[i]
        else:
            feedback += "_"
    return feedback
def carregar_palavras_do_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as file:
            palavras = [linha.strip() for linha in file.readlines()]
        return palavras
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado.")
        return []

def minigame_hacking():
    arquivo_palavras = "palavras.txt"
    palavras_originais = carregar_palavras_do_arquivo(arquivo_palavras)
    palavras = palavras_originais.copy()
    cheats_originais = ["<!=>","(*&!)","[]","<*&@>","(;-)","[#$!)%??]","(%*!@!!=;;)","[++&]","(%!($!])","<(!$#%_+>","<>","()"]
    cheats = cheats_originais.copy()
    texto_caotico = (
        f"?#%$#%%+&<{cheats.pop(random.randint(0, len(cheats) - 1))}<*&!#$!)%??;]@!!=;($!;{palavras.pop(random.randint(0, len(palavras) - 1))})!!$$%¨¨+¨&@){cheats.pop(random.randint(0, len(cheats) - 1))}(!!$*(][?@({palavras.pop(random.randint(0, len(palavras) - 1))})_&&**¨%*&!!!##@)[^!$$-%{cheats.pop(random.randint(0, len(cheats) - 1))}¨???$$¨¨&){palavras.pop(random.randint(0, len(palavras) - 1))}*(]#@#$@!!!#*/\n(~%{cheats.pop(random.randint(0, len(cheats) - 1))}?>]*&*!-(=$#!?;;#>{cheats.pop(random.randint(0, len(cheats) - 1))}<*/]=$;:@/*/#{palavras.pop(random.randint(0, len(palavras) - 1))}@$-=<[[*)%+~~<?]**%]?$!^;+^)!!?<{palavras.pop(random.randint(0, len(palavras) - 1))}%#=%#!_-~~^!$$-%<!-)[=/??>==$&&[$#>)[{palavras.pop(random.randint(0, len(palavras) - 1))}[¨?\n"
        f"%@[={cheats.pop(random.randint(0, len(cheats) - 1))}?$[!!)@{cheats.pop(random.randint(0, len(cheats) - 1))}*!@@{palavras.pop(random.randint(0, len(palavras) - 1))})[!!{cheats.pop(random.randint(0, len(cheats) - 1))}$@)#><*/(!*(!$*(%%($¨(%<{palavras.pop(random.randint(0, len(palavras) - 1))}%%*(:(!][([!>><*%$!<@%${palavras.pop(random.randint(0, len(palavras) - 1))}**!][==+_{cheats.pop(random.randint(0, len(cheats) - 1))}@~;?¨##*!/<,^{cheats.pop(random.randint(0, len(cheats) - 1))}¨"
        )
    senha_correta = escolher_senha(palavras_originais)
    tentativas_restantes = 4
    print("ENTER PASSWORD NOW:")
    print(f"{tentativas_restantes} ATTEMPT(S)")
    print(texto_caotico)
    while tentativas_restantes > 0:
        palavra_escolhida = input(">").upper()

        if palavra_escolhida == senha_correta:
            print(">Exact match!\n>Please wait while system accessed.")
            break
        else:
            tentativas_restantes -= 1
            feedback = dar_feedback(senha_correta, palavra_escolhida)
            print(f">Entry denied {feedback}")
            print(f">3 attempt(s) left: {tentativas_restantes}")

    if tentativas_restantes == 0:
        print("TERMINAL WAS BEEN BLOCKED - PLEASE CONTACT THE ADMINISTRATOR")