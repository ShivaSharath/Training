def quicksort(l,s,e):
    pi=l[e]
    i=s-1
    for j in range(s,e):
        if l[j]<pi:
            i=i+1
            l[i],l[j]=l[j],l[i]
    l[i+1],l[e]=l[e],l[i+1]
    return i+1
def quick(l,s,e):
    if s<=e:
        pi=quicksort(l,s,e)
        quick(l,s,pi-1)
        quick(l,pi+1,e)
l=list(map(int,input().split()))
quick(l,0,len(l)-1)
print(l)

