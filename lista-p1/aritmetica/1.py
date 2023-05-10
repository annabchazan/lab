"""Escreva um programa que converte uma quantidade inteira de segundos
dados para dias, horas, minutos e segundos."""


seg=int(input("segundos"))

dias= seg//(60*60*24)
print(dias , "dias")

seg=seg-(dias*60*60*24)

horas = seg//(60*60)
print(horas , "horas")

seg=seg-(horas*60*60)

minu = seg//60
print(minu ,"minutos" )

seg = seg -(minu * 60)
print(seg , "segundos")
