def fibo(nums):
    x,y=0,1
    for p in range(nums):
        x,y=y,x+y
        yield x
def square(nums):
    for num in nums:
        yield num**2
print(sum(square(fibo(5))))