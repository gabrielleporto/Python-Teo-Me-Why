import random

def get_input():
    while True:
        numero_usuario = int(input("Entre com um número: "))

        if 1 <= numero_usuario <= 15:
            return numero_usuario
        print("Valor inválido, o valor deve ser entre 1 e 15")

numero_sorteio = random.randint(1,15)

for i in range(3):

    numero_usuario = get_input()
    
    if numero_sorteio == numero_usuario:
        print("Você acertou")
        break
    elif numero_usuario > numero_sorteio:
        print("Número muito alto, tente um menor")
    else:
        print("Número muito baixo, tente um maior")
    
else:
    print("Suas tentativas acabaram!")
    