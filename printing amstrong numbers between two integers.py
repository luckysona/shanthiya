r,s=input().split()
r=int(r)
s=int(s)
l=[]
for num1 in range(r+1, s):
   sum = 0

   temp = num1
   while temp > 0:
       digit = temp % 10
       sum += digit ** 3
       temp //= 10
 
   if num1 == sum:
      l.append(sum)
print(*l)
