n=int(input())
for i in range(n):
    a=input()
    r=a[::-1]
    if a!=r:
        print("NO")
    elif(a==r and len(a)%2==0):
        print("YES EVEN")
    else:
        print("YES ODD")