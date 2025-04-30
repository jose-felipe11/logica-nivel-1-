#18) Verificação de Nota - Peça ao usuário para digitar sua nota (0 a 

print("digite sua nota")
nota=float(input())
reprovado=nota<5
recuperaçao=nota <6.9>5
aprovado=nota>7
if reprovado :
    print("vc esta reprovado")
elif recuperaçao:
    print("vc esta de recuperacao ")
elif aprovado:
    print("vc esta aprovado")
