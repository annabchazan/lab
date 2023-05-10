n=int(input("num"))
k=int(input("k vezes"))
ns = str(n)
tamanho= len(str(n))



for x in range (0, k, 1):
    if(ns[tamanho-1]!='0'):
        n=n-1
    else:
        n = n/10
print(n)