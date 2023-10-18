def rotate(l,k):
    b=[0 for i in l]
    a=len(l)-k
    for i in range(k):
        if k<1:
            return l
        else:
            b[i]=l[a-1]
            a-=1
    for i in range(a-k):
        b[k]=a[i]
    return b
l=list(map(int,input().split(" ")))
k=int(input())
print(rotate(l,k)) 