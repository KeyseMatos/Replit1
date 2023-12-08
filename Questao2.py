'1-Crie um programa no qual o usuário deverá inserir os valores da altura, largura e profundidade de uma caixa d’água, em cm. No final, exiba o volume dessa caixa d’água. Dica: Volume = Altura x Largura x Profundidade'
altura= float(input("Informe a altura da caixa d´água em cm: "))
print(altura)
largura= float(input("Informe a largura da caixa d´água em cm: "))
print(largura)
profundidade= float(input("Informe a profundidade da caixa d´água em cm: "))
print(profundidade)

volume= altura * largura * profundidade

print("O volume da caixa d' água é: ", volume , "cm")