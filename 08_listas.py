gabi = ["Porto", "casada", 27, 1, True]
print(gabi[2])  #acessar elemento da lista (0, 1, 2...)

__________________________________________________

idades = [27, 25, 30, 22, 28]
print("Soma das idades:", sum(idades))
print("Média das idades:", sum(idades) / len(idades))

# [-1] : último elemento da lista
# [-2] : penúltimo elemento da lista...
# [0:4] : fatiar a lista do índice 0 ao 3

___________________________________________________

# quantas vezes o número que o usuário informou aparece na lista

lista = [1,2,3,3,3,2,1,1,1,1,1,5,6,7,7,6,5]

numero = int(input("Informe um número: "))

contador = 0
for i in lista:
    if i == numero:
        contador += 1
print("Quantidade de", numero, ":", contador)

___________________________________________________

# Iniciar com lista vazia, e o usuário criar

numeros = []

while True:
    numeros = input("Digite um número: ")
    if numeros == "":
        break

    numeros.append(int(numeros))  

print(numeros)