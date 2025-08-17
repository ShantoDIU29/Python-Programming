#Example :print number from 1 to 5 using a while loop
num=1
while num <=5:
   print(num)
   num+=1
#Example:print a number from 1 to 10 and classify them as ever or odd
num=1;
while num<=10:
  if num%2==0:
    print(num,"is even")
  else:
    print(num,"is odd") 
  num+=1    
  
# Example: Print numbers from 1 to 5, skipping even numbers using a while loop with continue statement
num=1
while num<=5:
  if num%2==0:
    num+=1
    continue
  print(num)
  num+=1
# Example: Print numbers from 1 onwards until reaching a number greater than 5 using a while loop with break statement
num = 1

while True:
  print(num)
  if num>5:
    break
  num+=1