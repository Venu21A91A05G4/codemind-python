n,b=map(int,input().split())
a=list(str(n))
k=a[0:b]
m="".join(k)
a=a[::-1]
n=a[0:b]
n=n[::-1]
g="".join(n)
print(abs(int(m)-int(g)))


