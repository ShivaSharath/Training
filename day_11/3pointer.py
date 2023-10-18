def pointer(l,key):
    for i in range(len(l)):
        a=l[i]
        b=i+1
        c=len(l)-1
        dif=key-a
        while b<c:
            x=l[b]+l[c]
            if x<dif:
                b+=1
            elif x>dif:
                c-=1
            else:
                return a,l[b],l[c]
l=list(map(int,input().split()))
key=int(input())
print(pointer(l,key))
        
        