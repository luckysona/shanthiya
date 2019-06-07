n=int(input())
n1=list(map(int,input().split()))
total=len(n1)
ans =sum(n1)
if(ans>0):
  result=ans/n
print(result)
