# ===============================================================
# PYTHON BASICS - COMPLETE NOTES WITH EXAMPLES
# ===============================================================

# 1. Printing Output
# What: The print() function displays output on the screen.
# Why: Used to show text, numbers, or results of calculations.
# Example:
print("Hello World")            # Prints a simple text
print("My name is Vishal.")     # Prints another string
print(23)                       # Prints an integer directly
print(35 + 32)                  # Prints result of an arithmetic expression


# 2. Variables
# What: A variable is a name that stores data in memory.
# Why: Instead of writing values again and again, we store them in variables.
# Example:
name = "Vishal"   # String type variable (text data)
age = 24          # Integer type variable (whole number)
price = 24.55     # Float type variable (decimal number)

print(name)
print(price)
print("My name is:", name)
print("My age is:", age)

# Copying value of one variable to another
age2 = age
print("Copied age:", age2)


# 3. Checking Data Types
# What: type() function shows the data type of a variable.
# Why: Useful when you want to know what kind of data is stored.
# Example:
print(type(name))   # str (string)
print(type(age))    # int (integer)
print(type(price))  # float (decimal)


# 4. Different Ways to Write Strings
# What: Strings can be written in single, double, or triple quotes.
# Why: Flexibility, and triple quotes are useful for multi-line strings.
# Example:
name1 = 'Vishal'
name2 = "vishal"
name3 = '''vishal'''

print(name1)
print(name2)
print(name3)


# 5. More Data Types
# Boolean (True/False) – used in conditions.
# None – represents "nothing" or "no value".
# Example:
old = True      # Boolean type (True/False values)
a = None        # NoneType (represents "nothing")

print(type(old))   # bool
print(type(a))     # NoneType


# 6. Basic Arithmetic
# What: You can do math operations with variables.
# Example:
a = 2
b = 5
sum = a + b
print("Sum =", sum)

diff = a - b
print("Difference =", diff)


# 7. Arithmetic Operators
# What: Symbols used for calculations.
# Examples:
# + addition
# - subtraction
# * multiplication
# / division
# % modulus (remainder)
# ** exponent (power)
a = 10
b = 2
print(a + b)   # Addition → 12
print(a - b)   # Subtraction → 8
print(a * b)   # Multiplication → 20
print(a / b)   # Division → 5.0
print(a % b)   # Modulus (remainder) → 0
print(a ** b)  # Exponentiation (a^b) → 100


# 8. Relational (Comparison) Operators
# What: Compare values, return True or False.
# Examples:
a = 10
b = 20
print(a == b)   # Equal → False
print(a != b)   # Not Equal → True
print(a > b)    # Greater → False
print(a < b)    # Less → True
print(a >= b)   # Greater or Equal → False
print(a <= b)   # Less or Equal → True


# 9. Assignment Operators
# What: Assign and update values.
# Examples:
a = 10
b = 20

a += b   # a = a + b → 30
print(a)

a -= 5   # a = a - 5 → 25
print(a)

a *= 2   # a = a * 2 → 50
print(a)

a /= 5   # a = a / 5 → 10.0
print(a)


# 10. Type Conversion (Automatic)
# What: Python automatically converts one type to another when needed.
# Example:
a = 2       # int
b = 5.5     # float
sum = a + b
print(sum)         # 7.5
print(type(sum))   # float


# 11. Type Casting (Manual)
# What: Manually change one type to another.
# Example:
# String → Integer
a = int("2")     # "2" becomes 2
b = 4.34
print(a + b)     # 6.34
print(type(a))   # int

# Float → String
a = 3.14
b = str(a)       # "3.14"
print(b, type(b))


# 12. TAKING INPUT FROM USER
# What: input() lets you take input from keyboard.
# Note: Always returns string, so we use int() or float() if needed.
# Example:
# Uncomment the lines below to test with user input

name = input("Enter your name: ")
print("Hello", name)

name = input("Enter your name: ")
age = int(input("Enter your age: "))         # input → int
marks = float(input("Enter your marks: "))   # input → float
print("Hello", name)
print("Your age is", age)
print("Your marks are", marks)


# 13. PRACTICE PROGRAMS
# (i) Sum of two numbers
first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
print("Sum is", first + second)

# (ii) Area of a square
side = float(input("Enter side of square: "))
print("Area of square is", side * side)

# (iii) Average of two floating numbers
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
print("Average is", (x + y) / 2)

# (iv) Compare two integers
a = int(input("Enter a: "))
b = int(input("Enter b: "))
print(a >= b)    # True if a ≥ b, else False


# 14. RULES FOR IDENTIFIERS
# Can contain letters, digits, underscore.
# Cannot start with digit.
# Cannot be keyword (if, class, etc.).
# Case-sensitive.
# Valid identifiers
my_name = "Vishal"
age2 = 24
_total = 100

# Invalid identifiers (❌ do not run these)
# 2name = "wrong"      # starts with number
# class = "python"     # class is a keyword


# 15. KEYWORDS IN PYTHON
# What: Reserved words with special meaning in Python.
# Why: Cannot use them as variable names.
# Example:
import keyword
print("Python Keywords are:")
print(keyword.kwlist)


# 16. COMMENTS IN PYTHON
# Single-line → starts with #.
# Multi-line → use triple quotes """ """.
# Single-line comment → starts with #
print("Hello World")   # This prints a message

"""
Multi-line comment
can be written inside
triple quotes
"""
print("Python is easy")


# 17. LOGICAL OPERATORS
# What: Combine conditions.
# Operators:
# and → True if both conditions are True
# or → True if at least one is True
# not → reverses the result
a = 10
b = 5

print(a > 5 and b < 10)   # True (both conditions are True)
print(a > 5 or b > 10)    # True (at least one is True)
print(not (a > b))        # False (because a > b is True, not reverses it)
