a=input()
count=0
for j in a:
  if j.isnumeric()!=True:
    if j.isalpha()!=True:
      count=count+1
print(count)
