"9-Faça um Programa que leia três números e mostre-os em ordem decrescente."

n1= int(input("Informe o 1° número: "))
n2= int(input("Informe o 2° número: "))
n3= int(input("Informe o 3° número: "))

if (n1 < n2 or n1 < n3):
  p1= n1
if (n2 < n3 or n2 < n1):
  p2= n2
if (n3 < n2 or n3 < n1):
  p3= n3

print("Os números em ordem decrescente são: ",p1)
print("Segundo",p2)
print("Terceiro",p3)