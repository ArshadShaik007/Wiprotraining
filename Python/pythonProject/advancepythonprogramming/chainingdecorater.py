def decor(fun):
    def inner():
        print("decoreted")
        fun()
    return inner
def decor1(fun):
    def inner():
        print("to much decoreted")
        fun()
    return inner
@decor
@decor1
def num():
    return 20
num()
