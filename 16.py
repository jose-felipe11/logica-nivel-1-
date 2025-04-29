#16) As maçãs custam R$1,30 cada se forem compradas menos de uma dúzia, e R$1,00 se forem compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas, calcule e escreva o custo total da compra.
print("digite o numero de maças ")
maca=int(input())
menos= maca<12
mais= maca>12
if menos:
    print("o valor das sua maças e" , maca *1,30)
elif mais:
    print("o valor das suas maças e", maca *1)
