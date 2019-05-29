R,S=input().split()
R=int(R)
S=int(S)
list=[]
for i in range(R+1,S):
    if(i%2!=0):
        list.append(i)
print(*list)
