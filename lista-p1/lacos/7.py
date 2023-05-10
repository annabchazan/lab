"""Escreva um programa que dado um inteiro positivo n, imprime o valor
de n!."""

n=int(input("número"))

i=1
s=0

while(i<=n):
    s=s+i
    i=i+1
print(s)