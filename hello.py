# data type
a = 5   # a is an integer
b = 5.0 # b is a float
c = '5' # c is a string
d = True
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))

# Arithmetic operations: +, -, *, /, //, %, **
a = 8
b = 2
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b}')       # true division
print(f'{a} // {b} = {a // b}')     # floor division
print(f'{a} % {b} = {a % b}')
print(f'{a} ** {b} = {a ** b}')     # a to the power of b 
print(f'sqrt({9}) = {9 ** 0.5}')

# Comparison operations: ==, !=, >, <, >=, <=

# Boolean operations: and, or, not
a = True
b = False
print(f'{a} and {b} = {a and b}')
print(f'{a} or {b} = {a or b}')
print(f'not {a} = {not a}')

s = 'Hello World'
a = 5
b = 2/3
print(f'|{s:25}|')
print(f'|{a:25}|')
print(f'|{b:25}|')
print(f'|{b:25.2f}|')
print(f'|{s:>25}|')
print(f'|{a:<25}|')
print(f'|{b:^25.2f}|')