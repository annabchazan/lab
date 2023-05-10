"""Escreva um programa que lê números até que o número 0 seja dado e
informa se os números estavam em ordem crescente (excluindo o 0)."""

i=1
a=1

while(a!=0):
    b=a
    a=int(input("digite um número"))
   
    if(i!=2 and a>=b):
        print(i)
        i=1
    
    elif(a==0):
        i=i
    else:
        i=2
        print(i)

if(i==1):
    print(i)
    print("crescente")
else:
    print("nao")