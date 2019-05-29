A=int(input())
if(A>0):
  for i in range(2,A//2):
    if(A%i==0):
      print("no")
      break
  else:
    print("yes")
else:
  print("no")
