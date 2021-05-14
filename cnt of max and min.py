n=int(input())
max=n%10
min=n%10
c1,c2=0,0
while n:
    r=n%10
    n=n//10
    if r>max:
        max=r
        c1=1
    elif max==r:
        c1+=1
    if r<min:
        min=r
        c2=1
    elif min==r:
        c2+=1
print(max,min)
print(c1,c2)
        
