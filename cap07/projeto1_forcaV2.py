from random import sample
from os import system, name
import re

def limpa_tela():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")
        
def personagem(tent):
    estagios = [
        '''
        |========|
        |
        |
        |
        |
        ===
        ''',
         '''
        |========|
        |        0
        |
        |
        |
        ===
        ''',
        '''
        |========|
        |        0
        |        |
        |        |
        |
        ===
        ''',
        '''
        |========|
        |        0
        |       \|
        |        |
        |
        ===
        ''',
        '''
        |========|
        |        0
        |       \|/
        |        |
        |
        ===
        ''',
       '''
        |========|
        |        0
        |       \|/
        |        |
        |       /
        ===
        '''
        ,
        '''
        |========|
        |        0
        |       \|/
        |        |
        |       / \\
        ===
        '''
    ]
    print(estagios[tent])

def jogo_forca():
    limpa_tela()

    lista = ["abacaxi", "uva", "manga", "banana", "melancia", "laranja", "goiaba"]
    palavra = "".join(sample(lista, 1))
    tentativas = 6
    saida = ['_'] * tentativas
    letras_incorretas = []
    
    for i in range(tentativas):
        vez = input(f"Tentativa {i+1}: ").lower()
        while bool(re.match(r'^[a-zA-Z]$', vez)) != True:
            print("Dados inválidos, digite apenas um caractere de A a Z")
            vez = input(f"Tentativa {i+1}: ").lower()
            
        if vez in palavra:
            print(f"Letra CERTA\n")
            for x in range(len(palavra)):
                if palavra[x] == vez:
                    saida[x] = vez
        else:
            letras_incorretas.append(vez)
            print(f"Letra INCORRETA\n{letras_incorretas}\n")
        
        print("".join(saida))
        
        if "".join(saida) == palavra:
            print("Você ganhou!!!")
            quit()
            
        personagem(len(letras_incorretas))
            
        print(f"\nChances restantes: {tentativas - (i+1)}\n")

    print(f"Você perdeu D:, a palavra era {palavra}")   

jogo_forca()