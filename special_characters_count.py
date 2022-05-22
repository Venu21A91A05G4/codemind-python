s=0
for i in input():
    if(i.isupper() or i.islower() or i.isdigit() or i==' '):
        continue
    else:
        s+=1
print(s)
