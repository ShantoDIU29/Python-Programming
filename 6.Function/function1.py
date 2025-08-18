#introduction to function in python
def sums(a,b):
  return a+b
result=sums(5,4)
print(result)
#dafult parameter add
def add(a,b,c=0):
  return a+b+c
result1=add(5,4)
result2=add(5,4,3)
print(result1)
print(result2)
#*args function
def add(*args):

  sum=0
  for num in args:
    sum=sum+num
    return sum
result=add(5,4) 
print(result) 
#**kwargs 
def func( **kwargs):
  print(f"apple:{kwargs['apple']}")
  for key,value in kwargs.items():
    print(f'{key}:{value}')
result=func(apple=5,orange=4)    
   
