l,m=input().split()
l=int(l)
m=int(m)
Even=[]
for i in range(l+1,m):
    if(i%2==0):
        Even.append(i)
print(*Even)
