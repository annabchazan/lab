"""Escreva um programa que lê n números e então imprime o menor
número lido."""

n=int(input("quantos números?"))
i=1
c=0

while(i<=n):
    a=int(input("numero"))
    c=c+a
    i=i+1
print(c/n)