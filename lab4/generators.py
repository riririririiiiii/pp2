#ex1
def gen_func(n):
    for i in range(n):
        yield i**2
n = 3
for square in gen_func(n):
    print(square)

#ex2
def gen_even(n):
    for i in range(0, n+1):
        if i % 2 == 0:  
            yield i

n = int(input("Enter a number: "))
result = gen_even(n)
even_numbers_list = list(result)
even_numbers_str = ', '.join(map(str, even_numbers_list))
print(even_numbers_str)

#ex3
def gen(n):
    for i in range(n):
        if i % 4 == 0 and i % 3 ==0:
            yield i
n = int(input())
divisible = gen(n)
for n in divisible:
    print(n)

#ex4
def squares(a, b):
    for i in range(a, b+1):
        yield i**2

a = int(input())
b = int(input())

for square in squares(a, b):
    print(square)

#ex5
def countdown(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input("Enter a number: "))
for number in countdown(n):
    print(number, end=' ')
