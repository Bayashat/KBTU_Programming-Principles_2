# 1
def gram_to_ounces(gram):
    return 28.3495231 * gram

# 2
def Fahrenheit_to_Celsius(F):
    return (F - 32) * 5 / 9

# 3
def solve(numheads, numlegs):
    rabbits = numlegs / 2 - numheads
    chickens = numheads - rabbits
    return rabbits, chickens

# 4
def filer_prime(numbers: list[int]) -> list[int]:
    prime_numbers = []
    for num in numbers: # 7
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime and num > 1:
            prime_numbers.append(num)
    return prime_numbers
    
# 5
from itertools import permutations
def print_permutations(s: str):
    for permutation in permutations(s):
        print("".join(permutation))

# 6
def reverse_input(s: str) -> str:
    return s[::-1]

# 7
def has_33(numbers: list[int]) -> bool:
    for i in range(len(numbers)-1):
        if numbers[i] == 3 and numbers[i+1] == 3:
            return True
    return False

# 8
def spy_game(numbers: list[int]) -> bool:
    tmp = []
    for i in range(len(numbers)):
        if numbers[i] == 0 and len(tmp) < 2:
            tmp.append(0)
        if numbers[i] == 7 and len(tmp) == 2:
            tmp.append(7)
    
    return True if tmp == [0,0,7] else False
   
   
# 9
import math   
def volume_of_sphere(radius: float) -> float:
    return f"{(4/3) * math.pi * (radius**2):.2f}"

# 10
from typing import Any
def unique_elements(l: list[Any]) -> list[Any]:
    res = []
    for element in l:
        if element not in res:
            res.append(element)
    return res

# 11
def check_palindrome(s: str) -> bool:
    return True if s == s[::-1] else False

# 12
def histogram(columns: list[int]):
    for num in columns:
        print("*" * num)
        
# 13
import random
def play(random_number, name, cnt):
    cnt += 1
    guess = int(input("Take a guess.\n"))
    if guess == random_number:
        print(f"Good job, {name}! You guessed my number in {cnt} guesses!")
        return 0
    elif guess > random_number:
        print("Your guess is too high.")
        play(random_number, name, cnt)
    else:
        print("Your guess is too low.")
        play(random_number, name, cnt)
        

def guess_number():
    random_number = random.randint(1, 20)
    name = input("Hello! What is your name? ")
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    play(random_number, name, 0)

# 14
# created "test_file.py"