s=input()   
list=['a','e','i','o','u','A','E','I','O','U']
for i in s:
  if i in list:
    print("yes")
    break
else:
    print("no")
