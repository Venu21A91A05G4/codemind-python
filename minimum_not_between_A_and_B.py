n=int(input())
l=list(map(int,input().strip().split()))
a,b=map(int,input().strip().split())
c=0
k=[]
for i in range(n):
    if(l[i]<a or l[i]>b):
        c=1
        k.append(l[i])
print(min(k))if c else print("-1")


