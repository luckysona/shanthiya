N,K=input().split()
N=int(N)
K=int(K)
digitlist=list(map(int,input().strip().split()))
sum=0
for num in range(1,K+1):
    sum=sum+num
print(sum)
