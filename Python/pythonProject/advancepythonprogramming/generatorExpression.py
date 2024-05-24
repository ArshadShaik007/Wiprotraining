gen=('even' if i%2==0 else 'odd' for i in range(10))
for i in gen:
    print(i)