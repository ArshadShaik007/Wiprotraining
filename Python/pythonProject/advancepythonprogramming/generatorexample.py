def smpl_gen():
    yield 1
    yield 2
    yield 3

for value in smpl_gen():
    print(value)