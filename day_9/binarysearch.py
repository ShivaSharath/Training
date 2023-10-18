def binarysearch(l,low,mid,high,key):
    if low>high:
        return -1
    mid=(low+high)//2
    if key==l[mid]:
        return mid
    if key>l[mid]:
        return binarysearch(l,mid+1,mid,high,key)
    if key<l[mid]:
        return binarysearch(l,low,mid,mid-1,key)
l=list(map(int,input().split()))
key=int(input())
print(binarysearch(l,0,0,len(l)-1,key)+1)