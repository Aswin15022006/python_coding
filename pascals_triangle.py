n=int(input())
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    num=str(11**i)
    for k in num:
        print(k,end="")
    print()    
