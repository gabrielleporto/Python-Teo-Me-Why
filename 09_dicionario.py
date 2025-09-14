# pares de chaves/valor
# as chaves podem ser str e int

dados_gabrielle = {
    "sobrenome": "porto",
    "filhos":True,
    "Formacao": "Fono",
    "Trabalhos":[
        {"Artista": "tatuagem"},
        {"Artista2": "Pintora de quadros"},
        {"Fono": "Audiologista", "ultima empresa": "Dore"}
    ]
}

print(dados_gabrielle["Formacao"])
print(dados_gabrielle["Trabalhos"][-1]["ultima empresa"])

# descobrir apenas as chaves : print(dados_gabrielle.keys())
# descobrir apenas os valores : print(dados_gabrielle.values())

for chave, valor in dados_gabrielle.items():
    print(chave, ":", valor)


# tuplas: são listas que não podem ser alteradas, a não ser que 
#seja uma lista dentro da tupla

___________________________________________________________________

# exercício
fruta = input("Entre com o nome de uma fruta")

frutas = {
    "pera": "1,50",
    "goiaba": "2,20",
    "laranja": "1,75",
    "mamão": "2,15",
    "limão": "0,80",
}

if fruta in frutas:
    print(frutas[fruta])
else:
    print("Entre com um valor válido")

################################################