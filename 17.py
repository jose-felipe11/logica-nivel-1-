#17) Classificação de Idade - Peça ao usuário sua idade e classifique da seguinte forma:
#Menor de 12 anos: Criança
#Entre 12 e 17 anos: Adolescente
#Entre 18 e 59 anos: Adulto
#60 anos ou mais: Idoso
print("digite sua idade")
idade=int(input())
criança=idade<=12
adolesente=idade <17>13
adulto=idade<59>18
idoso=idade>=60
if criança :
    print("vc e uma criança")
elif adolesente:
    print("vc e um adolecente")
elif adulto:
    print("vc e um adulto")
elif idoso :
    print("vc e um idoso")
