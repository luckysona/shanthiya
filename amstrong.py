s = int(input())  
sum = 0  
temp = s  
while(temp > 0):  
   digit = temp % 10  
   sum += digit ** 3  
   temp=temp//10 
if(s == sum):  
   print("yes")  
else:  
   print("no")  
