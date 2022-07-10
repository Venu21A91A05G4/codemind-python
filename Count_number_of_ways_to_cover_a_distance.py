def d(n):
    if n<0:
        return 0
    elif n==0:
        return 1
    else:
        return (d(n-1)+d(n-2)+d(n-3))
n=int(input())
print(d(n))

