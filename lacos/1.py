"""Escreva um programa que lê números até que o número 0 seja dados e
então imprime quantos números dados eram positivos e quantos eram
negativos."""




i=0
x=0
a=1

while(a!=0):
    a=int(input("digite um número"))
    if(a>0):
        i=i+1
    else:
        x=i+1

print(i, 'números positivos')
print(x , "números negativos")