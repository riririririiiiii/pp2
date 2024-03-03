#ex1
import math

def multiply_list(numbers):
    if not numbers:
        return None  
    return math.prod(numbers)
input_list = input("Enter a list of numbers separated by space: ").split()
numbers = [int(num) for num in input_list]

result = multiply_list(numbers)
print(result)

#ex2
def count_letters(str):
    upper_count = sum(1 for char in str if char.isupper())
    lower_count = sum(1 for char in str if char.islower())
    return upper_count, lower_count
str = input("Enter a string: ")
result = count_letters(str)
print(result)

#ex3
def check_palindrome(str):
    str = ''.join(char.lower() for char in str if char.isalnum())
    x = slice(None, None, -1) 
    reversed_str = str[x] 
    return str == reversed_str

str = input("Enter a string: ")
if check_palindrome(str):
        print("The string is a palindrome")
else: 
        print("The string is not a palindrome")

#ex4
import time
import math

def calculate_square_root(number, milliseconds):
    time.sleep(milliseconds / 1000)  
    result = math.sqrt(number)
    print(f"Square root of {number} after {milliseconds} milliseconds is {result}")

number = 25100
milliseconds = 2123

calculate_square_root(number, milliseconds)

#ex5
t = (5, 0, 3, 1, False)
print(all(t))


