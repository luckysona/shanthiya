num1=int(input())
num2=[int(x) for x in input().split()]
num2.sort()
me=len(num2)//2
print(num2[me])
