# infinite iterator
import itertools as it

# for loop

for i in it.count(5,5) :
    if i == 35:
        break
    else:
        print(i, end =" ")

# infinite itrator

infinite_iterator = it.count(1)
