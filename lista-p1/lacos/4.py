"""Escreva um programa que lê n números e então imprime o menor
número lido."""

n=int(input("quantos números?"))
i=1
a=1
c=a
while(i<=n):
    b=a
    a=int(input("numero"))
    if(a<b):
        c=a
        
    else:
        c=c
        
    i=i+1
print(c)