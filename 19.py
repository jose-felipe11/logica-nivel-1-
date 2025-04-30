#19) Ler 3 valores (considere que não serão informados valores iguais) e escrever o maior deles.

print("digite tres numero")
print("digite o primeiro numero")
n1=int(input())
print("digite o segundo numero")
n2=int(input())
print("digite o terceiro numero")
n3=int(input())
n1m=n1>n2 and n1>n3
n2m=n2>n3 and n2>n1

if n1m:
    print("numero maior " ,n1)
elif n2m:
    print("numero maior", n2)
else:
    print("numero maior" ,n3)
