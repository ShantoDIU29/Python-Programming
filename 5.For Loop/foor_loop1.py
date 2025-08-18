#range([start],stop[,step])
#Example 1:range with only stop argument
for i in range(5):
  
   print(i)#outpu:0,1,2,3,4
 
print("next")  
#Example 2:range with start and stop arguments
for i in range(2,5):
  print(i)
#Example 3:range with start,stop,and step arguments
for i in range(1,10,2):
  print(i)
# Example: Print numbers from 1 to 5 using a for loop
for num in range(1, 6):

   print(num)
# Example: Print numbers from 1 to 10 and classify them as even or odd using a for loop with if-elif statement
for num in range(1,11):
   if num%2==0:
     print(num,"is even")
   else:
     print(num,"is odd") 
# Example: Print numbers from 1 to 5, skipping even numbers using a for loop with continue statement
for num in range(1,6):
  if num%2==0:
    continue
  print(num)
# Example: Iterate over each character in a string
word="Python"
for char in word:
  print(char)
  
#Example:Iterate over each element in a list
numbers=[1,2,3,4,5]
for num in numbers:
  print(num)  
  
#Print each fruit in a fruit list:  
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
#Loop through the letters in the word "banana":
for x in "banana":
  print(x)
#Print each adjective for every fruit:

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)  