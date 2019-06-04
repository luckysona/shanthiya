N = int(input())
a1 = 1
a2 = 1
count = 0
while(count<N):
	print(a1,end=" ")
	a3 = a1+a2
	a1 = a2
	a2 = a3
	count = count+1
