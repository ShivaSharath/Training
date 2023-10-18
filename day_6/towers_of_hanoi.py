def toh(n,s,a,d):
    if n==0:
        return 
    toh(n-1,s,d,a)
    print(s,d)
    toh(n-1,a,s,d)
n=int(input())
toh(n,'A','B','C')