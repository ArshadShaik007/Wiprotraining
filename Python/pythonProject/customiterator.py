class Prime:
    def __init__(self):
        self.num = 1
    def is_prime(self,num):
        for i in range(2,num):
            if num % i == 0:
                return False
        return True
    def next_(self):
        # return the next iterator element
        self.num+=1
        while not self.is_prime(self.num):
            self.num+=1
        return self.num

p=Prime() #object creation
print(p.next_()) #getting the next iterator