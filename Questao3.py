'3-Faça um Programa que verifique se uma letra digitada é F ou M. Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.'
letra= input("Informe a letra que represente o seu sexo: ")
if letra == "F" or letra =="f":
  print("Sexo Feminino")
elif letra == "M" or letra == "m":
  print("Sexo Masculino")
else :
  print("Sexo Inválido")
