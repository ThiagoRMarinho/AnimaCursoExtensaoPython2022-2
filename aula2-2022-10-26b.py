#Pede o nome do aluno e sua nota (0 a 10) e, se ele tirou nota 10, mostra "parabéns"

nome = input("Informe seu nome: ")
nota = float(input("Informe sua nota: "))

if nota == 10:
  print(f"{nome}, Parabéns")
elif (nota >=6 and nota < 10):
  print(f"{nome}, bom trabalho")
elif (nota > 10):
  print("nota incorreta")
else:
  print ("tente de novo")

