#20) Ler 3 valores (considere que não serão informados valores iguais) e escrever a soma dos 2 maiores

print("digite tres numero")
print("digite o primeiro numero")
n1=int(input())
print("digite o segundo numero")
n2=int(input())
print("digite o terceiro numero")
n3=int(input())
n1m=n1<n2 and n1<n3
n2m=n2<n3 and n2<n1

if n1m:
    print("soma dos dois maiores " ,n2+n3)
elif n2m:
    print("soma dos dois maiores", n1+n3)
else:
    print("soma dos dois maiores" ,n2+n1)
