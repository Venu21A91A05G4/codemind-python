s=input()
c=0
f=0
for i in range(len(s)):
    if s[i].isdigit():
        c=c+1
        f=1
print("Contains %d digit"%c) if f==1 else print("Doesn't contain digit")
