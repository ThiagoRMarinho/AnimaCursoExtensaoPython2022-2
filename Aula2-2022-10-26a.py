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

#Estrutura condicional-"if"
#se a pessoa for maior de idade, mostre: "Você é maior de idade,ótimo! Ja pode beber ou dirigir."
if (idade >= 18): 
  print ("Você é maior de idade,ótimo! Ja pode beber ou dirigir")
else:
  print ("Você não é maior de idade")

#E seu eu quisesse perguntar o gênero (M= MASCULINO E F= FEMININO)
#e você também precisa ou precisou prestar serviço militar

genero = input ("Informe seu genêro: M= Masculino, F= Femino, O= Outros: ")

if idade>=18 and genero == "M":
  print ("... e você também precisa/precisou prestar o serviço militar obrigatório")  

else:
  print ("Você não precisa prestar o serviço militar")

  