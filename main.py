# comando input(): quero permitir que o usuário digite algo. 
nome = input("Digite seu nome: ")

#pede a idade do usário "Qual sua idade?"
idade = int(input("Qual sua idade: "))

#comando de saída...exibir na tela 
print (f"Boa noite, seu nome é {nome}")

#exiba "Sua idade é:" 
print (f"Sua idade é {idade}")

#dobro da idade
dobro = idade *2

print("O dobro da idade informada é {}".format(dobro))