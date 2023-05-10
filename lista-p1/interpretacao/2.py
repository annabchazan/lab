x=int(input('x'))
passos=0


while(x>0):
    if(x>5):
        x=x-5
        passos+=1
    if(x>5):
        x=x-5
        passos+=1
    elif(x>4):
        x=x-4
    
    elif(x>3):
        x=x-3
        passos += 1
    
    elif(x>2):
        x=x-2
        passos += 1
    elif(x>1):
        x=x-1
        passos +=1
    else:
        x=0
        print(passos)