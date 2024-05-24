# normal function defination

def add(a,b):
    return a+b
print(add(3,7))
#lambda function

# example 1

mul = lambda x: x*100

print(mul(50))

# example 2

add = lambda a,b: a+b

print(add(3,7))

# example 3

prod= lambda x,y,z: x*y*z

print(prod(y=2,x=4,z=5))

# pass argumrnts in the lambda functions

add = lambda *args : sum(args)

print(add(1,2,3,5,75,3,23,45,2,34))

#if

#filter the string

sub_string =lambda string : string in "welcome to python"
print(sub_string("to"))

# filter lists

num=[10.20,30,40,50,60]
greater= list(filter(lambda num : num >30 ,num))
print(greater)

# even and odd
num=[11.20,39,40,53,62]
even= list(filter(lambda i: i%2==0 ,num))
print(even)

num=[11.20,39,40,53,62]
odd= list(filter(lambda i: i%2!=0 ,num))
print(odd)

# div by 4

num=[11.20,39,40,53,62]
div= list(filter(lambda i: i%4==0 ,num))
print(div)

# age greater than 18

age=[11.20,39,40,53,62]
eligible= list(filter(lambda i: i>18 ,num))
print(eligible)

# maps

num=[11.20,39,40,53,62]

double = list(map(lambda i: i*2,num))
print(double)

# power of 2

num=[11,20,39,40,53,62]
square = list(map(lambda i: i**2,num))
print(square)

# divided by 10

num=[11, 20, 39, 40, 53, 62]
divby10 = list(map(lambda i: i/10,num))
print(divby10)

# reduce
from functools import reduce
list1=[11,20,39,40,53,62]
sum = reduce((lambda x, y: x+y), list1)
print(sum)
