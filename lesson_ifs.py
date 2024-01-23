print(2+4)
print (type(10/4))
x=5
y=x**5
print (y)
print (type(y))
a="hi"
print(a*4)

b='HEHEHE'
print(a,' ', b)
print(a[0:4])
print(f"our string has {len(a) } characters")
print(2==2)
print (True+ True)
#Multiple logical statements
print(1==1 and 1==2)
print(1==1 or 1==1)

myList=[1,2,3,4,5,6,7,8,9,10]
print(type(myList))# <classe 'list'>
print(myList[0:5])#1
print(  len(myList))

print(f"our lists has {len(myList) } elements")

mixList =  [1,2, myList]
print(mixList)
mixList.append(6)
mixList.pop()
print(mixList)

import random
number=random.randint(1,10)
print(number)
#if statements  
if number<1:
  print('hi')
elif number>=1:
  print('ooo')
else :
  print("WHAT")
number2=random.randint(10,20)
#nested if statements
print(number,number2)
if number<9:
  if number2<19:
    print("unluck")
  else:
    print("LUCCC")
else :
  print('LUCk')
if number<9 and number2<19:
  print('TTJEJINogsnslgfjdpsgjfgn')

















