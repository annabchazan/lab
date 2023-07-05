n=int(input('num'))
questoes= 0
for i in range (1,n+1):
    p1=int(input(f" {i})1- sabe, 0-nao"))
    p2=int(input(f" {i})1- sabe, 0-nao"))
    p3=int(input(f" {i})1- sabe, 0-nao"))
    
    if((p1+p2+p3)>=2):
        questoes+=1
    else:
        questoes = questoes
print(f'podem responder {questoes} questoes')
