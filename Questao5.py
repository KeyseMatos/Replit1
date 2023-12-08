"13-Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido."

def semana(dias):
  if (dias == 1):
    print("Domingo")
  if (dias == 2):
    print("Segunda-feira")
  if (dias == 3):
    print("Terça-feira")
  if (dias == 4):
    print("Quarta-feira")
  if (dias == 5):
    print("Quinta-feira")
  if (dias == 6):
    print("Sexta-feira")
  if (dias == 7):
    print("Sábado")

dias= int(input("Informe um número correspondente aos dias da semana: "))
semana(dias)