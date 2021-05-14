n=int(input())
temp=n
f=l=0
nn=0
c=0
d=0
while n:
    r=n%10
    n=n//10
    c+=1
n=temp
c=d=c-1
if n>0:
    f=n//pow(10,c)
    l=n%10
while n:
    r=n%10
    n=n//10
    if c==d:
        r=f
    elif c==0:
        r=1
    nn=nn*10+r
    c=c-1
print(nn)
        
