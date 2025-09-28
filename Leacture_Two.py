# 1. Strings

# A string is a sequence of characters (letters, numbers, symbols).

str1 = "Hello World"       # Double quotes
str2 = 'Apna College'      # Single quotes
str3 = """This is 
a multi-line string"""     # Triple quotes # used for multi-line text.

print(str1)
print(str2)
print(str3)

# Output:
# Hello World
# Apna College
# This is 
# a multi-line string

# Example: "It's a good day"
# Example: 'He said "Python is easy"'

# 2.Concatenation in Python

# Concatenation means joining two or more strings together using the + operator.

#Important: Python does not add spaces automatically. If you want a space between words, you must add " " manually.

# Example 1: Without Space

first = "Vishal"
last = "Kumar"
print(first + last)   # Output: VishalKumar
# "Vishal" and "Kumar" are joined directly, so no space comes in between.

# Example 2: With Space

first = "Vishal"
last = "Kumar"
print(first + " " + last)   # Output: Vishal Kumar
# A space " " is added between the two strings.

# Example 3: Notes Example

print("hello" + "world")   # Output: helloworld

# Example 4: Using Variables and Text

name = "Python"
version = "3.12"
print("I am learning " + name + " version " + version)
# Output: I am learning Python version 3.12

# 3. Basic Operations (Length)

# Basic Operation: len() Function
# len(string) is a built-in Python function that returns the total number of characters in a string.
# Spaces, digits, and special characters are also counted as characters.

# Example 1: Simple String
my_str = "Apna College"
print("Length of string:", len(my_str))

# Output:
# Length of string: 12

# Example 2: Counting Spaces and Special Characters
txt = "Hello World!"
print(len(txt))   # Output: 12
# "Hello World!" → 11 letters + 1 space = 12.

# Example 3: Empty String
empty = ""
print(len(empty))   # Output: 0
# An empty string has zero characters.

# Example 4: String with Numbers
num_str = "Python123"
print(len(num_str))   # Output: 9
# Digits are also treated as characters.

# 4.String Indexing

# Indexing means accessing individual characters in a string using their position (index number).

# Python uses zero-based indexing → first character is at index 0.

# You can also use negative indexing → last character is at index -1, second last at -2, and so on.

# Example 1: Positive Indexing
str4 = "Apna_College"

print(str4[0])   # 'A'  → first character
print(str4[1])   # 'p'  → second character
print(str4[5])   # 'C'  → sixth character

# Example 2: Negative Indexing
print(str4[-1])   # 'e'  → last character
print(str4[-2])   # 'g'  → second last
print(str4[-7])   # '_'  → seventh from last

# Example 3: Using Index in Loops
for i in range(len(str4)):
    print("Index", i, ":", str4[i])
# Output:
# Index 0 : A
# Index 1 : p
# Index 2 : n
# Index 3 : a
# Index 4 : _
# Index 5 : C
# Index 6 : o
# Index 7 : l
# Index 8 : l
# Index 9 : e
# Index 10 : g
# Index 11 : e

# Example 4: Error Case
print(str4[20])   # ❌ IndexError
# Since "Apna_College" has only 12 characters, index 20 doesn’t exist.

# 5. Slicing

# Slicing is used to extract a part of a string (or sequence)

# string[start:end]

# start → the index where slicing begins (inclusive).
# end → the index where slicing ends (exclusive, not included).

# indexing starts at 0.

# Examples
text = "Apna College"

# 1.Basic slicing
print(text[0:4])  # Output: 'Apna' (from index 0 to 3)

# 2.Slicing from start
print(text[:5])  # Output: 'Apna ' (from start to index 4)

# 3.Slicing till end
print(text[5:])  # Output: 'College' (from index 5 to the end)

# 4.Negative indexing in slicing
print(text[-7:-1])  # Output: 'Colleg' (from 7th last to 2nd last character)

# 5.Skipping characters (step)
# Syntax: string[start:end:step]
print(text[0:10:2])  # Output: 'AaCleg'
# step=2 → takes every second character



# 6. Escape Sequences

# Special characters inside strings:
# \n → New Line
# \t → Tab Space

str6 = "Hello\nWorld"
print(str6)
# Output:
# Hello
# World

str7 = "Hello\tWorld"
print(str7)
# Output:
# Hello   World



# 7. String Functions
# Useful built-in functions for strings:

# 1. endswith()
# Checks if the string ends with the specified substring. Returns True or False.
str8 = "i am a coder."
print(str8.endswith("er."))  # True
print(str8.endswith("coder")) # False

# 2. count()
# Counts the number of times a substring appears in the string.

print(str8.count("am"))  # 1
print(str8.count("a"))   # 2

# 3. capitalize()
# Capitalizes the first character of the string, making the rest lowercase.

print(str8.capitalize())  # "I am a coder."

# 4. find()
# Returns the index of the first occurrence of a substring. Returns -1 if not found.
print(str8.find("am"))    # 2
print(str8.find("coder")) # 7
print(str8.find("python"))# -1

# 5. replace()
# Replaces a specified substring with another string.

print(str8.replace("coder", "programmer"))  
# "i am a programmer."


# 8. Practice with Input

# 1. Input first name & print length
name = input("Enter your first name: ")
print("Length of your name:", len(name))

# Output:
# Enter your first name: vishal
# Length of your name: 6

# 2. Count $ in a string
str9 = "Hi, $ I am $ Vishal $99"
print("Count of $:", str9.count("$"))

# Output:
# Count of $: 3


# 9. Conditional Statements
# What are Conditional Statements?

# Conditional statements allow your program to make decisions based on certain conditions.
# The main statements are:

# if → Executes a block if the condition is True.

# elif → Checks another condition if previous if was False.

# else → Executes when all previous conditions are False

# if condition:
     # code block
# elif condition:
     # another block
# else:
     # default block

# Example – Voting Age
age = 21

if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")
# Output: You can vote


# Example – Traffic Light
light = "Red"

if light == "Red":
    print("Stop")
elif light == "Yellow":
    print("Get Ready")
else:
    print("Go")

# Output: Stop


# Example – Grading System
marks = 87

if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
else:
    grade = "D"

print("Grade of the Student ->", grade)

# Output: Grade of the Student -> B

# Example – Nested if
age = 89

if age >= 18:
    if age >= 80:
        print("Cannot Drive")
    else:
        print("Can Drive")
else:
    print("Cannot Drive")

# Output: Cannot Drive

# First checks if age is 18 or above.
# Inside that, checks if age is 80 or above → then "Cannot Drive".
# Nested if allows multiple layers of decisions.



# 10. Practice Questions 
# Q1. Odd or Even

# Take input from user and convert to integer
num = int(input("Enter a number: "))

# Check if number is divisible by 2
if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

# Output:
# Enter a number: 7
# Odd Number


# Q2. Greatest of 3 Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("First number is greatest:", a)
elif b >= c:
    print("Second number is greatest:", b)
else:
    print("Third number is greatest:", c)
# Output:
# Enter first number: 45
# Enter second number: 78
# Enter third number: 12
# Second number is greatest: 78



# Q3. Multiple of 7
x = int(input("Enter a number: "))
if x % 7 == 0:
    print("Multiple of 7")
else:
    print("Not a multiple of 7")

# Output:
# Enter a number: 49
# Multiple of 7