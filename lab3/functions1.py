#ex1
"""
def grams_to_ounces(g):
    ounces = 28.3495231 * g
    return ounces

g = float(input())

result = grams_to_ounces(g)

print(result)


#ex2
def cent_temp(F):
    C = (5 / 9) * (F - 32)
    return C
F = int(input())
result = cent_temp(F)
print(result)

#ex3
def find_chickens_and_rabbits(heads, legs):
    c = 0
    while c <= heads:
        r = heads - c
        if 2 * c + 4 * r == legs:
            return c, r
        c += 1
    return None

heads_count = 35
legs_count = 94

result = find_chickens_and_rabbits(heads_count, legs_count)

print(result)
"""
#ex4
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
        return True

def filter_prime(numbers):
    prime_numbers = []
    for num in numbers:
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers

numbers = list(map(int, user_input.split()))

prime_numbers = filter_prime(numbers)

print(prime_numbers)


   