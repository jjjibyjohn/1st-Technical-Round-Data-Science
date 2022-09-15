##Q2

n = int(input())
while(n):
    if(n==0):
        break;
    R = 65536
    go = 1
    k=n
    while(k):
        s = input("Input command: ")
        p1,p2 = s.split(" ")
        t = int(p2)
        if(p1=='MUL'):
            if(go):
                if(t==0):
                    go=0
                else:
                    while(t%2==0):
                        t = t/2
                        R = R/2
        k=k-1
        n=k
    if(not(R) or not(go)):
        print("1\n")
    else:
        print(R,"\n")