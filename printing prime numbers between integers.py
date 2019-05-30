r,s=input().split()
r=int(r)
s=int(s)
g=[]
for num in range(r+1,s):
  if(num>1):
    for j in range(2,num):
        if(num%j==0):
          break
    else:
       g.append(num)
print(*g)
