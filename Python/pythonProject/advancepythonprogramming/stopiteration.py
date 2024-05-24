#stop iteration

iter_value="hello world"
iter_object=iter(iter_value)
while True:
    try:
        print(next(iter_object))
    except StopIteration:
        break

