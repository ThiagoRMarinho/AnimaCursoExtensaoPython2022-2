print("Início da aula 03 (09/11/2022)")

contador = 1

#exibir de 1 até 10 repetidamente
while(contador <= 10):
  print (contador)
  contador = contador + 1 

#Laço for (python for= for each)

fruta = "morango"
print(fruta)

fruta1 = "morango"
fruta2 = "Laranja"
fruta3 = "Pêra"

#Lista
frutas = ["morango", "laranja", "pêra"]

#quero exibir apenas a 3a. fruta (pêra)
print(frutas[2])

#Exibir quantas frutas tem na minha lista?
print(len(frutas)) #length = tamanho

#Inculir nova fruta
frutas.append("manga")

print(len(frutas)) #length = tamanho
print(frutas)

print(frutas[0])
print(frutas[1])
print(frutas[2])
print(frutas[3])

print("Exemplo das frutas com While")
frutas.append("uva")

i=0 #(i de index)
while(i<len(frutas)):
  print(frutas[i])
  i = i + 1

print ("Exemplo das frutas com FOR")
for fruta in frutas:
  print(fruta)



