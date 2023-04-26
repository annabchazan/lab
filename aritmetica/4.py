"""Escreva um programa que dado um valor em reais, imprime quais e
quantas notas devem ser usadas para obter tal valor utilizando o menor
número de notas possível. Por exemplo, se o valor é R$ 746 então você
pode usar três notas de R$ 200, uma nota de R$ 100, duas notas de
R$ 20, uma de R$5 e uma de R$1, em um total de 8 notas. Tente se
convencer que o seu algoritmo está correto."""




a=int(input())

n100=(a//100)
b=a-(n100*100)
print(n100 ,  "nota(s) de R$ 100,00")

n50=(b//50)
c=b-(n50*50)
print(n50 , "nota(s) de R$ 50,00")


n20=(c//20)
d=c-(n20*20)
print(n20 ,  "nota(s) de R$ 20,00")


n10=(d//10)
e=d-(n10*10)
print(n10 ,  "nota(s) de R$ 10,00")


n5=(e//5)
f=e-(n5*5)
print(n5 ,   "nota(s) de R$ 5,00")


n2=(f//2)
g=f-(n2*2)
print(n2 ,  "nota(s) de R$ 2,00")

n1=(g//1)
print(n1,  "nota(s) de R$ 10,00")

print(n100 + n50 + n20 + n10 + n5 + n2 , "notas no total") 