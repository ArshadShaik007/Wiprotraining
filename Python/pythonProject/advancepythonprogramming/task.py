'''
#Remove floats from given list of numbers
rmv_floats = [x for x in [1, 2.5, 6, 7.8, 9] if not (isinstance(x,float))]
print(rmv_floats)
# count number of spaces in a string
spaces = [y for y in "hello this is sunny here" if y == " "]
print(len(spaces))

# find common numbers in two lists of numbers
common = [x for x in [10, 2, 3, 6, 7, 97, 5, 4] if x in [12, 3, 4, 6, 2, 9, 10]]
print(common)

# constants in a string
cns = [i for i in "this is an example string" if i not in "aeiou "]
print(cns)

class Power:
    def __init__(self,num):
        self.num=num
    def next_(self):
        # return the next iterator element
        self.num **= 2
        return self.num

p=Power(2) #object creation
print(p.next_()) #getting the next iterator
print(p.next_()) #getting the next iterator
print(p.next_()) #getting the next iterator

tup=(1,2,3,4)
tup_iter=iter(tup)
print(next(tup_iter))

# generator for cube of numbers from 1 to n

gen= (i**3 for i in range(1,10))
print(gen)
for i in gen:
    print(i)

# prime numbers between range

def primebetween(a,b):
    for i in range (a,b+1):
        if i >1:
            for j in range(2,i):
                if i%j==0:
                    break
                else:
                    yield i


for i in primebetween(7,50):
    print(i)
'''

def reverse(fun):
    def inner (str):
        return str[::-1]
    return inner

@reverse
def deco(str):
    return str
print(deco("string is reveresed like oxo"))

def divecor(fun):
    def inner (x,y):
        return x/y
    return inner
@divecor
def div(x,y):
    return (divecor(div))
print(div(2,3))