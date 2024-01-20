from random import sample
import re

lista = ["abacaxi", "uva", "manga", "banana", "melancia", "laranja", "goiaba"]
palavra = "".join(sample(lista, 1))

def jogo_forca(palavra):
    tentativas = len(palavra)
    saida = ['_'] * tentativas
    
    for i in range(tentativas):
        vez = input(f"Tentativa {i+1}: ").lower()
        while bool(re.match(r'^[a-zA-Z]$', vez)) != True:
            print("Dados inválidos, digite apenas um caractere de A a Z")
            vez = input(f"Tentativa {i+1}: ").lower()
            
        if vez in palavra:
            print(f"Letra certa\n")
            for x in range(len(palavra)):
                if palavra[x] == vez:
                    saida[x] = vez
        else:
            print("Letra incorreta\n")
        
        print("".join(saida))
        
        if "".join(saida) == palavra:
            print("Você ganhou!!!")
            quit()
            
        print(f"\nChances restantes: {tentativas - (i+1)}\n")
    
    print(f"Você perdeu D:, a palavra era {palavra}")   
        
jogo_forca(palavra)