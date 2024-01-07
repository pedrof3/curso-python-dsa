operador = int(input("""Qual operação deseja realizar?
                     
    1 - Soma
    2 - Subtração
    3 - Multiplicação
    4 - Divisão
    
    Opções: (1/2/3/4): """))

while operador < 1 or operador > 4:
    operador = int(input("""DIGITE UMA OPÇÃO VÁLIDA!
                     
    1 - Soma
    2 - Subtração
    3 - Multiplicação
    4 - Divisão
    
    
    Opções: (1/2/3/4): """))
    
num1 = int(input("\nDigite o 1° número: "))
num2 = int(input("Digite o 2° número: "))

def resultado(op, n1, n2):
    if op == 1:
        return n1 + n2
    elif op == 2:
        return n1 - n2
    elif op == 3:
        return n1 * n2
    else:
        return n1 / n2
    
print(f"Resultado: {resultado(operador, num1, num2)}")