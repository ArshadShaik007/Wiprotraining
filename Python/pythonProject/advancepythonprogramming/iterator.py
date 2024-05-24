# iterate with iter() to initialize list and next method to iterate through object
ls=[12,3,5,7,84,2,5]
my_iter = iter(ls)
print(next(my_iter))
print(my_iter.__next__())
# using iter with the string

iter_string=iter("hello world")

for obj in iter_string:
    print(obj)

