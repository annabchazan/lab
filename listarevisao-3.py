x = 1
valores = []

while x !=0:
    x = int(input('valor'))
    valores.append(x)

tam = len(valores)-1

for i in range (tam):
    I = valores[i]//50
    i= valores [i] - 50*I

    J = (i)//10
    j= i - 10 * J

    K = (j )//5
    k = j - 5*K

    L = (k)//10

    print(f'Tesete {i} \n {I} , {J} , {K}, {L} \n')
