#14) Ler um valor e escrever a mensagem É MAIOR QUE 10! se o valor lido for maior que 10, caso contrário escrever NÃO É MAIOR QUE 10!
print("digite um numero")
numero=int(input())
exato=numero==10
abaixo=numero<10
emcima=numero>10
if emcima:
    print("este numero e maior que 10!!")
elif abaixo:
    print("ESTE NUMERO E MENOR QUE 10!!!!")
elif exato:
    print("este numero e 10")
