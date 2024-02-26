import math
# 1
class StrManipulate:
    def get_string(self):
        self.string = input("Enter string: ")
        
    def print_string(self):
        print(self.string)
        

# 2
class Shape:
    def __init__(self) -> None:
        pass
    
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length) -> None:
        self.length = length
        
    def area(self):
        return self.length**2
    

# 3
class Rectangle(Shape):
    def __init__(self, length, width) -> None:
        self.length = length
        self.width = width
        
    def area(self):
        return self.length * self.width
    

# 4
class Point:
    def __init__(self, x, y) -> None:
        self.coordinates = (x, y)
        
    def show(self):
        print(self.coordinates)
        
    def move(self, x, y):
        self.coordinates = (x, y)
        
    def dist(self, other: 'Point'):
        x1, y1 = self.coordinates
        x2, y2 = other.coordinates
        
        return f"{math.sqrt((x2-x1)**2 + (y2-y1)**2):.2f}"
    
p = Point(2, 2)
p.show()
p.move(3, 4)
p.show()
c = Point(0, 0)
print(c.dist(p))

# 5
class Account:
    def __init__(self, owner, balance=0.0) -> None:
        self.owner: str = owner
        self.balance: float = balance
        
    def deposit(self, amount):
        self.balance += amount
        return f"Deposit {amount} successfull"
    
    def withdraw(self, amount):
        try:
            balance = self.balance - amount
            if balance < 0:
                raise ValueError("Exceed available balance")
            else:
                self.balance = balance
                return f"Withdraw {amount} successfull"
        except ValueError as e:
            print(e)
        
        
    

a = Account("Bayashat")
a.withdraw(500)
a.deposit(800)
print(a.balance)
a.withdraw(400)
print(a.balance)
a.withdraw(400)
print(a.balance)



# 6
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
    
    
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

prime_numbers = list(filter(is_prime, numbers))
print(prime_numbers)