n=int(input())
temp=n
s=0
while(n):
    d=n%10
    s=s*10+d
    n=n//10
if(s==temp):
    print('True')
else:
    print('False')
