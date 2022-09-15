##Q3

import numpy as np
arr = [[1 for i in range(5)] for j in range(5)]
ply = 0
print("Initial Board:\n", np.matrix(arr))
while(1):
    if(ply%2==0):
        print("\n\nPlayer 1 turn \n")
    else:
        print("\n\nPlayer 2 turn \n")
        
    while(1):
        r = int(input("Select the row: "))
        c = int(input("Select the col: "))
        k1 = r
        k2 = c
        if(r>0 and r<6):
            if(c>0 and c<6):
                if(arr[r-1][c-1]==0):
                    print("Block already removed..\n")
                    print('Try again:')
                    continue
                else:
                    arr[r-1][c-1]=0
                    break
            else:
                print("Try again: ")
                continue
        else:
            print("Try again: ")
            continue
        break
      
    while(1):
        m = input("Do you want to take more (Y/N): ")
        if(m=='y' or m=='Y'):
            m2 = input("Do you want to take from row or col (R/C): ")
            if(m2=='R' or m2=='r'):
                while(1):
                    j = 0
                    for p in range(5):
                        j = j + arr[r-1][p]
                    if(j==0):
                        print('Nothing more in row to take!')
                        break
                    m3 = int(input("Enter the number for the column to be removed: "))
                    if(abs(m3-c)==1 or abs(m3-k2)==1):
                        arr[r-1][m3-1]=0
                    else:
                        print('Try again:')
                        continue
                    k2 = m3
                    e = input("Take more? (Y/N): ")
                    if(e=='N' or e=='n'):
                        break
                    
            elif(m2=='C' or m2=='c'):
                while(1):
                    j = 0
                    for p in range(5):
                        j = j + arr[p][c-1]
                    if(j==0):
                        print('Nothing more in col to take!')
                        break
                    m3 = int(input("Enter the number for the row to be removed: "))
                    if(abs(m3-c)==1 or abs(m3-k1)==1):
                        arr[m3-1][c-1]=0
                    else:
                        print('Try again:')
                        continue
                    k1 = m3
                    e = input("Take more? (Y/N): ")
                    if(e=='N' or e=='n'):
                        break

        else:
            print("Try again: ")
            continue

        break
                  
    d=0
    for i in range(5):
        for j in range(5):
            d=d+arr[i][j]
    if(d==0):
        print("\n\nlosing")
        break
    elif(d==1):
        print("\n\nwinning")
        break
    ply = ply + 1
    
    print("\n\nBoard after the move:\n", np.matrix(arr))