def par_impar(numero:int)
    if numero % 2 == 0:
        print("É par")
    else:
        print("É impar")

numero = input("Entre com um número: ")
numero = int(numero)

par_impar(numero)

____________________________________________________

def soma(a: float, b:float):     #*args - elementos opcionais
    return a + b

def media(a:float, b:float):
    return soma / 2

a = float(input("entre com o valor de a"))
b = float(input("entre com o valor de b"))

print("Média:", media(a,b))

##############################################