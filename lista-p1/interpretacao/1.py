
cores = []
cores_diferentes=[]
meias=0
for x in range (0,4):
    cores.append(int(input(f'cor {x}: ')))
meias =0 

for c in cores:
    if c not in cores_diferentes:
        cores_diferentes.append(c)
print(4-(len(cores_diferentes)))