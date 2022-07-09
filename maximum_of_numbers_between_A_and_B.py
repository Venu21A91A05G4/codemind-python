n=int(input())
l=list(map(int,input().strip().split()))
a,b=map(int,input().strip().split())
k=[]
c=0
for i in range(n):
    if(l[i]>=a and l[i]<=b):
        c=1
        k.append(l[i])
print(max(k))if c==1 else print("-1")



