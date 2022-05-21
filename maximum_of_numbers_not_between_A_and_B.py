a=int(input())
k=list(map(int,input().strip().split()))
s=[]
f=0
m,n=map(int,input().split())
for i in range(a):
    if(k[i]<m):
        f=1
        d=k[i]
        s.append(d)
    elif(k[i]>n):
        f=1
        d=k[i]
        s.append(d)
if(f==0):
    print("-1")
else:
    print(max(s))
