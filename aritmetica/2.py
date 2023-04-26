"""Escreva um programa que dados uma quantidade inteira de dias, horas,
minutos e segundos nos diz a quantidade total de segundos"""

dias=int(input("dias"))
horas=int(input("horas"))
minu = int(input("minutos"))
segundos = int(input("segundos"))


seg=(dias*60*60*24) + (horas*60*60) + (minu * 60) + segundos

print(seg)