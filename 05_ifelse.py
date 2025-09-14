agua = input("Você deseja água com gás ou sem gás? ")
if str(agua) == "sem gás":
    print("Você pagará 1.50")
elif str(agua) == "com gás":
    print("Você pagará 2.50")
else:
    print("Você não escolheu nenhuma opção.")


# texto = """ escolha sua água:
# (1) água sem gás
# (2) água com gás
# """
# opcao = input(texto)
# conta = 0
# if opcao == "1":
#     conta = 1.50
# elif opcao == "2":
#     conta = 2.50
# if conta == 0:
#     print("Você não escolheu nenhuma opção.")
# else:
#     print("Sua conta é R$", conta)