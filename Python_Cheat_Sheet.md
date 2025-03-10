# Python Cheat Sheet
made by me and a tiny bit of ai help

## Variables and Data Types
```python
x = 5           # Integer
y = 3.14        # Float
name = "Alice"  # String
is_valid = True # Boolean
```

## Basic Operations
```python
# Arithmetic
sum = 5 + 3
difference = 5 - 3
product = 5 * 3
quotient = 5 / 3
remainder = 5 % 3

# Comparison
equal = (5 == 3)
not_equal = (5 != 3)
greater_than = (5 > 3)
less_than = (5 < 3)
```

## Lists
```python
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")  # Add item
fruits.remove("banana")  # Remove item
print(fruits[0])         # Access item
```

## Dictionaries
```python
person = {"name": "Alice", "age": 25}
print(person["name"])    # Access value
person["age"] = 26       # Modify value
```

## Loops
```python
# For loop
for i in range(5):
    print(i)

# While loop
count = 0
while count < 5:
    print(count)
    count += 1
```

## Functions
```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))
```

## Classes
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name}."

p = Person("Alice", 25)
print(p.greet())
```

## Importing Modules
```python
import math
print(math.sqrt(16))  # Output: 4.0
```

## File Handling
```python
# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, World!")

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
```

## Exception Handling
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
```
