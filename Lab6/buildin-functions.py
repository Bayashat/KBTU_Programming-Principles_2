# 1. Write a Python program with builtin function to multiply all the numbers in a list
from functools import reduce
l = [1, 2, 3, 4, 5]

print(reduce(lambda x, y: x*y, l))  # 120

# 2. Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters
s = 'Hello World'

print(len([i for i in s if i.isupper()]))  # 2
print(len([i for i in s if i.islower()]))  # 8

# 3. Write a Python program with builtin function that checks whether a passed string is palindrome or not.
s = 'madam'
print(s == s[::-1])  # True

# 4. Write a Python program that invoke square root function after specific milliseconds. 
#     ```
#     Sample Input:
#     25100
#     2123
#     Sample Output:
#     Square root of 25100 after 2123 miliseconds is 158.42979517754858
#     ````

def sqrt(n, t):
    import time
    time.sleep(t/1000)
    print(f'Square root of {n} after {t} miliseconds is {n**0.5}')
    
sqrt(25100, 2123)

# 5. Write a Python program with builtin function that returns True if all elements of the tuple are true.

t = (1, 2, 3, 4, 5)

print(all(t))  # False