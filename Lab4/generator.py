# 1. Create a generator that generates the squares of numbers up to some number `N`.
def squares(N):
    for i in range(N):
        yield i ** 2
    

squares_gen = squares(10)
print(next(squares_gen))  # 0
print(next(squares_gen))  # 1
print(next(squares_gen))  # 4


# 2. Write a program using generator to print the even numbers between 0 and `n` in comma separated form where `n` is input from console.

def even_numbers(n):
    for i in range(0, n, 2):
        yield i


n = int(input())
even_gen = even_numbers(n)
print(*even_gen, sep=",")  # 0, 2, 4, 6, 8

# 3. Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and `n`.

def divisible_by_3_and_4(n):
    for i in range(n):
        if i % 3 == 0 and i % 4 == 0:
            yield i
        

n = int(input())

for num in divisible_by_3_and_4(n):
    print(num)
    

# 4. Implement a generator called `squares` to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.

def squares(a, b):
    for i in range(a, b):
        yield i ** 2
        

a = int(input())
b = int(input())


for num in squares(a, b):
    print(num)
    
# 5. Implement a generator that returns all numbers from (n) down to 0.
def squares(N):
    for i in range(N, 0, -1):
        yield i
    

squares_gen = squares(10)
print(next(squares_gen))  # 0
print(next(squares_gen))  # 1
print(next(squares_gen))  # 4