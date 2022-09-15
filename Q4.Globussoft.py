##Q4

N = int(input("Enter number of corners: "))
if(N==0):
    pass
else:
    x=[]
    y=[]
    for i in range(N):
        t = input("Enter x,y cordinate: ")
        x.append(int(t.split(" ")[0]))
        y.append(int(t.split(" ")[1]))
    
    x1 = x[:]
    y1 = y[:]
    
    m = x1.pop(0)
    n = y1.pop(0)
    result = []
    a = m
    b = n
    j=0
    while(len(x1)):
        k = x1[j]
        l = y1[j]
        if((k-m)==0):
            g = l-n
            if(g>0):
                result.append('N')
            else:
                result.append('S')
            m = x1.pop(j)
            n = y1.pop(j)
            j=0
                    
        elif((l-n)==0):
            g = k-m
            if(g>0):
                result.append('E')
            else:
                result.append('W')
            m = x1.pop(j)
            n = y1.pop(j)
            j=0
            
        else:
            j=j+1
            
    if((m-a)==0):
            g = b-n
            if(g>0):
                result.append('N')
            else:
                result.append('S')
    elif((n-b)==0):
            g = a-m
            if(g>0):
                result.append('E')
            else:
                result.append('W')
                
    print(''.join(result))