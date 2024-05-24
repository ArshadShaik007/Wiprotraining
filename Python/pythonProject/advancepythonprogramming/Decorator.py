def make_pretty(fun):
    def inner():
        print("decorateed")
        fun()
    return inner
@make_pretty
def ordinary():
    print("ordinary")

de_fun_value=make_pretty(ordinary)
de_fun_value()