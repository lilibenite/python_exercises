# Name: Lili
# Project: Python Exercises
# Exercises 1–10

# -------------------------
# Exercise 1
# -------------------------
print("Hello, Python!")

# -------------------------
# Exercise 2
# -------------------------
name = "Lili"
age = 18
print("Name:", name, "Age:", age)

# -------------------------
# Exercise 3
# -------------------------
user_input = input("Enter something: ")
print("You entered:", user_input)

# -------------------------
# Exercise 4
# -------------------------
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Sum:", num1 + num2)

# -------------------------
# Exercise 5
# -------------------------
print("Subtract:", num1 - num2)
print("Multiply:", num1 * num2)
print("Divide:", num1 / num2)

# -------------------------
# Exercise 6
# -------------------------
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# -------------------------
# Exercise 7
# -------------------------
minutes = int(input("Enter minutes: "))
hours = minutes // 60
remaining_minutes = minutes % 60
print(hours, "hours and", remaining_minutes, "minutes")

# -------------------------
# Exercise 8
# -------------------------
n = int(input("Enter a number: "))
print("Square:", n ** 2)
print("Cube:", n ** 3)

# -------------------------
# Exercise 9
# -------------------------
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

# Swap using temporary variable
temp = a
a = b
b = temp
print("After swap (with temp): a =", a, ", b =", b)

# Swap without temporary variable
a, b = b, a
print("After swap (without temp): a =", a, ", b =", b)

# -------------------------
# Exercise 10
# -------------------------
length = float(input("Enter length: "))
width = float(input("Enter width: "))
area = length * width
print("Area of rectangle:", area)