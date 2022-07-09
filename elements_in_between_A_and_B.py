n=int(input())
l=list(map(int,input().strip().split()))
a,b=map(int,input().strip().split())
c=0
for i in range(n):
    if(l[i]>=a and l[i]<=b):
        c=1
        print(l[i],end=' ')
if(c==0):
    print("-1")

