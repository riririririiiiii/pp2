#ex1
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

#ex5
from itertools import permutations

def print_permutations(s):
    perms = permutations(s)
    for perm in perms:
        print(''.join(perm))

user_input = input()
print()
print_permutations(user_input)

#ex6
def reverse(str):
    a=str[::-1]
    print(a)
reverse("We are ready")   

#ex7
def has_33(nums):
    for i in range(len(nums) - 1):
     if nums[i] == 3 and nums[i + 1] == 3:
      return True
    return False
num1=[1, 3, 2, 3]
num2=[1, 3, 3, 2]
print(has_33(num1))
print(has_33(num2))

#ex8
def spy_game(nums):
    t=False
    for i in range(len(nums)-1):
        if nums[i]==0 and nums[i+1]==0 and nums[i+2]:
            t= True
            break
        else:
            continue
    print(t)
    
spy_game([1,2,4,0,0,7,5])
spy_game([1,0,2,4,0,5,7])
spy_game([1,7,2,0,4,5,0])

#ex9
def volume(radius):
    P=3.14
    result=4*P*radius*radius
    print(result)
volume(5)

#ex10
def newlist(mylist):
    uniquelist = []
    for i in range(len(mylist)):
        if mylist[i] not in uniquelist:
            uniquelist.append(mylist[i])
    print(uniquelist)

mylist = [1,1,12,2]
newlist(mylist)

#ex11
def palindrome(word):
    word = word.lower() 
    if word[::-1] == word:
        print("Yes")
    else:
        print("No")

palindrome("anna")

#ex12
def histogram(numbers):
    for i in numbers:
        print( "*" * i)       
numbers =4,9,7
histogram(numbers)

#ex13
import random
def guess():
    print("Hello! What is your name?")
    b = input()
    d = random.randint(1,20)
    print(f'Well, {b}, I am thinking of a number between 1 and 20.\nTake a guess.')
    c = int(input())
    i=1
    while c != d:
        if c<d:
            print('Your guess is too low.\nTake a guess.')
        else:
            print('Your guess is too high.\nTake a guess.')
        i+=1
        c = int(input())
    print(f'Good job, {b} You guessed my number in {i} guesses!')
guess()

   