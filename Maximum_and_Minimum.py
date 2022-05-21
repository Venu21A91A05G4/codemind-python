


a=int(input())
f=0
s=list(map(int,input().strip().split()))
k=[]
for i in range(a):
    c=0
    for j in range(a):
        if(s[i]==s[j]):
            c+=1
    if(c==s[i]):
        f=1
        k.append(s[i])
        s[i]=0
if(f==1):
    print(min(k),max(k))
else:
    print('-1')

