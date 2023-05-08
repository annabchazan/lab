n=int(input('n'))
k=int(input('k'))
lista=[]
for i in range(1,n,2):
    lista.append(i)

for x in range(2,n,2):
    lista.append(x)

print(lista)
print(lista[k-1])
