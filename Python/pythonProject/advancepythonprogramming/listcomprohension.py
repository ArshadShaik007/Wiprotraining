# list comprohension
s = range(1,1001)

divisibles = [num for num in s if num % 7 == 0]
print(divisibles)
# even n odd
evn = [num for num in range(1,21) if num % 2 == 0]
od = [num for num in range(1,21) if num % 2 != 0]
print("even : ", evn)
print("odd", od)
# Matrix
matrix = [[i for i in range(3)] for i in range(3)]
print(matrix)

# if else
even_or_odd=['even' if i%2==0 else 'odd' for i in range(10)]
print(even_or_odd)
# nested if
divby5n2 = [y for y in range(101) if y % 2 == 0 if y % 5 == 0]
print(divby5n2)

# print x in range
print([x for x in range(50) if x % 2 == 0])