def prime(a):
    c=0
    for i in range(1,a+1):
        if(a%i==0):
            c+=1
        if(c>2):
            break
    if(c==2):
        return 1
    else:
        return 0
a=int(input())
b=int(input())
s=a+b
i=s+1
while(1):
    if(prime(i)):
        print(abs(s-i))
        break
    i+=1